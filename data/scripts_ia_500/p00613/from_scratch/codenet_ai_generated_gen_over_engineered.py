from abc import ABC, abstractmethod
from typing import List, Iterator

class InputSource(ABC):
    @abstractmethod
    def read_int(self) -> int:
        pass

    @abstractmethod
    def read_ints(self, n: int) -> List[int]:
        pass

class StdInputSource(InputSource):
    def __init__(self):
        self._buffer = []
        self._index = 0

    def _fetch_next_line(self):
        line = ''
        while line.strip() == '':
            line = input()
        self._buffer = list(map(int, line.strip().split()))
        self._index = 0

    def read_int(self) -> int:
        if self._index >= len(self._buffer):
            self._fetch_next_line()
        val = self._buffer[self._index]
        self._index += 1
        return val

    def read_ints(self, n: int) -> List[int]:
        result = []
        while len(result) < n:
            if self._index >= len(self._buffer):
                self._fetch_next_line()
            take = min(n - len(result), len(self._buffer) - self._index)
            result.extend(self._buffer[self._index:self._index + take])
            self._index += take
        return result

class OutputSink(ABC):
    @abstractmethod
    def write_line(self, line: str) -> None:
        pass

class StdOutputSink(OutputSink):
    def write_line(self, line: str) -> None:
        print(line)

class CakeSalesSolver:
    def __init__(self, input_source: InputSource, output_sink: OutputSink):
        self._input = input_source
        self._output = output_sink

    def _compute_total_sales(self, k: int, pair_sums: List[int]) -> int:
        # sum_all_pairs = (sum_cakes * (sum_cakes - 1)) / 2 is not correct here because the pair sums are sums of pairs,
        # we know sum of all pair sums = (K-1)*sum_cakes
        # Because each cake count contributes exactly (K-1) times to pair sums.
        #
        # sum_of_pair_sums = (K - 1) * total_sales
        # so total_sales = sum_of_pair_sums / (K - 1)
        return sum(pair_sums) // (k - 1)

    def solve(self) -> None:
        while True:
            k = self._input.read_int()
            if k == 0:
                break
            pair_count = k * (k - 1) // 2
            pair_sums = self._input.read_ints(pair_count)
            total = self._compute_total_sales(k, pair_sums)
            self._output.write_line(str(total))

def main():
    input_source = StdInputSource()
    output_sink = StdOutputSink()
    solver = CakeSalesSolver(input_source, output_sink)
    solver.solve()

if __name__ == "__main__":
    main()