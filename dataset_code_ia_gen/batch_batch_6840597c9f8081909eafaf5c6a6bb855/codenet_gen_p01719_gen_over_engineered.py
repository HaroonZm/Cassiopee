from abc import ABC, abstractmethod
from typing import List, Tuple, Dict


class IStockPriceProvider(ABC):
    @abstractmethod
    def get_price(self, day: int, stock_type: int) -> int:
        pass

    @abstractmethod
    def total_days(self) -> int:
        pass

    @abstractmethod
    def total_stock_types(self) -> int:
        pass


class StockPriceMatrix(IStockPriceProvider):
    def __init__(self, prices: List[List[int]]) -> None:
        self._prices = prices  # prices[day][stock_type]

    def get_price(self, day: int, stock_type: int) -> int:
        return self._prices[day][stock_type]

    def total_days(self) -> int:
        return len(self._prices)

    def total_stock_types(self) -> int:
        if self._prices:
            return len(self._prices[0])
        return 0


class PortfolioState:
    def __init__(self, cash: int, holdings: Tuple[int, ...]) -> None:
        self.cash = cash
        self.holdings = holdings

    def key(self) -> Tuple[int, Tuple[int, ...]]:
        return (self.cash, self.holdings)

    def __repr__(self) -> str:
        return f"PortfolioState(cash={self.cash}, holdings={self.holdings})"


