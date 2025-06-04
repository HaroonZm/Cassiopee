class Sequence:
    def __init__(self, elements):
        self.elements = list(elements)
        self.length = len(elements)

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            return False
        return self.elements == other.elements

    def __repr__(self):
        return f"Sequence({self.elements})"

class FrequencyTransformer:
    def transform(self, sequence):
        freq_map = self._count_frequencies(sequence.elements)
        transformed_elements = [freq_map[val] for val in sequence.elements]
        return Sequence(transformed_elements)

    def _count_frequencies(self, elements):
        freq = {}
        for e in elements:
            freq[e] = freq.get(e, 0) + 1
        return freq

class FixedPointFinder:
    def __init__(self, transformer):
        self.transformer = transformer

    def find_fixed_point(self, initial_sequence):
        current_sequence = initial_sequence
        count = 0
        while True:
            next_sequence = self.transformer.transform(current_sequence)
            count += 1
            if next_sequence == current_sequence:
                return count - 1, current_sequence
            current_sequence = next_sequence

class InputOutputHandler:
    def __init__(self):
        self.transformer = FrequencyTransformer()
        self.fixed_point_finder = FixedPointFinder(self.transformer)

    def process(self):
        while True:
            n_line = self._read_nonempty_line()
            if n_line is None:
                break
            n = int(n_line)
            if n == 0:
                break
            sequence_line = self._read_nonempty_line()
            elements = list(map(int, sequence_line.strip().split()))
            seq = Sequence(elements)
            count, fixed_point_seq = self.fixed_point_finder.find_fixed_point(seq)
            print(count)
            print(" ".join(map(str, fixed_point_seq.elements)))

    def _read_nonempty_line(self):
        while True:
            try:
                line = input()
            except EOFError:
                return None
            if line.strip() != '':
                return line
            # else ignore empty lines

def main():
    ioh = InputOutputHandler()
    ioh.process()

if __name__ == "__main__":
    main()