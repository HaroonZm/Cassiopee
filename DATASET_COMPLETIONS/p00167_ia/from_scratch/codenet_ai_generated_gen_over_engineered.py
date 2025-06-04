class SortStrategy:
    def sort(self, data):
        raise NotImplementedError("SortStrategy requires an implementation of sort method")

class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        n = len(data)
        swap_count = 0

        # Representing the unsorted and sorted segments explicitly for abstraction
        # Not strictly necessary but to enhance extensibility
        for i in range(n):
            # Unsorted portion is from 0 to n-i-1
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swap_count += 1
            if n - i - 1 == 1:
                # When the unsorted partition length is 1, stop early
                break
        return swap_count

class InputParser:
    def __init__(self, input_source):
        self.input_source = input_source
        self.lines = self._line_generator()

    def _line_generator(self):
        for line in self.input_source:
            yield line.strip()

    def parse_datasets(self):
        while True:
            try:
                line = next(self.lines)
                if line == '0':
                    break
                n = int(line)
                data = []
                for _ in range(n):
                    data.append(int(next(self.lines)))
                yield data
            except StopIteration:
                break

class OutputHandler:
    @staticmethod
    def output_swap_count(count):
        print(count)

class BubbleSortProgram:
    def __init__(self, input_source):
        self.parser = InputParser(input_source)
        self.sorter = BubbleSortStrategy()
        self.output_handler = OutputHandler()

    def run(self):
        for dataset in self.parser.parse_datasets():
            # Copy dataset to avoid side-effects if needed for extensions
            working_data = list(dataset)
            swap_count = self.sorter.sort(working_data)
            self.output_handler.output_swap_count(swap_count)

if __name__ == "__main__":
    import sys
    program = BubbleSortProgram(sys.stdin)
    program.run()