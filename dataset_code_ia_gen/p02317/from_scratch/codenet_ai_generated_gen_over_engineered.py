from abc import ABC, abstractmethod
from typing import List, Optional

class SequenceInputSource(ABC):
    @abstractmethod
    def read_length(self) -> int:
        pass

    @abstractmethod
    def read_sequence(self, length: int) -> List[int]:
        pass

class StdInputSequenceSource(SequenceInputSource):
    def read_length(self) -> int:
        return int(input())

    def read_sequence(self, length: int) -> List[int]:
        seq = []
        for _ in range(length):
            seq.append(int(input()))
        return seq

class LongestIncreasingSubsequenceStrategy(ABC):
    @abstractmethod
    def compute(self, sequence: List[int]) -> int:
        pass

class PatienceSortingLISStrategy(LongestIncreasingSubsequenceStrategy):
    def compute(self, sequence: List[int]) -> int:
        import bisect
        piles = []
        for x in sequence:
            # find leftmost pile top >= x
            pos = bisect.bisect_left(piles, x)
            if pos == len(piles):
                piles.append(x)
            else:
                piles[pos] = x
        return len(piles)

class LISContext:
    def __init__(self,
                 input_source: SequenceInputSource,
                 lis_strategy: LongestIncreasingSubsequenceStrategy):
        self.input_source = input_source
        self.lis_strategy = lis_strategy

    def run(self) -> int:
        n = self.input_source.read_length()
        sequence = self.input_source.read_sequence(n)
        result = self.lis_strategy.compute(sequence)
        return result

def main():
    input_source = StdInputSequenceSource()
    lis_strategy = PatienceSortingLISStrategy()
    context = LISContext(input_source, lis_strategy)
    print(context.run())

if __name__ == '__main__':
    main()