import sys
from typing import Iterator, Tuple, Protocol

class NumberPair(Protocol):
    def a(self) -> int: ...
    def b(self) -> int: ...

class ImmutablePair:
    __slots__ = ('_a', '_b')

    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b
    
    @property
    def a(self) -> int:
        return self._a
    
    @property
    def b(self) -> int:
        return self._b

class GCDLCMCalculator:
    def compute_gcd(self, x: int, y: int) -> int:
        # Euclidean algorithm
        while y != 0:
            x, y = y, x % y
        return x
    
    def compute_lcm(self, x: int, y: int) -> int:
        gcd_val = self.compute_gcd(x, y)
        # To avoid overflow and stay in constraints:
        return x // gcd_val * y

    def calculate(self, pair: NumberPair) -> Tuple[int, int]:
        gcd = self.compute_gcd(pair.a, pair.b)
        lcm = self.compute_lcm(pair.a, pair.b)
        return gcd, lcm

class LineParser:
    def parse_line(self, line: str) -> NumberPair:
        splitted = line.strip().split()
        if len(splitted) != 2:
            raise ValueError("Input line does not contain exactly two values")
        a, b = map(int, splitted)
        if a <= 0 or b <= 0:
            raise ValueError("Values must be greater than 0")
        return ImmutablePair(a, b)

class InputProvider:
    def __init__(self, stream):
        self._stream = stream

    def __iter__(self) -> Iterator[NumberPair]:
        parser = LineParser()
        for line in self._stream:
            if line.strip():
                try:
                    yield parser.parse_line(line)
                except Exception as e:
                    # Gracefully ignore or log bad lines if needed
                    # For now, just silently continue
                    continue

class OutputConsumer:
    def print_result(self, gcd: int, lcm: int) -> None:
        print(f"{gcd} {lcm}")

class GCDLCMApplication:
    def __init__(self, input_stream):
        self.input_provider = InputProvider(input_stream)
        self.calculator = GCDLCMCalculator()
        self.output_consumer = OutputConsumer()
    
    def run(self) -> None:
        for pair in self.input_provider:
            gcd, lcm = self.calculator.calculate(pair)
            self.output_consumer.print_result(gcd, lcm)

def main():
    app = GCDLCMApplication(sys.stdin)
    app.run()

if __name__ == "__main__":
    main()