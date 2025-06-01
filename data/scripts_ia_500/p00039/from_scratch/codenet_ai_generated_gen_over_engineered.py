from abc import ABC, abstractmethod
from typing import List, Dict, Iterator


class RomanNumeralConverterInterface(ABC):
    @abstractmethod
    def roman_to_arabic(self, roman: str) -> int:
        pass


class RomanSymbolRepositoryInterface(ABC):
    @abstractmethod
    def get_value(self, symbol: str) -> int:
        pass

    @abstractmethod
    def all_symbols(self) -> Iterator[str]:
        pass


class RomanSymbolRepository(RomanSymbolRepositoryInterface):
    def __init__(self):
        # Defining the Roman numerals mapping; ready for potential extension
        self._symbols: Dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def get_value(self, symbol: str) -> int:
        if symbol not in self._symbols:
            raise ValueError(f"Invalid Roman symbol: {symbol}")
        return self._symbols[symbol]

    def all_symbols(self) -> Iterator[str]:
        return iter(self._symbols.keys())


class RomanNumeralParser:
    def __init__(self, symbol_repo: RomanSymbolRepositoryInterface):
        self._symbol_repo = symbol_repo

    def parse(self, roman: str) -> List[int]:
        # Convert each Roman numeral character into its numeric value
        return [self._symbol_repo.get_value(ch) for ch in roman]


class RomanNumeralInterpreter(RomanNumeralConverterInterface):
    def __init__(self, parser: RomanNumeralParser):
        self._parser = parser

    def roman_to_arabic(self, roman: str) -> int:
        values = self._parser.parse(roman)

        result = 0
        prev_value = 0
        # Following the subtractive notation rules described
        for value in reversed(values):
            if value >= prev_value:
                result += value
            else:
                result -= value
            prev_value = value
        return result


class InputProvider(ABC):
    @abstractmethod
    def lines(self) -> Iterator[str]:
        pass


class StdInputProvider(InputProvider):
    def lines(self) -> Iterator[str]:
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line:
                yield line


class RomanNumeralConverterSystem:
    def __init__(self, input_provider: InputProvider, converter: RomanNumeralConverterInterface):
        self._input_provider = input_provider
        self._converter = converter

    def run(self):
        for roman_input in self._input_provider.lines():
            arabic = self._converter.roman_to_arabic(roman_input)
            print(arabic)


def main():
    symbol_repo = RomanSymbolRepository()
    parser = RomanNumeralParser(symbol_repo)
    converter = RomanNumeralInterpreter(parser)
    input_provider = StdInputProvider()
    system = RomanNumeralConverterSystem(input_provider, converter)
    system.run()


if __name__ == "__main__":
    main()