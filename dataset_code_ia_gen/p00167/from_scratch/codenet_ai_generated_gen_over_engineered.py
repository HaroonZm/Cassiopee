from abc import ABC, abstractmethod
from typing import List, Iterator, Optional

class SwapCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get(self) -> int:
        return self.count

class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> int:
        """
        Sorts the data in place and returns the count of swaps performed.
        """
        pass

class BubbleSort(SortAlgorithm):
    def __init__(self, swap_counter: SwapCounter):
        self.swap_counter = swap_counter

    def sort(self, data: List[int]) -> int:
        n = len(data)
        self.swap_counter.reset()
        for unsorted_end in range(n, 1, -1):
            for i in range(unsorted_end - 1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    self.swap_counter.increment()
        return self.swap_counter.get()

class InputDataSet:
    def __init__(self, n: int, values: List[int]):
        self.n = n
        self.values = values

class InputParser(ABC):
    @abstractmethod
    def parse(self) -> Iterator[InputDataSet]:
        pass

class StdInputParser(InputParser):
    def __init__(self):
        pass

    def parse(self) -> Iterator[InputDataSet]:
        while True:
            line = self._read_line()
            if line is None:
                break
            n = self._parse_int(line)
            if n == 0:
                break
            values = []
            for _ in range(n):
                val_line = self._read_line()
                if val_line is None:
                    raise EOFError("Unexpected end of input.")
                val = self._parse_int(val_line)
                values.append(val)
            yield InputDataSet(n, values)

    @staticmethod
    def _read_line() -> Optional[str]:
        try:
            return input()
        except EOFError:
            return None

    @staticmethod
    def _parse_int(s: str) -> int:
        return int(s.strip())

class OutputPrinter(ABC):
    @abstractmethod
    def print_result(self, result: int) -> None:
        pass

class StdOutputPrinter(OutputPrinter):
    def print_result(self, result: int) -> None:
        print(result)

class BubbleSortApplication:
    def __init__(self,
                 input_parser: InputParser,
                 sorting_algo: SortAlgorithm,
                 output_printer: OutputPrinter):
        self.input_parser = input_parser
        self.sorting_algo = sorting_algo
        self.output_printer = output_printer

    def run(self) -> None:
        for data_set in self.input_parser.parse():
            # Defensive copy to avoid side effects on original input list if reused
            data_copy = list(data_set.values)
            swap_count = self.sorting_algo.sort(data_copy)
            self.output_printer.print_result(swap_count)

if __name__ == "__main__":
    swap_counter = SwapCounter()
    bubble_sort = BubbleSort(swap_counter)
    input_parser = StdInputParser()
    output_printer = StdOutputPrinter()
    app = BubbleSortApplication(input_parser, bubble_sort, output_printer)
    app.run()