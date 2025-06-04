from typing import List, Callable

class DigitSequence:
    def __init__(self, digits: List[int]):
        self._digits = digits

    def length(self) -> int:
        return len(self._digits)

    def digit_at(self, index: int) -> int:
        if 0 <= index < self.length():
            return self._digits[index]
        raise IndexError("Index out of range")

    def __iter__(self):
        return iter(self._digits)

    def __repr__(self):
        return ''.join(str(d) for d in self._digits)

class DigitRemoverStrategy:
    def remove_digits(self, sequence: DigitSequence, k: int) -> DigitSequence:
        raise NotImplementedError()

class GreedyDigitRemover(DigitRemoverStrategy):
    def remove_digits(self, sequence: DigitSequence, k: int) -> DigitSequence:
        # This method removes k digits to form the largest possible number
        stack: List[int] = []
        to_remove = k
        for digit in sequence:
            while stack and to_remove > 0 and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        if to_remove > 0:
            stack = stack[:-to_remove]
        return DigitSequence(stack)

class DigitSequenceFactory:
    @staticmethod
    def create_from_list(digits: List[int]) -> DigitSequence:
        return DigitSequence(digits)

class DigitGameContext:
    def __init__(self, remover_strategy: DigitRemoverStrategy):
        self._remover_strategy = remover_strategy

    def get_max_point_number(self, sequence: DigitSequence, k: int) -> DigitSequence:
        return self._remover_strategy.remove_digits(sequence, k)

class InputParser:
    def __init__(self, input_supplier: Callable[[], str]):
        self._input_supplier = input_supplier

    def parse(self) -> (DigitSequence, int):
        line1 = self._input_supplier().strip()
        n, k = map(int, line1.split())
        line2 = self._input_supplier().strip()
        digits = list(map(int, line2.split()))
        if len(digits) != n:
            raise ValueError("Number of digits does not match N")
        return DigitSequenceFactory.create_from_list(digits), k

class OutputFormatter:
    @staticmethod
    def format_digit_sequence(sequence: DigitSequence) -> str:
        return ''.join(str(d) for d in sequence)

def main():
    import sys
    input_lines = iter(sys.stdin.readline, '')
    parser = InputParser(lambda: next(input_lines))
    sequence, k = parser.parse()
    context = DigitGameContext(GreedyDigitRemover())
    max_point_sequence = context.get_max_point_number(sequence, k)
    output = OutputFormatter.format_digit_sequence(max_point_sequence)
    print(output)

if __name__ == "__main__":
    main()