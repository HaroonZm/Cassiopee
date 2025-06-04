from abc import ABC, abstractmethod
from typing import List, Iterator

class Operation(ABC):
    @abstractmethod
    def is_applicable(self, n: int) -> bool:
        pass

    @abstractmethod
    def apply(self, n: int) -> int:
        pass

class EvenOperation(Operation):
    def is_applicable(self, n: int) -> bool:
        return n % 2 == 0

    def apply(self, n: int) -> int:
        return n // 2

class OddOperation(Operation):
    def is_applicable(self, n: int) -> bool:
        return n % 2 == 1

    def apply(self, n: int) -> int:
        return 3 * n + 1

class CollatzStepChooser:
    def __init__(self, operations: List[Operation]):
        self.operations = operations

    def choose(self, n: int) -> Operation:
        for op in self.operations:
            if op.is_applicable(n):
                return op
        raise ValueError("No applicable operation found")

class CollatzSequence:
    def __init__(self, chooser: CollatzStepChooser, upper_bound: int = 1_000_000):
        self.chooser = chooser
        self.upper_bound = upper_bound

    def __iter__(self) -> Iterator[int]:
        # This iterator is undefined at initialization: user must call with start n
        raise NotImplementedError("Use start(n) method to get iterator for sequence from n")

    def start(self, n: int) -> Iterator[int]:
        current = n
        yield current
        while current != 1:
            if current > self.upper_bound:
                raise ValueError(f"Value {current} exceeded upper bound {self.upper_bound}")
            op = self.chooser.choose(current)
            current = op.apply(current)
            yield current

class InputParser:
    def __init__(self):
        self._max_data_sets = 50

    def parse(self) -> List[int]:
        results = []
        count = 0
        while count < self._max_data_sets:
            try:
                line = input().strip()
            except EOFError:
                break
            if line == '0':
                break
            if not line.isdigit():
                continue
            n = int(line)
            if n < 1 or n > 1_000_000:
                continue
            results.append(n)
            count += 1
        return results

class CollatzCounter:
    def __init__(self, collatz_sequence: CollatzSequence):
        self.collatz_sequence = collatz_sequence

    def count_steps(self, n: int) -> int:
        iterator = self.collatz_sequence.start(n)
        next(iterator)  # skip initial value itself
        count = 0
        for _ in iterator:
            count += 1
        return count

def main() -> None:
    even_op = EvenOperation()
    odd_op = OddOperation()
    chooser = CollatzStepChooser([even_op, odd_op])
    collatz_seq = CollatzSequence(chooser)
    parser = InputParser()
    counter = CollatzCounter(collatz_seq)

    inputs = parser.parse()
    for n in inputs:
        try:
            steps = counter.count_steps(n)
        except ValueError:
            # According to problem constraints, this should never happen, but handle gracefully
            steps = -1
        print(steps)

if __name__ == "__main__":
    main()