class Ball:
    def __init__(self, color: int, value: int):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"Ball(color={self.color}, value={self.value})"


class ColorLimitManager:
    def __init__(self, limits):
        # limits indexed by color start at 1, so we pad 0-th index
        self.limits = [0] + limits
        self.counts = [0] * len(self.limits)

    def can_pick(self, color):
        return self.counts[color] < self.limits[color]

    def pick(self, color):
        if not self.can_pick(color):
            raise ValueError(f"Cannot pick more balls of color {color}")
        self.counts[color] += 1


class BallCollectorStrategy:
    def __init__(self, balls, color_limit_manager, max_total):
        self.balls = balls
        self.clm = color_limit_manager
        self.max_total = max_total

    def select_balls(self):
        # Sort balls descending by value to pick highest value balls first
        sorted_balls = sorted(self.balls, key=lambda b: b.value, reverse=True)

        selected_value_sum = 0
        selected_count = 0

        for ball in sorted_balls:
            if selected_count >= self.max_total:
                break
            if self.clm.can_pick(ball.color):
                self.clm.pick(ball.color)
                selected_value_sum += ball.value
                selected_count += 1

        return selected_value_sum


class ProblemCSolver:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.C = 0
        self.color_limits = []
        self.balls = []

    def read_input(self):
        self.N, self.M, self.C = map(int, input().split())
        self.color_limits = list(map(int, input().split()))
        self.balls = []
        for _ in range(self.N):
            c_i, w_i = map(int, input().split())
            self.balls.append(Ball(c_i, w_i))

    def solve(self):
        clm = ColorLimitManager(self.color_limits)
        strategy = BallCollectorStrategy(self.balls, clm, self.M)
        answer = strategy.select_balls()
        print(answer)


def main():
    solver = ProblemCSolver()
    solver.read_input()
    solver.solve()


if __name__ == "__main__":
    main()