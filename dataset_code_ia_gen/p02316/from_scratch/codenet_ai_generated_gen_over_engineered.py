class Item:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item(value={self.value}, weight={self.weight})"

class KnapsackState:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dp = [0] * (capacity + 1)

    def value_at(self, weight: int) -> int:
        if 0 <= weight <= self.capacity:
            return self.dp[weight]
        else:
            raise IndexError("Weight out of bounds")

    def update(self, items: list):
        for item in items:
            for w in range(item.weight, self.capacity + 1):
                candidate = self.dp[w - item.weight] + item.value
                if candidate > self.dp[w]:
                    self.dp[w] = candidate

class KnapsackSolver:
    def __init__(self, items: list, capacity: int):
        self.items = items
        self.capacity = capacity
        self.state = KnapsackState(capacity)

    def solve_unbounded(self) -> int:
        self.state.update(self.items)
        return max(self.state.dp)

class InputParser:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.lines = iter(raw_input.strip().split('\n'))

    def parse(self):
        first_line = next(self.lines)
        N, W = map(int, first_line.split())
        items = []
        for _ in range(N):
            v, w = map(int, next(self.lines).split())
            items.append(Item(v, w))
        return items, W

class KnapsackApp:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def run(self):
        parser = InputParser(self.input_str)
        items, capacity = parser.parse()
        solver = KnapsackSolver(items, capacity)
        result = solver.solve_unbounded()
        print(result)

import sys

if __name__ == "__main__":
    input_data = sys.stdin.read()
    app = KnapsackApp(input_data)
    app.run()