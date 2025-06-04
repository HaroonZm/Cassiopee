from abc import ABC, abstractmethod
from typing import List, Iterable

class DigitSequence(ABC):
    """
    Abstract base class for sequences of digits.
    """
    @abstractmethod
    def build_lower_row(self) -> 'DigitSequence':
        pass
    
    @abstractmethod
    def get_last_row_digit(self) -> int:
        pass


class ModuloDigitSequence(DigitSequence):
    """
    Concrete implementation representing a row of digits with a specific modulo rule.
    """
    def __init__(self, digits: List[int]) -> None:
        self.digits = digits
        
    def build_lower_row(self) -> 'ModuloDigitSequence':
        # Applies the rule: C = (A + B) % 10 for adjacent pairs A, B
        new_digits = [(self.digits[i] + self.digits[i+1]) % 10 for i in range(len(self.digits)-1)]
        return ModuloDigitSequence(new_digits)
    
    def get_last_row_digit(self) -> int:
        # Terminal condition when length is 1
        if len(self.digits) == 1:
            return self.digits[0]
        else:
            # Recursively reduce rows
            return self.build_lower_row().get_last_row_digit()
    
    def __repr__(self) -> str:
        return f"ModuloDigitSequence({self.digits})"


class DigitSequenceFactory:
    """
    Factory class for creating DigitSequence objects.
    Enables future extensions for different rules or formats.
    """
    @staticmethod
    def from_string(data: str) -> DigitSequence:
        digits = [int(ch) for ch in data.strip()]
        if len(digits) != 10:
            raise ValueError("Each input line must contain exactly 10 digits.")
        return ModuloDigitSequence(digits)


class DigitSequenceProcessor:
    """
    Processes multiple digit sequences, generating the bottom-most digit for each.
    """
    def __init__(self, input_lines: Iterable[str]) -> None:
        self.input_lines = input_lines
        
    def process_all(self) -> List[int]:
        results = []
        for line in self.input_lines:
            line = line.strip()
            if not line:
                continue
            sequence = DigitSequenceFactory.from_string(line)
            last_digit = sequence.get_last_row_digit()
            results.append(last_digit)
        return results


def main() -> None:
    import sys
    processor = DigitSequenceProcessor(sys.stdin)
    results = processor.process_all()
    for res in results:
        print(res)


if __name__ == "__main__":
    main()