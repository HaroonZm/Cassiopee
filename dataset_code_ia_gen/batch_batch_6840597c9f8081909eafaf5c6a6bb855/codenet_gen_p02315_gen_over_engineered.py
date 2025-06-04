class KnapsackItem:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item(value={self.value}, weight={self.weight})"


class Knapsack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []

    def add_item(self, item: KnapsackItem):
        self.items.append(item)

    def _initialize_dp_table(self):
        # DP table dimensions: (number_of_items+1) x (capacity+1)
        return [[0 for _ in range(self.capacity + 1)] for _ in range(len(self.items) + 1)]

    def solve(self) -> int:
        dp = self._initialize_dp_table()
        for i in range(1, len(self.items) + 1):
            curr_item = self.items[i - 1]
            for c in range(self.capacity + 1):
                if curr_item.weight <= c:
                    dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - curr_item.weight] + curr_item.value)
                else:
                    dp[i][c] = dp[i - 1][c]
        return dp[-1][self.capacity]


class KnapsackInputParser:
    def __init__(self, input_lines):
        self.lines = iter(input_lines)
        self.N = 0
        self.W = 0
        self.items = []

    def parse(self):
        self._parse_header()
        self._parse_items()

    def _parse_header(self):
        first_line = next(self.lines).strip()
        self.N, self.W = map(int, first_line.split())

    def _parse_items(self):
        for _ in range(self.N):
            line = next(self.lines).strip()
            v, w = map(int, line.split())
            self.items.append(KnapsackItem(value=v, weight=w))


class KnapsackSolverFacade:
    def __init__(self, input_lines):
        self.parser = KnapsackInputParser(input_lines)

    def execute(self):
        self.parser.parse()
        knapsack = Knapsack(self.parser.W)
        for item in self.parser.items:
            knapsack.add_item(item)
        return knapsack.solve()


def main():
    import sys
    solver = KnapsackSolverFacade(sys.stdin)
    result = solver.execute()
    print(result)


if __name__ == "__main__":
    main()