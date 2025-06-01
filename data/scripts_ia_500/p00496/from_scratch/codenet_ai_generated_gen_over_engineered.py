class NightMarketProblem:
    class Shop:
        def __init__(self, index: int, enjoyment: int, duration: int):
            self.index = index
            self.enjoyment = enjoyment
            self.duration = duration

    class Schedule:
        def __init__(self, total_time: int, fireworks_time: int):
            self.total_time = total_time
            self.fireworks_time = fireworks_time

    class NightMarketSolver:
        def __init__(self, shops, schedule):
            self.shops = shops
            self.schedule = schedule
            self.N = len(shops)
            self.T = schedule.total_time
            self.S = schedule.fireworks_time

        def is_valid_play_time(self, start: int, duration: int) -> bool:
            # Check if the play interval [start, start+duration) contains S inside interval
            # Invalid if S is strictly inside (start, start+duration)
            # Allowed if S == start or S == start+duration
            end = start + duration
            return not (start < self.S < end)

        def solve(self) -> int:
            # Initialize DP table
            # dp[i][t] = maximum enjoyment using shops up to i (1-indexed) with time t
            # We will use 1D DP rolling for optimization
            dp = [-1] * (self.T + 1)
            dp[0] = 0

            for i in range(self.N):
                shop = self.shops[i]
                new_dp = dp[:]
                for time in range(self.T + 1):
                    if dp[time] < 0:
                        continue
                    start = time
                    end = start + shop.duration
                    if end <= self.T and self.is_valid_play_time(start, shop.duration):
                        if new_dp[end] < dp[time] + shop.enjoyment:
                            new_dp[end] = dp[time] + shop.enjoyment
                dp = new_dp
            return max(dp)

    class InputParser:
        @staticmethod
        def parse_input():
            import sys
            input_line = sys.stdin.readline().strip()
            N, T, S = map(int, input_line.split())
            shops = []
            for i in range(1, N + 1):
                A, B = map(int, sys.stdin.readline().strip().split())
                shops.append(NightMarketProblem.Shop(i, A, B))
            schedule = NightMarketProblem.Schedule(T, S)
            return shops, schedule

    class OutputPrinter:
        @staticmethod
        def print_result(result: int):
            print(result)

def main():
    shops, schedule = NightMarketProblem.InputParser.parse_input()
    solver = NightMarketProblem.NightMarketSolver(shops, schedule)
    answer = solver.solve()
    NightMarketProblem.OutputPrinter.print_result(answer)

if __name__ == "__main__":
    main()