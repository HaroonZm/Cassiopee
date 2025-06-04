class SwapCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count


class Sequence:
    def __init__(self, elements):
        self._elements = elements

    def length(self):
        return len(self._elements)

    def get(self, index):
        return self._elements[index]

    def set(self, index, value):
        self._elements[index] = value

    def swap(self, i, j):
        self._elements[i], self._elements[j] = self._elements[j], self._elements[i]

    def __str__(self):
        return ' '.join(map(str, self._elements))


class SelectionSortAlgorithm:
    def __init__(self, sequence):
        self.sequence = sequence
        self.swap_counter = SwapCounter()

    def find_min_index(self, start):
        min_index = start
        for j in range(start, self.sequence.length()):
            if self.sequence.get(j) < self.sequence.get(min_index):
                min_index = j
        return min_index

    def sort(self):
        n = self.sequence.length()
        for i in range(n):
            min_index = self.find_min_index(i)
            if i != min_index:
                self.sequence.swap(i, min_index)
                self.swap_counter.increment()
        return self.sequence, self.swap_counter.value()


class SelectionSortApp:
    def __init__(self):
        self.sequence = None
        self.sorted_sequence = None
        self.swap_count = 0

    def run(self):
        self._read_input()
        sort_algo = SelectionSortAlgorithm(self.sequence)
        self.sorted_sequence, self.swap_count = sort_algo.sort()
        self._print_output()

    def _read_input(self):
        n = int(input())
        elements = list(map(int, input().split()))
        if n != len(elements):
            raise ValueError("Number of elements does not match the specified size.")
        self.sequence = Sequence(elements)

    def _print_output(self):
        print(self.sorted_sequence)
        print(self.swap_count)


if __name__ == "__main__":
    app = SelectionSortApp()
    app.run()