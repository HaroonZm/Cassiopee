class PrizeCollection:
    def __init__(self, quantities):
        self.quantities = quantities
        self.types = len(quantities)

    def minimum_trials_for_double(self):
        max_q = max(self.quantities) if self.quantities else 0
        if max_q < 2:
            return None  # Impossible to have two identical prizes

        # Calculate sum of quantities
        total = sum(self.quantities)

        # Filter out prizes with at least 2 copies for considerations
        candidates = [q for q in self.quantities if q >= 2]

        # If only one prize type, 2 trials suffice if quantity >= 2
        if self.types == 1 and max_q >= 2:
            return 2

        # Use the pigeonhole principle extended:
        # The worst case to get two identical is:
        # 1 (for each prize type) + 1 extra try
        # However, must consider stock limits.

        # Find the minimal number M so that no matter what,
        # among M draws, there is a prize type with at least 2 copies drawn.

        # The maximum # of different items one can get with single instances is the count of nonzero quantities
        num_nonzero = sum(1 for q in self.quantities if q > 0)

        # But some quantities may limit this count if less than one or two, but we accounted for zero quantities in num_nonzero

        # Try M from 2 upwards
        # The minimal M is at least 2
        # Upper bound: sum(quantities)+1

        left = 2
        right = total + 1

        def can_avoid_double(m):
            # Check if it is possible to pick m prizes without any two identical
            # I.e., pick at most 1 from each prize type
            # So if m <= number of available prize types with quantity >=1, it's possible
            # but must also verify quantity limits.

            # How many single prizes can we pick at most?
            singles = sum(1 for q in self.quantities if q > 0)
            if m <= singles:
                return True
            return False

        # Binary search for minimal M s.t. can_avoid_double(M) == False
        res = None
        while left <= right:
            mid = (left + right) // 2
            if not can_avoid_double(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

class InputProcessor:
    def __init__(self):
        self.datasets = []

    def read_datasets(self, input_lines):
        from collections import deque
        lines = deque(input_lines)
        while lines:
            first_line = lines.popleft().strip()
            if first_line == '0':
                break
            n = int(first_line)
            if not lines:
                break
            quantities_line = lines.popleft().strip()
            quantities = list(map(int, quantities_line.split()))
            self.datasets.append((n, quantities))

class OutputGenerator:
    def __init__(self, datasets):
        self.datasets = datasets

    def compute_results(self):
        results = []
        for n, quantities in self.datasets:
            pc = PrizeCollection(quantities)
            res = pc.minimum_trials_for_double()
            if res is None:
                results.append("NA")
            else:
                results.append(str(res))
        return results

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    processor = InputProcessor()
    processor.read_datasets(input_lines)
    generator = OutputGenerator(processor.datasets)
    results = generator.compute_results()
    for line in results:
        print(line)

if __name__ == "__main__":
    main()