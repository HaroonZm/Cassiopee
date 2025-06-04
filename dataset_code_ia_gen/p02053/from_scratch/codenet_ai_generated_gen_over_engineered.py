from typing import List, Tuple
from abc import ABC, abstractmethod
import sys

class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def distance_to(self, other: 'Position') -> int:
        return abs(self.row - other.row) + abs(self.col - other.col)

    def __repr__(self):
        return f"Position(row={self.row}, col={self.col})"

class CampusGrid(ABC):
    @abstractmethod
    def parse(self, inputs: List[str]):
        pass

    @abstractmethod
    def get_building_positions(self) -> List[Position]:
        pass

class HokkaidoCampusGrid(CampusGrid):
    def __init__(self):
        self.H = 0
        self.W = 0
        self.grid: List[str] = []
        self.buildings: List[Position] = []

    def parse(self, inputs: List[str]):
        # First line: sizes
        H_W_line = inputs[0].strip().split()
        assert len(H_W_line) == 2
        self.H, self.W = map(int, H_W_line)
        assert 2 <= self.H <= 10**3
        assert 2 <= self.W <= 10**3
        
        # Next H lines: grid
        self.grid = [inputs[i+1].strip() for i in range(self.H)]
        assert len(self.grid) == self.H
        for rowline in self.grid:
            assert len(rowline) == self.W

        # Extract building positions
        self.buildings.clear()
        for i in range(self.H):
            for j in range(self.W):
                if self.grid[i][j] == 'B':
                    # Positions are 1-indexed as per problem statement
                    self.buildings.append(Position(i+1, j+1))
        assert len(self.buildings) >= 2

    def get_building_positions(self) -> List[Position]:
        return self.buildings

class DistanceCalculator(ABC):
    @abstractmethod
    def max_distance(self, positions: List[Position]) -> int:
        pass

class ManhattanDistanceCalculator(DistanceCalculator):
    def max_distance(self, positions: List[Position]) -> int:
        # Sophisticated approach:
        # Use bounding box to find max manhattan distance with linear complexity
        # Because max |i - i'| + |j - j'| can be found among corner points of bounding rectangle

        if len(positions) < 2:
            return 0

        rows = [p.row for p in positions]
        cols = [p.col for p in positions]

        rmin = min(rows)
        rmax = max(rows)
        cmin = min(cols)
        cmax = max(cols)

        # The max manhattan distance between any two points in positions is at least
        # one of the distances between corners of the bounding rectangle, but only if all those corners are valid buildings.
        # Here buildings may not be at these corners.
        # So we check max over all pairs (p1, p2).
        # But since up to 10^6 pairs, need optimization.

        # A known trick:
        # Manhattan distance can be decomposed into maximum of
        # (r + c) differences and (r - c) differences.
        # So we store max and min of r+c and r-c and distance between these extremes.

        max_r_plus_c = max(p.row + p.col for p in positions)
        min_r_plus_c = min(p.row + p.col for p in positions)
        max_r_minus_c = max(p.row - p.col for p in positions)
        min_r_minus_c = min(p.row - p.col for p in positions)

        d1 = max_r_plus_c - min_r_plus_c
        d2 = max_r_minus_c - min_r_minus_c

        return max(d1, d2)

class CampusDistanceSolver:
    def __init__(self, parser: CampusGrid, distance_calc: DistanceCalculator):
        self.parser = parser
        self.distance_calc = distance_calc

    def solve(self, inputs: List[str]) -> int:
        self.parser.parse(inputs)
        building_positions = self.parser.get_building_positions()
        return self.distance_calc.max_distance(building_positions)

def main():
    inp = sys.stdin.read().strip().split('\n')
    solver = CampusDistanceSolver(HokkaidoCampusGrid(), ManhattanDistanceCalculator())
    answer = solver.solve(inp)
    print(answer)

if __name__ == '__main__':
    main()