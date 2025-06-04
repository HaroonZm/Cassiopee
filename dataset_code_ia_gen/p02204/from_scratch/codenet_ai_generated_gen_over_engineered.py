class AbstractPlan:
    def __init__(self, days, tshirts):
        self.days = days
        self.tshirts = tshirts

    def minimal_changes(self):
        raise NotImplementedError("Subclasses should implement this method")


class ContestTShirtPlan(AbstractPlan):
    def __init__(self, tshirt_count, day_count, plan):
        super().__init__(day_count, tshirt_count)
        self.plan = plan

    def minimal_changes(self):
        # We minimize changes so that no two consecutive days have the same T-shirt.
        changes = 0
        for i in range(1, self.days):
            if self.plan[i] == self.plan[i - 1]:
                changes += 1
                # Change the current day's T-shirt to any different from both neighbors if possible
                # But since problem guarantees always possible and the minimal changes count is asked,
                # we just count changes here.
                # The concrete replacement is irrelevant for counting minimal changes.
        return changes


class InputReader:
    def __init__(self):
        self.M = 0
        self.N = 0
        self.A = []

    def read(self):
        self.M, self.N = map(int, input().split())
        self.A = list(map(int, input().split()))


class OutputWriter:
    @staticmethod
    def write(result):
        print(result)


class ContestTShirtSolver:
    def __init__(self):
        self.reader = InputReader()
        self.writer = OutputWriter()
        self.plan = None

    def solve(self):
        self.reader.read()
        self.plan = ContestTShirtPlan(self.reader.M, self.reader.N, self.reader.A)
        result = self.plan.minimal_changes()
        self.writer.write(result)


if __name__ == "__main__":
    solver = ContestTShirtSolver()
    solver.solve()