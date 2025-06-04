class AbstractValueSequence:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, idx):
        return self._values[idx]

    def sorted_descending(self):
        return SortedDescendingSequence(self._values)

class SortedDescendingSequence(AbstractValueSequence):
    def __init__(self, values):
        super().__init__(sorted(values, reverse=True))

class HappinessCalculator:
    def __init__(self, gag_sequence: AbstractValueSequence):
        self.gag_sequence = gag_sequence

    def compute_max_happiness(self):
        # We want to maximize sum of V_i - j where j is the order (1-based).
        # Optimal order: descending V_i to maximize sum(V_i) - sum(j).
        sorted_seq = self.gag_sequence.sorted_descending()
        total_happiness = 0
        for idx, value in enumerate(sorted_seq, 1):
            total_happiness += value - idx
        return total_happiness

class InputReader:
    def __init__(self):
        import sys
        self.lines = sys.stdin.read().splitlines()
        self.index = 0

    def next_int(self):
        val = int(self.lines[self.index])
        self.index += 1
        return val

    def next_int_list(self):
        vals = list(map(int, self.lines[self.index].split()))
        self.index += 1
        return vals

class OutputWriter:
    def __init__(self):
        import sys
        self.stdout = sys.stdout

    def writeln(self, s):
        self.stdout.write(str(s) + "\n")

def main():
    reader = InputReader()
    n = reader.next_int()
    values = reader.next_int_list()

    gag_sequence = AbstractValueSequence(values)
    calculator = HappinessCalculator(gag_sequence)
    answer = calculator.compute_max_happiness()

    writer = OutputWriter()
    writer.writeln(answer)

if __name__ == "__main__":
    main()