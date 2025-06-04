class NightMarketProblem:
    class NightStall:
        def __init__(self, index: int, enjoyment: int, duration: int):
            self.index = index
            self.enjoyment = enjoyment
            self.duration = duration

    class Schedule:
        def __init__(self, stalls, S, T):
            self.stalls = stalls
            self.S = S
            self.T = T
            self.dp = [-1] * (T + 1)
            self.dp[0] = 0

        def can_schedule(self, start_time: int, duration: int) -> bool:
            # Conditions for firework viewing:
            # The activity interval must not include S inside the interval,
            # but S can be equal to start or end time.
            end_time = start_time + duration
            if end_time > self.T:
                return False
            if start_time < self.S < end_time:
                return False
            return True

        def maximize_enjoyment(self) -> int:
            # Using DP to choose stalls in increasing order of index
            for stall in self.stalls:
                new_dp = self.dp[:]
                b = stall.duration
                a = stall.enjoyment
                for t in range(self.T - b + 1):
                    if self.dp[t] < 0:
                        continue
                    if not self.can_schedule(t, b):
                        continue
                    candidate = self.dp[t] + a
                    end_t = t + b
                    if candidate > new_dp[end_t]:
                        new_dp[end_t] = candidate
                self.dp = new_dp
            return max(self.dp)

    class InputHandler:
        def __init__(self):
            self.N = 0
            self.T = 0
            self.S = 0
            self.stalls = []

        def read_input(self):
            import sys
            data = sys.stdin.read().strip().split()
            self.N, self.T, self.S = map(int, data[0:3])
            self.stalls = []
            idx = 3
            for i in range(1, self.N + 1):
                A = int(data[idx]); B = int(data[idx + 1])
                idx += 2
                self.stalls.append(NightMarketProblem.NightStall(i, A, B))

    class Controller:
        def __init__(self):
            self.input_handler = NightMarketProblem.InputHandler()

        def run(self):
            self.input_handler.read_input()
            schedule = NightMarketProblem.Schedule(
                self.input_handler.stalls,
                self.input_handler.S,
                self.input_handler.T
            )
            result = schedule.maximize_enjoyment()
            print(result)

if __name__ == "__main__":
    NightMarketProblem.Controller().run()