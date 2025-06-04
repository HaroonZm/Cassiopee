class CoinDenomination:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class CoinSet:
    # immutable, sorted descending by value
    _denominations = [
        CoinDenomination(1000, "1000-yen bill"),
        CoinDenomination(500, "500-yen coin"),
        CoinDenomination(100, "100-yen coin"),
        CoinDenomination(50, "50-yen coin"),
        CoinDenomination(10, "10-yen coin"),
        CoinDenomination(5, "5-yen coin"),
        CoinDenomination(1, "1-yen coin")
    ]

    @classmethod
    def get_minimum_coins_change(cls, change):
        # returns dict {denomination_value: count} for minimal number of coins to make given change
        remain = change
        result = {}
        for denom in cls._denominations:
            count = remain // denom.value
            if count > 0:
                result[denom.value] = count
                remain -= count * denom.value
        return result

    @classmethod
    def get_coin_index(cls, value):
        for i, denom in enumerate(cls._denominations):
            if denom.value == value:
                return i
        return -1

class PaymentStrategy:
    def __init__(self, price, current_coins):
        self.price = price
        self.current_coins = tuple(current_coins)  # tuple with counts of coins in order in CoinSet._denominations excluding 1000-yen bills
        self.bill_value = 1000

    def generate_payment_options(self):
        # We have unlimited 1000-yen bills, but finite coins in hand.
        # We try to find all payment methods that after payment produce minimal change (and thus get the 500-yen coin in change if possible).
        # To obtain a 500-yen coin, the change must contain it.
        # Since change is calculated as (money given - price).
        #
        # Because handing over too many coins is useless, we limit the payment over price to at most 1000 (one bill).
        #
        # The handover can include:
        # - an arbitrary number k of 1000-yen bills (k=0 or 1; 2 unlikely beneficial since 2000 - price > 1500; too costly)
        # - some coins we have in hand
        #
        # We enumerate all feasible coin combinations to hand over (those not exceeding coins in hand), plus zero or one 1000-yen bill.
        #
        # For performance, we limit coins combinations to those coins sums ≤ price + 1000 (reasonable threshold).
        #
        # We then compute change and minimal coins for change, and count received 500-yen coins from change.

        from itertools import product

        # Only 6 coin types: excluding 1000-yen bills (index 0), coins are indices 1..6 with counts in self.current_coins
        coin_counts = self.current_coins  # length 7 but index 0 is 1000-yen bill excluded here
        # Actually self.current_coins length is 7 but we exclude 1000 bills, initial state 0 for all coins (index 1..6)
        # We build using indices 1..6
        coin_types = CoinSet._denominations[1:]  # skip 1000-yen bill
        # For performance, let's consider max coin usage per denom is min(current count, some reasonable limit, e.g. 20)
        coin_limits = [min(count, 20) for count in coin_counts]  # coin_counts corresponds to indices 0..6; but we passed coins ex-1000; here let's be consistent

        # Actually to align with our representation:
        # current_coins length is 7 with indices 0..6 as 1000,500,100,50,10,5,1?
        # No. We defined _denominations with 1000 first, then 500, then others.
        # The problem states he starts with no coins, only 1000-yen bills unlimited.
        # So current_coins counts for coins excluding 1000-yen bills: 6 coins (500,100,50,10,5,1)
        # Then coin_counts length is 6.
        # So in code: coin_counts = tuple of counts for 500,100,50,10,5,1
        # Our payment state has no count for 1000-yen bills.
        # So coin_types are denominations from 500 down to 1.
        # Hence indices 0..5 for these coins.
        # There is no unlimited 1000-yen bills count here, handled differently.
        #
        # Update: We'll have current_coins tuple of length 6 for coins (excluding 1000-yen).
        # During payment, we can add 0 or 1 1000-yen bills.
        # We'll need to store the coin counts as 6 length tuple.
        #
        # We'll enumerate all combinations of coin usage within limits coin_limits.
        # To limit search space, use a heuristic: total coin sum ≤ price + 1000

        # Modified approach:
        # Iterate coin usage from 0..limit for each, generate their total coin value sum.
        # For each, k in (0,1) number of 1000-yen bills handed over.
        # Hand over money = coin sum + k*1000
        # Only if hand over money >= price, compute change.
        # Check change includes 500-yen coin(s).
        # Yield info: total payment money, change, 500-yen coins count in change, coins used

        # To ease complexity, use recursive bounded generation with pruning.

        results = []

        def dfs(i, used_coins, total_coin_value):
            if i == len(coin_counts):
                # For k in {0,1}
                for k1000 in (0,1):
                    payment = total_coin_value + 1000 * k1000
                    if payment < self.price: # not enough money
                        continue
                    change = payment - self.price
                    if change < 0:
                        continue
                    # Get minimal coins for change
                    change_coins = CoinSet.get_minimum_coins_change(change)
                    # Number of 500-yen coins in change
                    count_500 = change_coins.get(500, 0)
                    # We want to look only if we get at least 0 coins (any #)
                    # This will generate all payment options
                    results.append((count_500, payment, tuple(used_coins), k1000))
                return
            limit = coin_counts[i]
            for c in range(limit + 1):
                used_coins.append(c)
                dfs(i+1, used_coins, total_coin_value + c * CoinSet._denominations[i+1].value)
                used_coins.pop()

        dfs(0, [], 0)
        return results

