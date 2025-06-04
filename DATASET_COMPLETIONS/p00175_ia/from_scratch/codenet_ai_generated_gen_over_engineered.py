from abc import ABC, abstractmethod
from typing import List, Optional, Iterator


class NumberBaseConverter(ABC):
    """
    Abstract base class for number base conversion.
    Designed for future extension to various numeral systems.
    """

    @abstractmethod
    def convert_to_base(self, n: int) -> str:
        pass


class Base4Converter(NumberBaseConverter):
    """
    Converter from decimal (base 10) to base 4 numeral system.
    """

    def __init__(self):
        self.digits = ['0', '1', '2', '3']

    def convert_to_base(self, n: int) -> str:
        if n == 0:
            return '0'
        digits_reversed = []
        number = n
        while number > 0:
            remainder = number % 4
            digits_reversed.append(self.digits[remainder])
            number //=4
        return ''.join(reversed(digits_reversed))


class InputDataReader:
    """
    Reads multiple integer inputs until termination signal.
    """

    def __init__(self, termination_value: int = -1):
        self.termination_value = termination_value

    def read_inputs(self) -> Iterator[int]:
        while True:
            line = input()
            if line.strip() == '':
                continue
            try:
                val = int(line)
            except ValueError:
                continue
            if val == self.termination_value:
                break
            if 0 <= val <= 1_000_000:
                yield val
            else:
                continue


class FourBaseNumberProcessor:
    """
    Processes multiple input integers converting them to base 4.
    """

    def __init__(self, converter: NumberBaseConverter, reader: InputDataReader):
        self.converter = converter
        self.reader = reader

    def process(self) -> List[str]:
        results = []
        for number in self.reader.read_inputs():
            results.append(self.converter.convert_to_base(number))
        return results


class FourBaseApplication:
    """
    Encapsulates the entire application lifecycle.
    """

    def __init__(self):
        self.converter = Base4Converter()
        self.reader = InputDataReader()
        self.processor = FourBaseNumberProcessor(self.converter, self.reader)

    def run(self) -> None:
        results = self.processor.process()
        for res in results:
            print(res)


if __name__ == "__main__":
    app = FourBaseApplication()
    app.run()