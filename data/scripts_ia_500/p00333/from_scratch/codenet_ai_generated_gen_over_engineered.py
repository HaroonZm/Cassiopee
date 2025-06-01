class LandDimension:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def greatest_common_divisor(self) -> int:
        # Euclidean algorithm for GCD - ensures minimal square size
        a, b = self.width, self.height
        while b:
            a, b = b, a % b
        return a

class PlotCostCalculator:
    def __init__(self, land: LandDimension, cost_per_plot: int):
        self.land = land
        self.cost_per_plot = cost_per_plot

    def calculate_min_cost(self) -> int:
        square_size = self.land.greatest_common_divisor()
        number_of_plots = (self.land.width // square_size) * (self.land.height // square_size)
        return number_of_plots * self.cost_per_plot

class InputParser:
    @staticmethod
    def parse(input_line: str):
        parts = input_line.strip().split()
        if len(parts) != 3:
            raise ValueError("Input must consist of exactly three integers.")
        w, h, c = map(int, parts)
        if not (1 <= w <= 1000 and 1 <= h <= 1000 and 1 <= c <= 1000):
            raise ValueError("Input values out of allowed range.")
        return w, h, c

class NewTownPlanner:
    def __init__(self, raw_input: str):
        self.w, self.h, self.c = InputParser.parse(raw_input)
        self.land = LandDimension(self.w, self.h)
        self.calculator = PlotCostCalculator(self.land, self.c)

    def plan(self) -> int:
        return self.calculator.calculate_min_cost()

if __name__ == "__main__":
    import sys
    raw_input = sys.stdin.readline()
    planner = NewTownPlanner(raw_input)
    print(planner.plan())