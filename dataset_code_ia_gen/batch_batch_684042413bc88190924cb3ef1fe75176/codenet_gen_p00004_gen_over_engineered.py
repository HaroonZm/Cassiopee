import sys
from abc import ABC, abstractmethod
from typing import List, Tuple

class EquationSystem(ABC):
    @abstractmethod
    def solve(self) -> Tuple[float, float]:
        pass

class TwoVariableLinearSystem(EquationSystem):
    def __init__(self, coefficients: List[float]):
        if len(coefficients) != 6:
            raise ValueError("Exactly six coefficients must be provided.")
        self.a, self.b, self.c, self.d, self.e, self.f = coefficients
    
    def _determinant(self) -> float:
        return self.a * self.e - self.b * self.d
    
    def solve(self) -> Tuple[float, float]:
        det = self._determinant()
        if det == 0:
            raise ValueError("The system does not have a unique solution.")
        x = (self.c * self.e - self.b * self.f) / det
        y = (self.a * self.f - self.c * self.d) / det
        return (x, y)

class Formatter(ABC):
    @abstractmethod
    def format(self, values: Tuple[float, ...]) -> str:
        pass

class FixedDecimalFormatter(Formatter):
    def __init__(self, precision: int):
        self.precision = precision
        self.format_string = "{0:." + str(precision) + "f}"
    
    def format(self, values: Tuple[float, ...]) -> str:
        return " ".join(self.format_string.format(v) for v in values)

class EquationSolverEngine:
    def __init__(self, system_factory, formatter: Formatter):
        self.system_factory = system_factory
        self.formatter = formatter
    
    def process_input_line(self, line: str) -> str:
        tokens = line.strip().split()
        if len(tokens) != 6:
            raise ValueError("Each input line must have exactly six numbers.")
        coefficients = list(map(float, tokens))
        system = self.system_factory(coefficients)
        solution = system.solve()
        return self.formatter.format(solution)
    
    def run(self):
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                output = self.process_input_line(line)
                print(output)
            except Exception as e:
                # For this problem, we assume unique solutions, so no error handling needed
                # But in real case, we might want to log or handle error differently
                print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    solver_engine = EquationSolverEngine(TwoVariableLinearSystem, FixedDecimalFormatter(3))
    solver_engine.run()