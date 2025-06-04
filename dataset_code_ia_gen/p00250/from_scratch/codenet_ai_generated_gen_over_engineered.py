class SconeDelivery:
    class SubsetSelector:
        def __init__(self, scones, m):
            self.scones = scones
            self.m = m

        def max_remainder_in_subrange(self):
            # Precompute prefix sums for efficient range sum queries
            prefix_sums = SconeDelivery.PrefixSum(self.scones)

            max_remainder = 0
            n = len(self.scones)
            start = 0
            end = 0

            # Sliding window to examine all contiguous subranges
            while start < n:
                # We will move 'end' to cover [start, end) subranges
                while end < n:
                    total = prefix_sums.sum_range(start, end)
                    remainder = total % self.m
                    if remainder > max_remainder:
                        max_remainder = remainder
                    # If adding more trays can only increase total, keep expanding
                    end += 1
                start += 1
                # Reset end to start for next subrange
                end = start
            return max_remainder

    class PrefixSum:
        def __init__(self, array):
            self.prefix = self._make_prefix(array)

        def _make_prefix(self, array):
            prefix = [0]
            for num in array:
                prefix.append(prefix[-1] + num)
            return prefix

        def sum_range(self, left, right):
            # sum of array[left:right+1]
            # Because prefix array length is n+1, and prefix[i] is sum up to i-1
            return self.prefix[right + 1] - self.prefix[left]

    class InputParser:
        def __init__(self):
            pass

        def parse(self):
            while True:
                line = input().strip()
                if not line:
                    continue
                n_m = line.split()
                if len(n_m) != 2:
                    continue
                n, m = map(int, n_m)
                if n == 0 and m == 0:
                    break
                scones_line = input().strip()
                while not scones_line:
                    scones_line = input().strip()
                scones = list(map(int, scones_line.split()))
                yield n, m, scones

    class OutputFormatter:
        def __init__(self):
            pass

        def print_result(self, result):
            print(result)

    def __init__(self):
        self.parser = self.InputParser()
        self.outputter = self.OutputFormatter()

    def solve_dataset(self, n, m, scones):
        selector = self.SubsetSelector(scones, m)
        max_remainder = selector.max_remainder_in_subrange()
        return max_remainder

    def run(self):
        for n, m, scones in self.parser.parse():
            result = self.solve_dataset(n, m, scones)
            self.outputter.print_result(result)


if __name__ == "__main__":
    # Using the above unnecessarily complex abstraction to solve
    solver = SconeDelivery()
    solver.run()