class StateManager:
    # To store states: (shop_index, coins_tuple) => (max_500coins, min_expense)
    # coins_tuple: current coin counts for (500,100,50,10,5,1)
    def __init__(self):
        self.states = {}

    def get(self, shop_index, coin_tuple):
        return self.states.get( (shop_index, coin_tuple), None)

    def set(self, shop_index, coin_tuple, c500, expense):
        key = (shop_index, coin_tuple)
        old = self.states.get(key)
        if old is None:
            self.states[key] = (c500, expense)
            return True
        else:
            old_c, old_e = old
            if c500 > old_c or (c500 == old_c and expense < old_e):
                self.states[key] = (c500, expense)
                return True
        return False

class YenSavingSolver:
    def __init__(self, prices):
        self.prices = prices
        self.n = len(prices)
        self.coin_types = CoinSet._denominations[1:]  # 500,100,50,10,5,1
        self.initial_coins = (0,0,0,0,0,0)  # no coins at start
        self.INF = 1 << 60

    def solve(self):
        # dynamic programming with memoization:
        # dp states store (max 500-yen coins obtained, min expense) for each (index, coins held)
        # coins held = tuple of counts of 6 coins (no 1000-yen bill, infinite)
        # at each shop, we can choose to buy or skip
        # buying changes coin counts based on payment and change
        #
        # We start state: 0th shop, no coins, 0 coins collected, 0 expense
        #
        # process each shop i from 0 to n-1:
        # For each state:
        #   option skip: same coin counts, c500, expense
        #   option buy: try all payment methods:
        #       subtract coins used, add coins from change,
        #       increment c500 coins by number of 500-yen coins received from change

        from collections import defaultdict, deque

        current_states = {}
        current_states[self.initial_coins] = (0,0)  # coin counts -> (c500coins collected, expense spent)
        for price in self.prices:
            next_states = {}
            for coins_held, (c500, expense) in current_states.items():
                # Option 1: skip this shop
                self.update_state(next_states, coins_held, c500, expense)
                # Option 2: buy this shop's souvenir

                strategy = PaymentStrategy(price, coins_held)
                payments = strategy.generate_payment_options()
                for (received_500coins, payment_money, used_coins, used_1000_bills) in payments:
                    # check if we have enough coins to pay used_coins
                    # used_coins corresponds to coins handed over of six coin types in order: [500,100,50,10,5,1]
                    # but we started with counts coins_held of same order, must check >= used_coins?

                    if any(used_coins[i] > coins_held[i] for i in range(6)):
                        continue  # can't pay these coins

                    # build new coins count after payment:
                    # new_coins = coins_held - used_coins + change_coins except 500-yen coins increase count is noted separately (500-yen coins are in coin set, but also counted in c500)
                    # To calculate change_coins, do change = payment_money - price again and get minimal coins except 500-yen coins count

                    change = payment_money - price
                    change_min_coins = CoinSet.get_minimum_coins_change(change)

                    # coins after transaction:

                    new_coins = [0]*6
                    for i, denom in enumerate(self.coin_types):
                        coin_val = denom.value
                        after = coins_held[i] - used_coins[i] + change_min_coins.get(coin_val, 0)
                        new_coins[i] = after

                    new_coins = tuple(new_coins)
                    new_c500 = c500 + received_500coins
                    new_expense = expense + payment_money
                    self.update_state(next_states, new_coins, new_c500, new_expense)
            current_states = next_states

        # answer: find maximum c500 coins and minimum expense
        max_c500 = -1
        min_expense = self.INF
        for (c500coins, exp) in current_states.values():
            if c500coins > max_c500 or (c500coins == max_c500 and exp < min_expense):
                max_c500 = c500coins
                min_expense = exp
        return max_c500, min_expense

    def update_state(self, state_dict, coins, c500, expense):
        if coins not in state_dict:
            state_dict[coins] = (c500, expense)
        else:
            old_c500, old_expense = state_dict[coins]
            if c500 > old_c500 or (c500 == old_c500 and expense < old_expense):
                state_dict[coins] = (c500, expense)

def main():
    import sys
    input = sys.stdin.readline
    results = []
    while True:
        n_line = input()
        if not n_line:
            break
        n = n_line.strip()
        if n == '0':
            break
        n = int(n)
        prices = []
        for _ in range(n):
            p = int(input())
            prices.append(p)
        solver = YenSavingSolver(prices)
        c, s = solver.solve()
        print(c, s)

if __name__ == "__main__":
    main()