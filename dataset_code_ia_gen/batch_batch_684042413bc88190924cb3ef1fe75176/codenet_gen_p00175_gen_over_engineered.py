from abc import ABC, abstractmethod
from typing import List, Optional

class NumberSystem(ABC):
    @abstractmethod
    def convert_from_decimal(self, n: int) -> str:
        pass

    @abstractmethod
    def convert_to_decimal(self, s: str) -> int:
        pass

class BaseFourNumberSystem(NumberSystem):
    def __init__(self):
        self.base = 4
        self.digits = ['0', '1', '2', '3']

    def convert_from_decimal(self, n: int) -> str:
        if n == 0:
            return '0'
        digits_reversed = []
        current = n
        while current > 0:
            remainder = current % self.base
            digits_reversed.append(self.digits[remainder])
            current //= self.base
        return ''.join(reversed(digits_reversed))

    def convert_to_decimal(self, s: str) -> int:
        result = 0
        for c in s:
            if c not in self.digits:
                raise ValueError(f"Invalid digit '{c}' for base {self.base}")
            result = result * self.base + self.digits.index(c)
        return result

class InputOutputHandler:
    def __init__(self, number_system: NumberSystem):
        self.number_system = number_system

    def process_input(self, lines: List[str]) -> List[str]:
        results = []
        for line in lines:
            line = line.strip()
            if line == '-1':
                break
            try:
                n = int(line)
                if not (0 <= n <= 1000000):
                    raise ValueError("Number out of allowed range")
                converted = self.number_system.convert_from_decimal(n)
                results.append(converted)
            except Exception as e:
                # In case of invalid input, here we just continue
                continue
        return results

class Program:
    def __init__(self):
        self.number_system = BaseFourNumberSystem()
        self.io_handler = InputOutputHandler(self.number_system)

    def run(self, input_lines: Optional[List[str]] = None):
        if input_lines is None:
            import sys
            input_lines = sys.stdin.read().splitlines()
        results = self.io_handler.process_input(input_lines)
        for res in results:
            print(res)

if __name__ == '__main__':
    program = Program()
    program.run()