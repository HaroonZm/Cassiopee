import sys
from abc import ABC, abstractmethod
from typing import Iterator, Tuple, Optional

class InputSource(ABC):
    @abstractmethod
    def read_pairs(self) -> Iterator[Tuple[int, int]]:
        pass

class StdInInputSource(InputSource):
    def read_pairs(self) -> Iterator[Tuple[int, int]]:
        for line in sys.stdin:
            line = line.strip()
            if line == '':
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                a, b = int(parts[0]), int(parts[1])
                yield a, b
            except ValueError:
                continue

class Validator(ABC):
    @abstractmethod
    def validate(self, pair: Tuple[int, int]) -> bool:
        pass

class RangeValidator(Validator):
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

    def validate(self, pair: Tuple[int, int]) -> bool:
        a, b = pair
        return self.min_val <= a <= self.max_val and self.min_val <= b <= self.max_val

class Operation(ABC):
    @abstractmethod
    def compute(self, pair: Tuple[int, int]) -> int:
        pass

class SumOperation(Operation):
    def compute(self, pair: Tuple[int, int]) -> int:
        a, b = pair
        return a + b

class OutputSink(ABC):
    @abstractmethod
    def write(self, value: int) -> None:
        pass

class StdOutOutputSink(OutputSink):
    def write(self, value: int) -> None:
        print(value)

class APlusBProcessor:
    def __init__(self, input_source: InputSource, validator: Validator,
                 operation: Operation, output_sink: OutputSink):
        self.input_source = input_source
        self.validator = validator
        self.operation = operation
        self.output_sink = output_sink

    def process(self) -> None:
        for pair in self.input_source.read_pairs():
            if self.validator.validate(pair):
                result = self.operation.compute(pair)
                self.output_sink.write(result)
            else:
                # Could extend for logging or error handling
                pass

def main() -> None:
    input_source = StdInInputSource()
    validator = RangeValidator(-1000, 1000)
    operation = SumOperation()
    output_sink = StdOutOutputSink()
    processor = APlusBProcessor(input_source, validator, operation, output_sink)
    processor.process()

if __name__ == "__main__":
    main()