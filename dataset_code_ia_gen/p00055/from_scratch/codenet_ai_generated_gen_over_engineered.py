from abc import ABC, abstractmethod
from typing import List, Iterator

class TermStrategy(ABC):
    @abstractmethod
    def compute_term(self, prev_term: float) -> float:
        pass

class EvenTermStrategy(TermStrategy):
    def compute_term(self, prev_term: float) -> float:
        return prev_term * 2

class OddTermStrategy(TermStrategy):
    def compute_term(self, prev_term: float) -> float:
        return prev_term / 3

class TermStrategyFactory:
    def get_strategy(self, index: int) -> TermStrategy:
        if index % 2 == 0:
            return EvenTermStrategy()
        else:
            return OddTermStrategy()

class SequenceGenerator:
    def __init__(self, initial_term: float, length: int, strategy_factory: TermStrategyFactory):
        self.initial_term = initial_term
        self.length = length
        self.strategy_factory = strategy_factory

    def generate(self) -> List[float]:
        terms = [self.initial_term]
        for i in range(1, self.length):
            strategy = self.strategy_factory.get_strategy(i)
            next_term = strategy.compute_term(terms[-1])
            terms.append(next_term)
        return terms

class SequenceSummation:
    def __init__(self, sequence: List[float]):
        self.sequence = sequence

    def sum_terms(self) -> float:
        return sum(self.sequence)

class InputReader:
    def __init__(self):
        self._input_lines = []

    def read_all_inputs(self) -> Iterator[float]:
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line:
                yield float(line)

class OutputWriter:
    def write(self, value: float) -> None:
        print(f"{value:.8f}")

class SequenceProcessor:
    def __init__(self, term_count: int = 10):
        self.term_count = term_count
        self.strategy_factory = TermStrategyFactory()
        self.output_writer = OutputWriter()

    def process(self, initial_term: float) -> None:
        generator = SequenceGenerator(initial_term, self.term_count, self.strategy_factory)
        terms = generator.generate()
        summation = SequenceSummation(terms)
        result = summation.sum_terms()
        self.output_writer.write(result)

def main():
    input_reader = InputReader()
    processor = SequenceProcessor(term_count=10)
    for initial_term in input_reader.read_all_inputs():
        processor.process(initial_term)

if __name__ == "__main__":
    main()