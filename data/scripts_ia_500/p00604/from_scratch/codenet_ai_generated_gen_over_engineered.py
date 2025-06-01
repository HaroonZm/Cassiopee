from typing import List, Iterator
import sys
import abc

class IDataReader(abc.ABC):
    @abc.abstractmethod
    def read_dataset(self) -> List[int]:
        pass

class StdInDataReader(IDataReader):
    def __init__(self) -> None:
        self._lines = iter(sys.stdin.read().strip().split('\n'))
    
    def read_dataset(self) -> List[int]:
        try:
            n = next(self._lines)
            n = n.strip()
            if n == '':
                return []
            n_int = int(n)
            if n_int == 0:
                return []
            P_line = next(self._lines)
            P = list(map(int, P_line.strip().split()))
            if len(P) != n_int:
                raise ValueError("Length of problem times does not match N.")
            return P
        except StopIteration:
            return []

class PenaltyCalculatorStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_minimal_penalty(self, problem_times: List[int]) -> int:
        pass

class SortedPenaltyCalculator(PenaltyCalculatorStrategy):
    def calculate_minimal_penalty(self, problem_times: List[int]) -> int:
        # Sort in ascending order to minimize penalty sum of cumulative completion times
        sorted_times = sorted(problem_times)
        accumulated_time = 0
        penalty = 0
        for t in sorted_times:
            accumulated_time += t
            penalty += accumulated_time
        return penalty

class ProblemSolver:
    def __init__(self, reader: IDataReader, calculator: PenaltyCalculatorStrategy) -> None:
        self._reader = reader
        self._calculator = calculator
    
    def solve_all(self) -> Iterator[int]:
        while True:
            problem_times = self._reader.read_dataset()
            if not problem_times:
                break
            yield self._calculator.calculate_minimal_penalty(problem_times)

def main() -> None:
    reader = StdInDataReader()
    calculator = SortedPenaltyCalculator()
    solver = ProblemSolver(reader, calculator)
    for result in solver.solve_all():
        print(result)

if __name__ == "__main__":
    main()