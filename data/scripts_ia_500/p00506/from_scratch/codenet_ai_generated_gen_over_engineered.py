from typing import List, Protocol
from math import gcd
from functools import reduce


class IReadInput(Protocol):
    def read(self) -> List[int]:
        ...


class IWriteOutput(Protocol):
    def write(self, data: List[int]) -> None:
        ...


class ConsoleReadInput:
    def read(self) -> List[int]:
        n_line = input().strip()
        n = int(n_line)  # though n is not necessarily used directly
        numbers_line = input().strip()
        numbers = list(map(int, numbers_line.split()))
        if not (2 <= n <= 3) or len(numbers) != n:
            raise ValueError("Input constraints violated")
        return numbers


class ConsoleWriteOutput:
    def write(self, data: List[int]) -> None:
        for divisor in data:
            print(divisor)


class GCDProcessor:
    @staticmethod
    def compute_gcd(numbers: List[int]) -> int:
        return reduce(gcd, numbers)


class DivisorsFinder:
    @staticmethod
    def find_divisors(number: int) -> List[int]:
        divisors = []
        i = 1
        while i * i <= number:
            if number % i == 0:
                divisors.append(i)
                if i != number // i:
                    divisors.append(number // i)
            i += 1
        return sorted(divisors)


class CommonDivisorsEngine:
    def __init__(
        self,
        input_reader: IReadInput,
        output_writer: IWriteOutput,
        gcd_processor: GCDProcessor,
        divisors_finder: DivisorsFinder,
    ):
        self._input_reader = input_reader
        self._output_writer = output_writer
        self._gcd_processor = gcd_processor
        self._divisors_finder = divisors_finder

    def run(self) -> None:
        numbers = self._input_reader.read()
        common_gcd = self._gcd_processor.compute_gcd(numbers)
        common_divisors = self._divisors_finder.find_divisors(common_gcd)
        self._output_writer.write(common_divisors)


def main():
    input_reader = ConsoleReadInput()
    output_writer = ConsoleWriteOutput()
    gcd_processor = GCDProcessor()
    divisors_finder = DivisorsFinder()
    engine = CommonDivisorsEngine(
        input_reader, output_writer, gcd_processor, divisors_finder
    )
    engine.run()


if __name__ == "__main__":
    main()