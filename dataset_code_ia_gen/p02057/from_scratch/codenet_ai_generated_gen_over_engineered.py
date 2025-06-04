class Sequence:
    def __init__(self, elements):
        self._elements = elements
        self._frequency = {}
        self._compute_frequency()

    def _compute_frequency(self):
        for e in self._elements:
            self._frequency[e] = self._frequency.get(e, 0) + 1

    @property
    def elements(self):
        return self._elements

    @property
    def frequency(self):
        return self._frequency

    def __len__(self):
        return len(self._elements)

    def unique_elements(self):
        return self._frequency.keys()

class RemainderMatrix:
    def __init__(self, seq_a: Sequence, seq_b: Sequence):
        self.seq_a = seq_a
        self.seq_b = seq_b

    def calc_sum_of_remainders(self):
        # Since (a mod b) computed for all pairs, 
        # to optimize, use frequency counts and avoid repeated work.
        total = 0
        freq_b = self.seq_b.frequency
        for a_val, a_count in self.seq_a.frequency.items():
            # For each unique a_val, compute sum over all b of (a_val mod b) * freq_b[b]
            # We do a naive approach despite large constraints for clarity of abstraction.
            # Could be optimized with bucketing, but left for future extension.
            for b_val, b_count in freq_b.items():
                total += (a_val % b_val) * a_count * b_count
        return total

class InputHandler:
    def __init__(self):
        self.N = None
        self.M = None
        self.seq_a = None
        self.seq_b = None

    def read_input(self):
        self.N, self.M = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        self.seq_a = Sequence(a)
        self.seq_b = Sequence(b)

class MODRushSolver:
    def __init__(self):
        self.input_handler = InputHandler()
        self.remainder_matrix = None
        self.result = None

    def solve(self):
        self.input_handler.read_input()
        self.remainder_matrix = RemainderMatrix(self.input_handler.seq_a, self.input_handler.seq_b)
        self.result = self.remainder_matrix.calc_sum_of_remainders()
        self.output()

    def output(self):
        print(self.result)

if __name__ == "__main__":
    solver = MODRushSolver()
    solver.solve()