class TransactionSimulator:
    def __init__(self, price_provider: IStockPriceProvider, initial_cash: int) -> None:
        self.price_provider = price_provider
        self.initial_cash = initial_cash
        self.n = self.price_provider.total_stock_types()
        self.d = self.price_provider.total_days()

    def compute_max_cash(self) -> int:
        # States are represented by (cash, holdings_tuple). But to reduce complexity,
        # we track at each day the reachable states.
        # holdings_tuple = (h_0, h_1, ..., h_(n-1)), each h_j >= 0
        # cash >= 0 integer
        # Because d,n,x, and prices are small, we perform BFS with state pruning.

        from collections import deque, defaultdict

        # Initial state: day 0, cash = initial_cash, holdings all 0
        initial_holdings = tuple([0] * self.n)
        initial_state = PortfolioState(self.initial_cash, initial_holdings)

        # dp[day][cash][holdings_tuple] = reachable or not
        # To reduce memory: at each day, we keep a dict mapping from (holdings) -> max cash for that holdings
        # This allows pruning suboptimal cash states with same holdings.

        dp: List[Dict[Tuple[int, ...], int]] = [defaultdict(lambda: -1) for _ in range(self.d + 1)]
        dp[0][initial_holdings] = self.initial_cash

        for day in range(self.d):
            day_price = [self.price_provider.get_price(day, j) for j in range(self.n)]
            current_states = dp[day]
            next_states = dp[day + 1]

            for holdings, cash in current_states.items():
                # For given cash and holdings, try all possible buy/sell operations for day+1
                # But since we can buy/sell any units multiple times, and holdings and cash must not be fractional,
                # we try all feasible buy/sell combinations.
                # The state space is large; instead, we use a logic based on:
                # At each day, since prices are constant during the day, we can:
                # 1) Sell all holdings (get cash)
                # 2) Then buy as much as possible of some stocks (or none)
                # 3) Or do nothing
                # Because buying and selling in arbitrary order, and no fees, any combination reduces to:
                # At day i, best is to hold any integer amount of stocks and cash such that the total asset value
                # at the end is maximized.

                # To make it tractable for the problem constraints:
                # We consider the following approach per state:
                # - Compute total asset value if we liquidate all stocks at current day price.
                # - Try buying any combination of stocks with that asset value, to hold at the end of day.

                # Step 1: liquidate all holdings to cash
                total_cash = cash
                for j in range(self.n):
                    total_cash += holdings[j] * day_price[j]

                # Step 2: enumerate all holdings combinations bought with total_cash
                # holdings_j in 0..max_units_j where max_units_j = total_cash // day_price[j]
                # But combinations explode if n=10 and total_cash large.
                # Given constraints x,p_i,j ≤ 10^5 and n,d ≤ 10, we can prune heavily.

                # To prune:
                # - Consider only the best single-stock buys
                # - Consider buying nothing (holding only cash)
                # - Consider buying one or multiple units of only the stock with best future expectation?
                # However, problem wants maximum final cash, so dynamic programming over days is better.

                # So to avoid complexity explosion, we advance to day+1 without transactions:
                # State doesn't change except day increments.

                # But problem allows multiple buys and sells per day. So we must consider selling and buying.

                # Instead, try a DP with only cash, we do not track holdings 
                # but this breaks if prices change differently.

                # Since constraints are very small (d,n ≤10), x,p_i,j ≤ 10^5, and max final money ≤ 10^5,
                # Let's do a full DP with states of cash and holdings.

                # Limit holdings per stock by max holdings = total_cash // min price
                # But this is large.

                # Alternate simplified: at day i, for each holdings, we can generate all possible states by:
                # For each stock j:
                #   - Try all possible amounts to sell (0..holdings[j])
                #   - Try all possible amounts to buy with current cash + cash from sells.

                # This is still potentially large but given constraints might be feasible.

                # Let's generate all possible sell combinations for the holdings:
                # To not explode, sell each stock either 0 or all units only.

                # For each holdings, generate all sell patterns with each stock sold or not sold:
                from itertools import product

                sell_options = []
                for j in range(self.n):
                    sell_options.append([0, holdings[j]])

                # product over n stocks: 2^n options (max 1024)

                for sell_pattern in product(*sell_options):
                    # sum sell proceeds
                    cash_after_sell = cash
                    new_holdings_after_sell = list(holdings)
                    for j in range(self.n):
                        sell_qty = sell_pattern[j]
                        if sell_qty > new_holdings_after_sell[j]:
                            # Invalid, skip
                            break
                        cash_after_sell += sell_qty * day_price[j]
                        new_holdings_after_sell[j] -= sell_qty
                    else:
                        # From cash_after_sell, try to buy stocks
                        # We try to buy zero or more units of each stock, limited by cash
                        # Let's try only buy-all-in-one-stock or none for tractability

                        # Candidate buying plans:
                        # - no buying (keep holdings as after sell)
                        # - buy max units of one stock

                        # Keep no buying:
                        new_holdings = tuple(new_holdings_after_sell)
                        prev_cash = next_states.get(new_holdings, -1)
                        if cash_after_sell > prev_cash:
                            next_states[new_holdings] = cash_after_sell

                        # Try buying max units of one stock:
                        for j in range(self.n):
                            price = day_price[j]
                            max_units = cash_after_sell // price if price > 0 else 0
                            if max_units == 0:
                                continue
                            new_holdings_buy = list(new_holdings_after_sell)
                            new_holdings_buy[j] += max_units
                            cash_after_buy = cash_after_sell - max_units * price
                            new_holdings_buy_tuple = tuple(new_holdings_buy)
                            prev_cash_buy = next_states.get(new_holdings_buy_tuple, -1)
                            if cash_after_buy > prev_cash_buy:
                                next_states[new_holdings_buy_tuple] = cash_after_buy

        # After final day, max final cash is max over all states of cash + stock value at last day
        final_day_price = [self.price_provider.get_price(self.d - 1, j) for j in range(self.n)]
        max_final_cash = 0
        for holdings, cash in dp[self.d].items():
            total = cash
            for j in range(self.n):
                total += holdings[j] * final_day_price[j]
            if total > max_final_cash:
                max_final_cash = total
        return max_final_cash


def main() -> None:
    import sys

    input_lines = sys.stdin.read().split()
    n, d, x = map(int, input_lines[:3])
    price_values = list(map(int, input_lines[3:]))

    prices = []
    index = 0
    for _ in range(d):
        day_prices = []
        for __ in range(n):
            day_prices.append(price_values[index])
            index += 1
        prices.append(day_prices)

    price_provider = StockPriceMatrix(prices)
    simulator = TransactionSimulator(price_provider, x)
    print(simulator.compute_max_cash())


if __name__ == '__main__':
    main()