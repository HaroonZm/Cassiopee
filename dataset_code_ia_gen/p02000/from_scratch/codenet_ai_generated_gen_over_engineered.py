class Sequence:
    def __init__(self, elements):
        self._elements = elements

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, index):
        return self._elements[index]

    def swap(self, i, j):
        self._elements[i], self._elements[j] = self._elements[j], self._elements[i]

    def to_list(self):
        return self._elements.copy()


class OperationCounter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def count(self):
        return self._count


class ConvexConcaveChecker:
    def __init__(self, sequence: Sequence):
        self._seq = sequence

    def is_convex_concave(self):
        n = len(self._seq)
        for i in range(1, n-1):
            left = self._seq[i-1]
            mid = self._seq[i]
            right = self._seq[i+1]
            if not ((left > mid and right > mid) or (left < mid and right < mid)):
                return False
        return True


class SwapOperation:
    def __init__(self, sequence: Sequence, op_counter: OperationCounter):
        self._seq = sequence
        self._op_counter = op_counter

    def apply_swap(self, i):
        self._seq.swap(i, i+1)
        self._op_counter.increment()


class ConvexConcaveTransformer:
    def __init__(self, sequence: Sequence):
        self.sequence = sequence
        self.n = len(sequence)
        self.op_counter = OperationCounter()
        self.swap_operator = SwapOperation(self.sequence, self.op_counter)
        self.checker = ConvexConcaveChecker(self.sequence)

    def minimal_swaps_to_convex_concave(self):
        # According to the problem, the minimal swaps to achieve a convex-concave sequence
        # can be found by trying two patterns: first element is high or first element is low in zigzag.
        # We generate two patterns of correct inequalities and count swaps needed.

        # The strategy:
        # positions with even index (0-based) should be peak or valley depending on pattern:
        # pattern1: even indexes peak (A[i] > A[i-1] and A[i] > A[i+1])
        # pattern2: even indexes valley (A[i] < A[i-1] and A[i] < A[i+1])
        #
        # We count how many positions violate the condition,
        # minimal swaps would be half the number of violations, since swapping can fix two elements.
        #
        # Because all elements are distinct, we do not have to worry about equal cases.

        def count_swaps_for_pattern(peaks_on_even_index):
            violations = 0
            for i in range(1, self.n-1):
                prev = self.sequence[i-1]
                curr = self.sequence[i]
                nxt = self.sequence[i+1]
                is_peak = curr > prev and curr > nxt
                is_valley = curr < prev and curr < nxt
                # Determine if position i should be peak or valley
                should_be_peak = (i % 2 == 0) if peaks_on_even_index else (i % 2 == 1)
                if should_be_peak:
                    if not is_peak:
                        violations += 1
                else:
                    if not is_valley:
                        violations += 1
            # Each swap fixes one adjacency, minimally one violation.
            # Since each swap swaps adjacent elements, and violations are per element,
            # a rough lower bound of swaps is ceil(violations/2)
            return (violations + 1) // 2

        swaps_pattern1 = count_swaps_for_pattern(True)
        swaps_pattern2 = count_swaps_for_pattern(False)
        return min(swaps_pattern1, swaps_pattern2)


def main():
    import sys

    class InputHandler:
        def __init__(self):
            self.n = None
            self.array = None

        def read_input(self):
            self.n = int(sys.stdin.readline().strip())
            self.array = list(map(int, sys.stdin.readline().strip().split()))

    input_handler = InputHandler()
    input_handler.read_input()

    seq = Sequence(input_handler.array)
    transformer = ConvexConcaveTransformer(seq)
    result = transformer.minimal_swaps_to_convex_concave()
    print(result)


if __name__ == "__main__":
    main()