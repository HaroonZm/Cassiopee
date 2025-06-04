from typing import List, Tuple
import sys

class DataSet:
    def __init__(self, n: int, k: int, houses: List[int]):
        self.n = n
        self.k = k
        self.houses = houses

class InputReader:
    def __init__(self, input_source=sys.stdin):
        self.input_source = input_source
        self.lines = self.input_source.read().strip().split('\n')
        self.index = 0

    def read_int(self) -> int:
        val = int(self.lines[self.index])
        self.index += 1
        return val

    def read_ints(self) -> List[int]:
        vals = list(map(int, self.lines[self.index].split()))
        self.index += 1
        return vals

    def read_dataset(self) -> DataSet:
        n, k = self.read_ints()
        houses = self.read_ints()
        return DataSet(n, k, houses)

class EdgeDifferences:
    def __init__(self, houses: List[int]):
        self.houses = houses
        self.differences = self._compute_differences()

    def _compute_differences(self) -> List[int]:
        return [self.houses[i+1] - self.houses[i] for i in range(len(self.houses)-1)]

class WireLengthOptimizer:
    def __init__(self, dataset: DataSet):
        self.dataset = dataset
        self.diff = EdgeDifferences(dataset.houses).differences

    def minimal_total_wire_length(self) -> int:
        if self.dataset.k >= self.dataset.n:
            # Each house can have its own generator, no wire needed
            return 0
        # Sort differences descendingly to find biggest gaps
        sorted_gaps = sorted(self.diff, reverse=True)
        # Sum of gaps minus the largest k-1 gaps where generators can be placed
        return sum(self.diff) - sum(sorted_gaps[:self.dataset.k-1])

class ProblemESolver:
    def __init__(self, input_reader: InputReader):
        self.input_reader = input_reader

    def solve(self) -> List[int]:
        t = self.input_reader.read_int()
        results = []
        for _ in range(t):
            dataset = self.input_reader.read_dataset()
            optimizer = WireLengthOptimizer(dataset)
            min_length = optimizer.minimal_total_wire_length()
            results.append(min_length)
        return results

def main():
    reader = InputReader()
    solver = ProblemESolver(reader)
    results = solver.solve()
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()