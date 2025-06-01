class AbstractNumberBaseConverter:
    def __init__(self, base: int):
        self._base = base

    def convert(self, number: int) -> str:
        raise NotImplementedError("Subclasses should implement this method.")

    def _digit_to_char(self, digit: int) -> str:
        if 0 <= digit <= 9:
            return str(digit)
        raise ValueError("Digit out of range for base conversion.")

class NegativeBaseConverter(AbstractNumberBaseConverter):
    def __init__(self, base: int):
        if base >= 0:
            raise ValueError("Base must be negative for NegativeBaseConverter.")
        super().__init__(base)

    def convert(self, number: int) -> str:
        if number == 0:
            return '0'
        digits = []
        n = number
        base = self._base
        while n != 0:
            n, remainder = divmod(n, base)
            if remainder < 0:
                n += 1
                remainder -= base
            digits.append(self._digit_to_char(remainder))
        return ''.join(reversed(digits))

class MinusDecimalNumber:
    """
    Represents a number in a negative base decimal system, specifically base -10.
    """
    def __init__(self, value: int):
        self._value = value
        self._converter = NegativeBaseConverter(-10)

    def to_minus_decimal_notation(self) -> str:
        return self._converter.convert(self._value)

class InputHandler:
    """
    Handles input stream, yielding dataset integers until zero is encountered.
    """
    def __init__(self, input_stream):
        self._input_stream = input_stream

    def read_numbers(self):
        for line in self._input_stream:
            line = line.strip()
            if not line:
                continue
            number = int(line)
            if number == 0:
                break
            yield number

class OutputHandler:
    """
    Handles output of numbers in minus decimal notation.
    """
    def __init__(self, output_stream):
        self._output_stream = output_stream

    def output(self, minus_decimal_str: str):
        print(minus_decimal_str, file=self._output_stream)

class MinusDecimalConverterApplication:
    """
    Orchestrates the conversion of integers to minus decimal notation.
    """

    def __init__(self, input_stream, output_stream):
        self._input_handler = InputHandler(input_stream)
        self._output_handler = OutputHandler(output_stream)

    def run(self):
        for number in self._input_handler.read_numbers():
            minus_decimal_number = MinusDecimalNumber(number)
            converted = minus_decimal_number.to_minus_decimal_notation()
            self._output_handler.output(converted)

import sys

if __name__ == "__main__":
    app = MinusDecimalConverterApplication(sys.stdin, sys.stdout)
    app.run()