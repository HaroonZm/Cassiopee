from abc import ABC, abstractmethod
from typing import List, Iterator

class NumeralSystem(ABC):
    @abstractmethod
    def encode(self, num: int) -> str:
        pass

    @abstractmethod
    def decode(self, representation: str) -> int:
        pass

class NegativeBaseNumeralSystem(NumeralSystem):
    def __init__(self, base: int):
        if base >= 0:
            raise ValueError("Base must be negative for NegativeBaseNumeralSystem")
        self.base = base

    def encode(self, num: int) -> str:
        """
        Converts a decimal integer to its representation in the negative base numeral system.
        For this task, base = -10.
        """
        if num == 0:
            return '0'
        digits: List[str] = []
        n = num
        while n != 0:
            n, remainder = divmod(n, self.base)
            # Adjust remainder and quotient if remainder is negative
            if remainder < 0:
                remainder -= self.base
                n += 1
            digits.append(str(remainder))
        digits.reverse()
        return ''.join(digits)

    def decode(self, representation: str) -> int:
        """
        Converts a negative-base numeral system string back to a decimal integer.
        """
        result = 0
        length = len(representation)
        for i, ch in enumerate(representation):
            digit = int(ch)
            power = length - i - 1
            result += digit * (self.base ** power)
        return result

class DataSetProcessor:
    def __init__(self, numeral_system: NumeralSystem):
        self.numeral_system = numeral_system

    def process(self, inputs: Iterator[int]) -> Iterator[str]:
        for num in inputs:
            if num == 0:
                break
            yield self.numeral_system.encode(num)

class InputReader:
    def __init__(self, source: Iterator[str]):
        self.source = source

    def read_ints(self) -> Iterator[int]:
        for line in self.source:
            line = line.strip()
            if not line:
                continue
            yield int(line)

class LibraryNumberFormatter:
    def __init__(self):
        # base is fixed at -10 per problem statement
        self.numeral_system = NegativeBaseNumeralSystem(-10)
        self.processor = DataSetProcessor(self.numeral_system)

    def format_numbers(self, numbers: Iterator[int]) -> Iterator[str]:
        return self.processor.process(numbers)

def main():
    import sys
    input_reader = InputReader(sys.stdin)
    library_formatter = LibraryNumberFormatter()
    for formatted in library_formatter.format_numbers(input_reader.read_ints()):
        print(formatted)

if __name__ == "__main__":
    main()