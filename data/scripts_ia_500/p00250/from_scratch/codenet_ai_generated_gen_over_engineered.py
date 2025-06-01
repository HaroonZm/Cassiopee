from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator, Optional


class Dataset(ABC):
    @abstractmethod
    def solve(self) -> int:
        pass


class SconeDeliveryPlan(Dataset):
    def __init__(self, n: int, m: int, trays: List[int]) -> None:
        self.n = n
        self.m = m
        self.trays = trays
        # Compute prefix sums for efficient subrange sum computations
        self.prefix_sums = self._compute_prefix_sums(trays)

    @staticmethod
    def _compute_prefix_sums(trays: List[int]) -> List[int]:
        # prefix_sums[i] holds sum of trays[0:i], prefix_sums[0] = 0
        prefix = [0]
        for k in trays:
            prefix.append(prefix[-1] + k)
        return prefix

    def _subrange_sum(self, left: int, right: int) -> int:
        # sum of trays[left:right], where right is exclusive
        return self.prefix_sums[right] - self.prefix_sums[left]

    def solve(self) -> int:
        # The goal is to select a contiguous subrange [l, r) so that:
        # total = sum of trays in range
        # max leftover = total % m is maximized
        #
        # Because we're allowed to take any continuous segment, we want to maximize (sum_of_segment % m).
        #
        # With large n, a naive O(n^2) approach is infeasible.
        # We apply prefix sums and track mod m values to find maximum remainder.
        #
        # For subarray sums mod m:
        # Given prefix sums P,
        # sum(i,j) = P[j] - P[i], mod m = (P[j] - P[i]) % m
        #
        # We want to maximize  (P[j] - P[i]) % m for j > i.
        # This is equivalent to:
        # For each P[j], find P[i] with P[i] > P[j], minimal such to maximize remainder.
        # We'll keep prefix sums sorted and search.
        #
        # This is a classical problem that can be solved in O(n log n) via balanced BST.

        # store prefix sums mod m
        mod_prefix = [p % self.m for p in self.prefix_sums]

        import bisect

        sorted_prefixes = []
        max_remainder = 0

        for val in mod_prefix:
            # insert position for val in sorted_prefixes
            # find smallest prefix > val
            pos = bisect.bisect_right(sorted_prefixes, val)
            if pos != len(sorted_prefixes):
                candidate = (val - sorted_prefixes[pos] + self.m) % self.m
                if candidate > max_remainder:
                    max_remainder = candidate
            else:
                # no prefix bigger than val found
                # candidate remainder is val itself, i.e. (val - 0) % m
                if val > max_remainder:
                    max_remainder = val
            bisect.insort(sorted_prefixes, val)

        return max_remainder


class InputParser:
    def __init__(self) -> None:
        pass

    def parse(self, lines: Iterator[str]) -> Iterator[Dataset]:
        while True:
            try:
                line1 = next(lines)
            except StopIteration:
                break
            n_m = line1.strip()
            if n_m == "0 0":
                break
            n_str, m_str = n_m.split()
            n, m = int(n_str), int(m_str)
            tray_line = next(lines)
            trays = list(map(int, tray_line.strip().split()))
            yield SconeDeliveryPlan(n, m, trays)


class OutputFormatter:
    def __init__(self) -> None:
        pass

    def format(self, results: Iterator[int]) -> Iterator[str]:
        for res in results:
            yield str(res)


class SconeDeliverySolver:
    def __init__(
        self,
        input_parser: InputParser,
        output_formatter: OutputFormatter,
    ) -> None:
        self.input_parser = input_parser
        self.output_formatter = output_formatter

    def solve_from_lines(self, lines: Iterator[str]) -> Iterator[str]:
        datasets = self.input_parser.parse(lines)
        results = (dataset.solve() for dataset in datasets)
        formatted = self.output_formatter.format(results)
        return formatted


def main() -> None:
    import sys

    input_lines = (line for line in sys.stdin)
    solver = SconeDeliverySolver(InputParser(), OutputFormatter())
    results = solver.solve_from_lines(input_lines)
    for line in results:
        print(line)


if __name__ == "__main__":
    main()