class CoinChangeException(Exception):
    pass

class CoinDenomination:
    def __init__(self, value: int):
        if value <= 0:
            raise CoinChangeException("Coin denomination must be positive")
        self.value = value

    def __repr__(self):
        return f"CoinDenomination({self.value})"

class CoinChangeInput:
    def __init__(self, amount: int, denominations: list):
        if amount <= 0:
            raise CoinChangeException("Amount must be positive")
        if not denominations:
            raise CoinChangeException("Denominations list cannot be empty")
        if 1 not in denominations:
            raise CoinChangeException("Denominations must include coin 1 for solvability")
        self.amount = amount
        self.denominations = [CoinDenomination(d) for d in denominations]

    def __repr__(self):
        return f"CoinChangeInput(amount={self.amount}, denominations={self.denominations})"

class CoinChangeDPState:
    def __init__(self, amount: int):
        self.amount = amount
        self.min_coins = float('inf')
        self.last_coin = None

    def update(self, coins_used: int, coin_value: int):
        if coins_used < self.min_coins:
            self.min_coins = coins_used
            self.last_coin = coin_value

    def __repr__(self):
        return f"CoinChangeDPState(amount={self.amount}, min_coins={self.min_coins}, last_coin={self.last_coin})"

class CoinChangeSolver:
    def __init__(self, coin_change_input: CoinChangeInput):
        self.input = coin_change_input
        self.dp = [CoinChangeDPState(i) for i in range(self.input.amount + 1)]
        self.dp[0].min_coins = 0  # Base case: 0 coins to make 0 amount

    def solve(self):
        for amt in range(1, self.input.amount + 1):
            for coin in self.input.denominations:
                if coin.value <= amt:
                    prev_state = self.dp[amt - coin.value]
                    if prev_state.min_coins != float('inf'):
                        self.dp[amt].update(prev_state.min_coins + 1, coin.value)
        if self.dp[self.input.amount].min_coins == float('inf'):
            raise CoinChangeException("No solution found.")
        return self.dp[self.input.amount].min_coins

class CoinChangeApp:
    def __init__(self):
        self.input = None
        self.solver = None

    def parse_input(self, line1: str, line2: str):
        try:
            n, m = map(int, line1.strip().split())
            denominations = list(map(int, line2.strip().split()))
            if len(denominations) != m:
                raise CoinChangeException("Number of denominations does not match m")
            self.input = CoinChangeInput(n, denominations)
        except ValueError:
            raise CoinChangeException("Invalid input format")

    def run(self):
        self.solver = CoinChangeSolver(self.input)
        min_coins = self.solver.solve()
        print(min_coins)

def main():
    import sys
    app = CoinChangeApp()
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    app.parse_input(line1, line2)
    app.run()

if __name__ == "__main__":
    main()