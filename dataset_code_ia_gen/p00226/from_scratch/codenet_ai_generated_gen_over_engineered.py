from abc import ABC, abstractmethod
from typing import Tuple, List


class InputSource(ABC):
    """Abstracts the source of input data sets."""
    
    @abstractmethod
    def read_dataset(self) -> Tuple[str, str]:
        """Reads one dataset (correct number and answer).
        
        Returns:
            Tuple[str, str]: A tuple of two strings (r, a).
                             Returns ('0', '0') to indicate end of input.
        """
        pass


class StdInputSource(InputSource):
    """Reads datasets from standard input."""
    
    def read_dataset(self) -> Tuple[str, str]:
        line = input().strip()
        if not line:
            return '0', '0'  # End marker if empty line encountered
        r, a = line.split()
        return r, a


class HitAndBlowCalculator:
    """Calculates hits and blows for Hit and Blow game."""
    
    def __init__(self, length: int = 4):
        self.length = length
        
    def calculate(self, correct: str, answer: str) -> Tuple[int, int]:
        """Calculate hit and blow counts.
        
        Args:
            correct (str): The correct 4-digit string.
            answer (str): The guessed 4-digit string.
            
        Returns:
            Tuple[int, int]: Number of hits and blows.
        """
        hit = sum(c == a for c, a in zip(correct, answer))
        
        # Count occurrences of each digit
        from collections import Counter
        correct_counts = Counter(correct)
        answer_counts = Counter(answer)
        
        # Total common digits
        common = sum((correct_counts & answer_counts).values())
        
        blow = common - hit
        return hit, blow


class HitAndBlowGame:
    """Handles multiple datasets and prints results."""
    
    def __init__(self, input_source: InputSource, calculator: HitAndBlowCalculator):
        self.input_source = input_source
        self.calculator = calculator
        self.results: List[Tuple[int, int]] = []
        
    def run(self):
        while True:
            r, a = self.input_source.read_dataset()
            # End condition
            if r == '0' and a == '0':
                break
            hit, blow = self.calculator.calculate(r, a)
            self.results.append((hit, blow))
            
    def output_results(self):
        for hit, blow in self.results:
            print(hit, blow)


def main():
    input_source = StdInputSource()
    calculator = HitAndBlowCalculator(length=4)
    game = HitAndBlowGame(input_source, calculator)
    game.run()
    game.output_results()


if __name__ == "__main__":
    main()