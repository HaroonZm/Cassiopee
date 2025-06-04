class MultipleCounter:
    def __init__(self, total_count: int, count_2: int, count_3: int, count_6: int):
        self._total_count = total_count
        self._count_2 = count_2
        self._count_3 = count_3
        self._count_6 = count_6

    @property
    def total_count(self) -> int:
        return self._total_count

    @property
    def count_2(self) -> int:
        return self._count_2

    @property
    def count_3(self) -> int:
        return self._count_3

    @property
    def count_6(self) -> int:
        return self._count_6

    def count_neither_multiple_of_2_nor_3(self) -> int:
        # Utilizing inclusion-exclusion principle:
        # numbers that are multiples of 2 or 3 = A + B - C
        multiples_of_2_or_3 = self.count_2 + self.count_3 - self.count_6
        return self.total_count - multiples_of_2_or_3


class InputParser:
    @staticmethod
    def parse_input(input_line: str) -> MultipleCounter:
        parts = input_line.strip().split()
        if len(parts) != 4:
            raise ValueError("Input must consist of exactly 4 integers separated by spaces.")
        N, A, B, C = map(int, parts)
        return MultipleCounter(N, A, B, C)


class Solution:
    def __init__(self):
        self._counter = None

    def load_input(self):
        import sys
        input_line = sys.stdin.readline()
        self._counter = InputParser.parse_input(input_line)

    def solve(self) -> int:
        if self._counter is None:
            raise RuntimeError("Input not loaded")
        return self._counter.count_neither_multiple_of_2_nor_3()

    def output(self, result: int):
        print(result)


def main():
    solution = Solution()
    solution.load_input()
    result = solution.solve()
    solution.output(result)


if __name__ == "__main__":
    main()