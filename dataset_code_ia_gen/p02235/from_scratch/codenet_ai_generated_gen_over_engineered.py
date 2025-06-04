from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator

class Sequence(ABC):
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def char_at(self, index: int) -> str:
        pass

class AlphabeticalSequence(Sequence):
    def __init__(self, sequence: str):
        self._sequence = sequence
    
    def __len__(self) -> int:
        return len(self._sequence)
    
    def char_at(self, index: int) -> str:
        return self._sequence[index]

class LcsResult:
    def __init__(self, length: int, subseq: str = ''):
        self.length = length
        self.subseq = subseq

class LcsSolver(ABC):
    @abstractmethod
    def solve(self, seq1: Sequence, seq2: Sequence) -> LcsResult:
        pass

class DynamicProgrammingLcsSolver(LcsSolver):
    def solve(self, seq1: Sequence, seq2: Sequence) -> LcsResult:
        m = len(seq1)
        n = len(seq2)
        
        # We only need length according to problem, but store full DP for extensibility
        dp: List[List[int]] = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            c1 = seq1.char_at(i-1)
            for j in range(1, n+1):
                c2 = seq2.char_at(j-1)
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # LCS length only as per requirements
        return LcsResult(length=dp[m][n])

class DatasetParser:
    def __init__(self, input_iter: Iterator[str]):
        self._input_iter = input_iter
    
    def read_int(self) -> int:
        return int(next(self._input_iter).strip())
    
    def read_sequence(self) -> AlphabeticalSequence:
        return AlphabeticalSequence(next(self._input_iter).strip())
    
    def read_datasets(self) -> List[Tuple[AlphabeticalSequence, AlphabeticalSequence]]:
        q = self.read_int()
        datasets = []
        for _ in range(q):
            x = self.read_sequence()
            y = self.read_sequence()
            datasets.append((x, y))
        return datasets

class LcsApplication:
    def __init__(self, solver: LcsSolver):
        self._solver = solver
    
    def run(self):
        import sys
        input_iter = iter(sys.stdin.readlines())
        parser = DatasetParser(input_iter)
        datasets = parser.read_datasets()
        
        # For extensibility, we separate compute and output
        results = self._compute_all(datasets)
        self._output_all(results)
    
    def _compute_all(self, datasets: List[Tuple[Sequence, Sequence]]) -> List[LcsResult]:
        return [self._solver.solve(x, y) for x, y in datasets]
    
    def _output_all(self, results: List[LcsResult]):
        for result in results:
            print(result.length)

if __name__ == "__main__":
    solver = DynamicProgrammingLcsSolver()
    app = LcsApplication(solver)
    app.run()