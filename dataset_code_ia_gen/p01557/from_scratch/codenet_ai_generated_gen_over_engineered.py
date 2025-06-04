from abc import ABC, abstractmethod
from collections import deque
from typing import List, Tuple, Set


class Permutation(ABC):
    @abstractmethod
    def is_sorted(self) -> bool:
        pass

    @abstractmethod
    def reverse_subsegment(self, i: int, j: int) -> 'Permutation':
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass


class IntListPermutation(Permutation):
    def __init__(self, data: List[int]):
        self.data = data

    def is_sorted(self) -> bool:
        return all(self.data[i] < self.data[i + 1] for i in range(len(self.data) - 1))

    def reverse_subsegment(self, i: int, j: int) -> 'IntListPermutation':
        # i, j are 1-based inclusive indices
        new_data = (
            self.data[:i - 1]
            + list(reversed(self.data[i - 1:j]))
            + self.data[j:]
        )
        return IntListPermutation(new_data)

    def serialize(self) -> str:
        return ','.join(map(str, self.data))

    def __hash__(self) -> int:
        return hash(self.serialize())

    def __eq__(self, other) -> bool:
        return isinstance(other, IntListPermutation) and self.data == other.data

    def __str__(self) -> str:
        return ' '.join(map(str, self.data))


class Operation(ABC):
    @abstractmethod
    def apply(self, perm: Permutation) -> Permutation:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ReverseOperation(Operation):
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def apply(self, perm: Permutation) -> Permutation:
        return perm.reverse_subsegment(self.i, self.j)

    def __str__(self) -> str:
        return f"reverse({self.i},{self.j})"


class ReverseSortSolver:
    def __init__(self, initial_perm: Permutation):
        self.initial_perm = initial_perm
        self.target_perm = IntListPermutation(sorted(initial_perm.data))
        self.n = len(initial_perm.data)

    def solve(self) -> Tuple[int, List[Operation]]:
        if self.initial_perm.is_sorted():
            return 0, []

        visited: Set[str] = set()
        queue = deque()
        # Each item in queue: (Permutation, List of Operations)
        queue.append((self.initial_perm, []))
        visited.add(self.initial_perm.serialize())

        while queue:
            current_perm, ops = queue.popleft()

            if current_perm.is_sorted():
                return len(ops), ops

            for i in range(1, self.n + 1):
                for j in range(i, self.n + 1):
                    op = ReverseOperation(i, j)
                    next_perm = op.apply(current_perm)
                    serial = next_perm.serialize()
                    if serial not in visited:
                        visited.add(serial)
                        queue.append((next_perm, ops + [op]))
        # The problem guarantees a solution; this point theoretically unreachable.
        raise RuntimeError("No solution found")


class InputParser:
    @staticmethod
    def parse_input() -> Permutation:
        n = int(input().strip())
        data = list(map(int, input().strip().split()))
        assert len(data) == n
        return IntListPermutation(data)


class OutputWriter:
    @staticmethod
    def write_result(step_count: int):
        print(step_count)


def main():
    perm = InputParser.parse_input()
    solver = ReverseSortSolver(perm)
    steps, operations = solver.solve()
    OutputWriter.write_result(steps)


if __name__ == "__main__":
    main()