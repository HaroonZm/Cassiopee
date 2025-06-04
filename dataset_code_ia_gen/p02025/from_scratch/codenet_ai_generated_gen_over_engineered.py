from typing import List, Protocol, runtime_checkable, Tuple

@runtime_checkable
class PopulationMatrix(Protocol):
    def height(self) -> int: ...
    def width(self) -> int: ...
    def population_at(self, row: int, col: int) -> int: ...

class RectangularCityPopulation:
    def __init__(self, population_grid: List[List[int]]):
        self._population = population_grid
        self._h = len(population_grid)
        self._w = len(population_grid[0]) if self._h > 0 else 0

    def height(self) -> int:
        return self._h

    def width(self) -> int:
        return self._w

    def population_at(self, row: int, col: int) -> int:
        return self._population[row][col]

class RescueOperation:
    def __init__(self, city_population: PopulationMatrix):
        self.city_population = city_population
        self.prefix_sum = self._compute_prefix_sum()

    def _compute_prefix_sum(self) -> List[List[int]]:
        h, w = self.city_population.height(), self.city_population.width()
        ps = [[0]*(w+1) for _ in range(h+1)]
        for i in range(1, h+1):
            for j in range(1, w+1):
                ps[i][j] = (self.city_population.population_at(i-1, j-1)
                            + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1])
        return ps

    def population_in_subrectangle(self, top: int, left: int, bottom: int, right: int) -> int:
        # zero-indexed inputs, inclusive boundaries
        ps = self.prefix_sum
        return ps[bottom+1][right+1] - ps[top][right+1] - ps[bottom+1][left] + ps[top][left]

    def total_rescue_times(self) -> int:
        h, w = self.city_population.height(), self.city_population.width()
        total = 0
        # Precompute the count of rectangles that include each cell (i,j)
        # Number of rectangles that include cell (i,j):
        # (i+1) * (j+1) * (h - i) * (w - j)
        for i in range(h):
            upper_count = i + 1
            lower_count = h - i
            for j in range(w):
                left_count = j + 1
                right_count = w - j
                cell_population = self.city_population.population_at(i, j)
                rect_count = upper_count * left_count * lower_count * right_count
                total += cell_population * rect_count
        return total

class InputParser:
    def __init__(self):
        self.H = 0
        self.W = 0
        self.population_grid: List[List[int]] = []

    def parse(self) -> RectangularCityPopulation:
        self.H, self.W = map(int, input().split())
        self.population_grid = [list(map(int, input().split())) for _ in range(self.H)]
        return RectangularCityPopulation(self.population_grid)

class AngelReliefController:
    def __init__(self):
        self.parser = InputParser()

    def run(self) -> None:
        population = self.parser.parse()
        rescue_op = RescueOperation(population)
        print(rescue_op.total_rescue_times())

if __name__ == '__main__':
    controller = AngelReliefController()
    controller.run()