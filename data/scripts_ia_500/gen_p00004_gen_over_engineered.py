class EquationSystem:
    def __init__(self, coefficients, constants):
        self.coefficients = coefficients  # Matrix [[a, b], [d, e]]
        self.constants = constants  # Vector [c, f]
        self.validate()

    def validate(self):
        if len(self.coefficients) != 2 or any(len(row) != 2 for row in self.coefficients):
            raise ValueError("Coefficients must be a 2x2 matrix.")
        if len(self.constants) != 2:
            raise ValueError("Constants vector must have length 2.")

    def determinant(self):
        a, b = self.coefficients[0]
        d, e = self.coefficients[1]
        return a * e - b * d

    def has_unique_solution(self):
        return self.determinant() != 0

    def solve(self):
        if not self.has_unique_solution():
            raise ValueError("No unique solution exists for the given system.")
        a, b = self.coefficients[0]
        d, e = self.coefficients[1]
        c, f = self.constants
        denom = self.determinant()
        x = (c * e - b * f) / denom
        y = (a * f - c * d) / denom
        return Solution(x, y)


class Solution:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def formatted(self):
        return f"{self.x:.3f} {self.y:.3f}"


class EquationSystemParser:
    @staticmethod
    def parse_line(line: str) -> EquationSystem:
        tokens = line.strip().split()
        if len(tokens) != 6:
            raise ValueError("Each input line must contain exactly 6 numeric values.")
        a, b, c, d, e, f = map(float, tokens)
        coefficients = [[a, b], [d, e]]
        constants = [c, f]
        return EquationSystem(coefficients, constants)


class SimultaneousEquationSolver:
    def __init__(self):
        self.parser = EquationSystemParser()

    def process_input(self, input_stream):
        for line in input_stream:
            if line.strip() == "":
                continue
            eq_system = self.parser.parse_line(line)
            solution = eq_system.solve()
            yield solution.formatted()


if __name__ == "__main__":
    import sys
    solver = SimultaneousEquationSolver()
    for result in solver.process_input(sys.stdin):
        print(result)