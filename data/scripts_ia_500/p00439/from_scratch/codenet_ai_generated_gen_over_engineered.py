from abc import ABC, abstractmethod
from typing import List, Optional, Iterator, Tuple


class IDataReader(ABC):
    @abstractmethod
    def read(self) -> Optional[Tuple[int, int, List[int]]]:
        pass


class StdInDataReader(IDataReader):
    def __init__(self):
        self._buffer: List[str] = []

    def _fetch_line(self) -> Optional[str]:
        try:
            line = input().strip()
            if line == '':
                return None
            return line
        except EOFError:
            return None

    def read(self) -> Optional[Tuple[int, int, List[int]]]:
        while True:
            line = self._fetch_line()
            if line is None:
                return None
            if line == '0 0':
                return None
            parts = line.split()
            if len(parts) != 2:
                continue  # malformed line, skip
            n, k = map(int, parts)
            if n == 0 and k == 0:
                return None
            sequence = []
            while len(sequence) < n:
                val_line = self._fetch_line()
                if val_line is None:
                    return None
                try:
                    value = int(val_line)
                    if -10000 <= value <= 10000:
                        sequence.append(value)
                except ValueError:
                    continue  # skip invalid lines
            return n, k, sequence


class IMaxSubarraySumCalculator(ABC):
    @abstractmethod
    def compute_max_subarray_sum(self, k: int, arr: List[int]) -> int:
        pass


class SlidingWindowMaxSumCalculator(IMaxSubarraySumCalculator):
    def compute_max_subarray_sum(self, k: int, arr: List[int]) -> int:
        # Defensive programming: ensure k <= len(arr)
        if k > len(arr):
            raise ValueError("k cannot be greater than array length")
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum


class ProblemSolver:
    def __init__(self, data_reader: IDataReader, calculator: IMaxSubarraySumCalculator):
        self._data_reader = data_reader
        self._calculator = calculator

    def solve_all(self) -> None:
        while True:
            dataset = self._data_reader.read()
            if dataset is None:
                break
            n, k, sequence = dataset
            max_sum = self._calculator.compute_max_subarray_sum(k, sequence)
            print(max_sum)


def main():
    data_reader = StdInDataReader()
    calculator = SlidingWindowMaxSumCalculator()
    solver = ProblemSolver(data_reader, calculator)
    solver.solve_all()


if __name__ == '__main__':
    main()