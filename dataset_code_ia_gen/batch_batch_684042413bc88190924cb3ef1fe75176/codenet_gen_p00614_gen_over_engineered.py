class Coin:
    def __init__(self, denomination: int):
        self.denomination = denomination

    def __repr__(self):
        return f"Coin({self.denomination})"


class Wallet:
    def __init__(self, coins: dict):
        # coins: dict of denomination -> count
        self.coins = coins.copy()
        self.denominations = sorted(coins.keys(), reverse=True)

    def total_value(self):
        return sum(den * cnt for den, cnt in self.coins.items())

    def copy(self):
        return Wallet(self.coins)

    def remove_coins(self, spend_coins: dict):
        # spend_coins: dict denomination -> count
        for den, cnt in spend_coins.items():
            if cnt > self.coins.get(den, 0):
                raise ValueError("Not enough coins to remove")
            self.coins[den] -= cnt

    def get_coins_list(self):
        return [(den, cnt) for den, cnt in self.coins.items() if cnt > 0]


class ChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def calc_min_coins_change(self, change_amount):
        # Greedy algorithm because denominations are canonical
        change_coins = {}
        remain = change_amount
        for den in self.denominations:
            use = remain // den
            if use > 0:
                change_coins[den] = use
                remain -= den * use
        if remain != 0:
            raise RuntimeError("Cannot make exact change")
        return change_coins

    def count_coins(self, coins_dict):
        return sum(coins_dict.values())


class PaymentSolver:
    def __init__(self, price: int, wallet: Wallet, coin_set):
        self.price = price
        self.wallet = wallet
        self.coin_set = coin_set
        self.coin_list = sorted(coin_set, reverse=True)
        self.change_maker = ChangeMaker(self.coin_list)

    def solve(self) -> int:
        # We want to minimize paid_coins + change_coins
        # Paid coins used must cover at least price
        # Change is returned greedily with min coin count
        # The wallet has limited counts per coin.

        # Represent state as tuple of how many coins used of each denomination
        # Because of large coins counts (up to 1000 each), brute force all combinations impossible.

        # Plan:
        # Since coin denominations are few(6), we can try:
        # Enumerate possible paid coins combinations with pruning:
        # - Paid amount >= price
        # - Keep track of paid coins count, and overall min
        # We'll implement an optimized DFS with memoization on state of used coins counts and current sum.

        # To reduce complexity, we can impose an upper bound on sum of coins we consider:
        # Max sum is the total value in wallet.

        # To optimize, we can try dynamic programming based on sum:
        # DP[s] = minimum paid coins count to achieve sum s
        # Note that max s = wallet total value.

        max_sum = self.wallet.total_value()

        # dp array: for each amount s, store min number of coins paid to achieve s
        # Initialize with large number
        INF = 10**9
        dp = [INF] * (max_sum + 1)
        dp[0] = 0
        # For used count per sum, we do not track which coins were used but only minimal count (to limit complexity)
        # We'll implement bounded knapsack: for each denomination coin, for each count from 1 to N_i
        for den in self.coin_list:
            count = self.wallet.coins.get(den, 0)
            if count == 0:
                continue
            # We use binary representation optimization for bounded knapsack
            k = 1
            counts = []
            while count > 0:
                use = min(k, count)
                counts.append(use)
                count -= use
                k <<= 1
            for c in counts:
                cost = c  # c coins used
                value = c * den
                # Update dp from high to low to avoid reuse of this batch multiple times
                for s in range(max_sum, value - 1, -1):
                    if dp[s - value] + cost < dp[s]:
                        dp[s] = dp[s - value] + cost

        # Now we have dp[s] = minimal number of coins to pay to get sum s
        # We want minimal dp[s] + minimal coins to return change for (s - price),
        # with s >= price
        ans = INF
        for s in range(self.price, max_sum + 1):
            if dp[s] == INF:
                continue
            change = s - self.price
            change_coins = self.change_maker.calc_min_coins_change(change)
            change_count = self.change_maker.count_coins(change_coins)
            total = dp[s] + change_count
            if total < ans:
                ans = total

        return ans


class InputParser:
    def __init__(self):
        self.coin_order = [1, 5, 10, 50, 100, 500]

    def parse(self, line: str):
        tokens = list(map(int, line.strip().split()))
        if tokens[0] == 0:
            return None
        P = tokens[0]
        coin_counts = tokens[1:]
        coins = dict(zip(self.coin_order, coin_counts))
        return P, coins


class ProblemJController:
    def __init__(self):
        self.parser = InputParser()
        self.coin_set = [1, 5, 10, 50, 100, 500]

    def run(self):
        import sys
        for line in sys.stdin:
            if line.strip() == '':
                continue
            parsed = self.parser.parse(line)
            if parsed is None:
                break
            P, coins = parsed
            wallet = Wallet(coins)
            solver = PaymentSolver(P, wallet, self.coin_set)
            ans = solver.solve()
            print(ans)


if __name__ == "__main__":
    ProblemJController().run()