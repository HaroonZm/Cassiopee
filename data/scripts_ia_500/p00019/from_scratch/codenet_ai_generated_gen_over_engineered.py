from abc import ABC, abstractmethod
from typing import Protocol


class InputReader(ABC):
    @abstractmethod
    def read(self) -> int:
        pass


class StdInputReader(InputReader):
    def read(self) -> int:
        line = input().strip()
        try:
            value = int(line)
        except ValueError:
            raise ValueError("Input must be an integer")
        if not (1 <= value <= 20):
            raise ValueError("Input must be between 1 and 20 inclusive")
        return value


class FactorialCalculator(ABC):
    @abstractmethod
    def factorial(self, n: int) -> int:
        pass


class RecursiveFactorialCalculator(FactorialCalculator):
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


class IterativeFactorialCalculator(FactorialCalculator):
    def factorial(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


class OutputWriter(ABC):
    @abstractmethod
    def write(self, value: int) -> None:
        pass


class StdOutputWriter(OutputWriter):
    def write(self, value: int) -> None:
        print(value)


class FactorialApplication:
    def __init__(
        self,
        reader: InputReader,
        calculator: FactorialCalculator,
        writer: OutputWriter
    ):
        self.reader = reader
        self.calculator = calculator
        self.writer = writer

    def run(self) -> None:
        n = self.reader.read()
        result = self.calculator.factorial(n)
        self.writer.write(result)


def main():
    reader = StdInputReader()
    # Using iterative for performance but either works for n <= 20
    calculator = IterativeFactorialCalculator()
    writer = StdOutputWriter()

    app = FactorialApplication(reader, calculator, writer)
    app.run()


if __name__ == "__main__":
    main()