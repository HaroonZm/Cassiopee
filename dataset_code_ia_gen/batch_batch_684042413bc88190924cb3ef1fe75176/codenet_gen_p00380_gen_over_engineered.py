class SequenceState:
    def __init__(self, elements):
        self.elements = elements
        self.n = len(elements)
        self.inversion_tracker = InversionTracker(elements)

    def swap(self, i, j):
        # i and j are 1-based indices
        # Update inversions before swap
        self.inversion_tracker.update_before_swap(i - 1, j - 1)
        # Perform swap in elements
        self.elements[i - 1], self.elements[j - 1] = self.elements[j - 1], self.elements[i - 1]
        # Update inversions after swap
        self.inversion_tracker.update_after_swap(i - 1, j - 1)

    def is_sorted(self):
        return self.inversion_tracker.total_inversions == 0


class InversionTracker:
    def __init__(self, elements):
        self.elements = elements
        self.n = len(elements)
        # We track the number of adjacent inversions in the sequence
        self.adj_inversions = self._calculate_adjacent_inversions()
        self.total_inversions = self.adj_inversions

    def _calculate_adjacent_inversions(self):
        count = 0
        for i in range(self.n - 1):
            if self.elements[i] > self.elements[i + 1]:
                count += 1
        return count

    def _check_pair(self, i):
        # Check adjacent pair (i, i+1) if valid
        if 0 <= i < self.n - 1:
            return 1 if self.elements[i] > self.elements[i + 1] else 0
        return 0

    def update_before_swap(self, i, j):
        # remove inversions for all pairs that could be affected by elements i and j before swap
        # affected indices are neighbors of i and j, plus i and j themselves
        affected = set()
        for idx in (i - 1, i, j - 1, j):
            if 0 <= idx < self.n - 1:
                affected.add(idx)
        for idx in affected:
            self.total_inversions -= self._check_pair(idx)

    def update_after_swap(self, i, j):
        # after the swap, add back inversion counts for affected pairs
        affected = set()
        for idx in (i - 1, i, j - 1, j):
            if 0 <= idx < self.n - 1:
                affected.add(idx)
        for idx in affected:
            self.total_inversions += self._check_pair(idx)


class BozosortSimulation:
    def __init__(self, sequence, commands):
        self.state = SequenceState(sequence)
        self.commands = commands

    def run(self):
        if self.state.is_sorted():
            return 0
        for t, (x, y) in enumerate(self.commands, 1):
            self.state.swap(x, y)
            if self.state.is_sorted():
                return t
        return -1


class InputParser:
    def __init__(self):
        self.N = 0
        self.sequence = []
        self.Q = 0
        self.commands = []

    def parse(self):
        import sys
        reader = sys.stdin
        self.N = int(reader.readline())
        if self.N > 0:
            self.sequence = list(map(int, reader.readline().split()))
        else:
            self.sequence = []
        self.Q = int(reader.readline())
        self.commands = [tuple(map(int, reader.readline().split())) for _ in range(self.Q)]


def main():
    parser = InputParser()
    parser.parse()
    simulation = BozosortSimulation(parser.sequence, parser.commands)
    result = simulation.run()
    print(result)


if __name__ == "__main__":
    main()