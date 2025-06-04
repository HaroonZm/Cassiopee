from abc import ABC, abstractmethod
from typing import List, Protocol

class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...

class Number(Comparable):
    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other: "Number") -> bool:
        return self.value < other.value
    
    def __gt__(self, other: "Number") -> bool:
        return self.value > other.value

    def __repr__(self):
        return str(self.value)

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, items: List[Comparable]) -> List[Comparable]:
        pass

class DescendingSortStrategy(SortStrategy):
    def sort(self, items: List[Comparable]) -> List[Comparable]:
        # Highly abstracted sorting using built-in for simplicity
        return sorted(items, reverse=True)

class InputReader(ABC):
    @abstractmethod
    def read(self) -> List[Number]:
        pass

class ConsoleInputReader(InputReader):
    def read(self) -> List[Number]:
        raw_input = input()
        numbers = [Number(int(x)) for x in raw_input.strip().split()]
        if len(numbers) != 5:
            raise ValueError("Exactly five numbers are required.")
        return numbers

class OutputWriter(ABC):
    @abstractmethod
    def write(self, items: List[Number]) -> None:
        pass

class ConsoleOutputWriter(OutputWriter):
    def write(self, items: List[Number]) -> None:
        print(" ".join(str(n) for n in items))

class SortingContext:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def execute_sort(self, items: List[Comparable]) -> List[Comparable]:
        return self.strategy.sort(items)

def main():
    input_reader: InputReader = ConsoleInputReader()
    numbers = input_reader.read()

    sorter = SortingContext(DescendingSortStrategy())
    sorted_numbers = sorter.execute_sort(numbers)

    output_writer = ConsoleOutputWriter()
    output_writer.write(sorted_numbers)

if __name__ == "__main__":
    main()