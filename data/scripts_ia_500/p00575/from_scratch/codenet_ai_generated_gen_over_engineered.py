class CoinEarningStrategy:
    def coins_for_logins(self, logins: int) -> int:
        raise NotImplementedError("Should implement in subclass")
    def minimal_logins_for_coins(self, target_coins: int) -> int:
        raise NotImplementedError("Should implement in subclass")

class SocialGameCoinStrategy(CoinEarningStrategy):
    def __init__(self, A: int, B: int):
        self.A = A
        self.B = B
        self.days_in_week = 7

    def coins_for_logins(self, logins: int) -> int:
        full_weeks = logins // self.days_in_week
        leftover_days = logins % self.days_in_week
        coins = full_weeks * (self.days_in_week * self.A + self.B) + leftover_days * self.A
        return coins

    def minimal_logins_for_coins(self, target_coins: int) -> int:
        # Implement a binary search over logins count
        low, high = 1, 10**9  # large upper bound to cover constraint up to 10^6 coins with B up to 1000
        while low < high:
            mid = (low + high) // 2
            current_coins = self.coins_for_logins(mid)
            if current_coins >= target_coins:
                high = mid
            else:
                low = mid + 1
        return low

class InputParser:
    @staticmethod
    def parse():
        import sys
        line = sys.stdin.readline()
        A_str, B_str, C_str = line.strip().split()
        return int(A_str), int(B_str), int(C_str)

class SocialGameSolver:
    def __init__(self):
        self.strategy = None
    def setup(self, A: int, B: int):
        self.strategy = SocialGameCoinStrategy(A, B)
    def solve(self, C: int) -> int:
        return self.strategy.minimal_logins_for_coins(C)

def main():
    A, B, C = InputParser.parse()
    solver = SocialGameSolver()
    solver.setup(A, B)
    result = solver.solve(C)
    print(result)

if __name__ == "__main__":
    main()