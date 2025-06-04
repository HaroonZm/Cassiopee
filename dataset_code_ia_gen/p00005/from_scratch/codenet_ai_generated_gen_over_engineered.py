import sys
from typing import Tuple, Iterator, List

class IntegerPair:
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b
    
    @property
    def a(self) -> int:
        return self._a
    
    @property
    def b(self) -> int:
        return self._b

class MathUtils:
    @staticmethod
    def gcd(x: int, y: int) -> int:
        # Euclidean algorithm with type checking for future extensions
        a, b = abs(x), abs(y)
        while b != 0:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(x: int, y: int, gcd_value: int = None) -> int:
        # Calculate LCM using GCD; gcd_value can be precomputed for optimization
        if gcd_value is None:
            gcd_value = MathUtils.gcd(x, y)
        return (x // gcd_value) * y

class InputProvider:
    # Abstract input source, facilitating future input types (e.g. file, network)
    def __init__(self, source=sys.stdin):
        self.source = source
    
    def lines(self) -> Iterator[str]:
        for line in self.source:
            yield line.strip()

class DataParser:
    @staticmethod
    def parse_line_to_integer_pair(line: str) -> IntegerPair:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError(f"Expected exactly two integers per line, got: {line}")
        a, b = map(int, parts)
        return IntegerPair(a, b)

class OutputHandler:
    # Abstract output manager for potential future extensions (logging, file output, etc.)
    def __init__(self, output=sys.stdout):
        self.output = output
    
    def print_result(self, gcd_value: int, lcm_value: int):
        print(f"{gcd_value} {lcm_value}", file=self.output)

class GcdLcmProcessor:
    # Encapsulated logic handling the problem solution
    def __init__(self, input_provider: InputProvider, output_handler: OutputHandler):
        self.input_provider = input_provider
        self.output_handler = output_handler
    
    def process(self):
        for line in self.input_provider.lines():
            if not line:
                continue  # skip empty lines
            pair = DataParser.parse_line_to_integer_pair(line)
            gcd_val = MathUtils.gcd(pair.a, pair.b)
            lcm_val = MathUtils.lcm(pair.a, pair.b, gcd_val)
            self.output_handler.print_result(gcd_val, lcm_val)

def main():
    input_provider = InputProvider()
    output_handler = OutputHandler()
    processor = GcdLcmProcessor(input_provider, output_handler)
    processor.process()

if __name__ == "__main__":
    main()