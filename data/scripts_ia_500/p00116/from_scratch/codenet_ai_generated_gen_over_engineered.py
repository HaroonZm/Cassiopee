from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Iterator


class Grid(ABC):
    @abstractmethod
    def height(self) -> int:
        pass

    @abstractmethod
    def width(self) -> int:
        pass

    @abstractmethod
    def cell(self, row: int, col: int) -> str:
        pass

    @abstractmethod
    def to_binary_matrix(self) -> List[List[int]]:
        """Returns 1 if cell is free ('.'), 0 if marked ('*')."""
        pass


class CharGrid(Grid):
    def __init__(self, data: List[str]) -> None:
        self._data = data

    def height(self) -> int:
        return len(self._data)

    def width(self) -> int:
        if self._data:
            return len(self._data[0])
        return 0

    def cell(self, row: int, col: int) -> str:
        return self._data[row][col]

    def to_binary_matrix(self) -> List[List[int]]:
        return [[1 if ch == '.' else 0 for ch in row] for row in self._data]


class MaxRectangleSolver(ABC):
    @abstractmethod
    def solve(self, grid: Grid) -> int:
        pass


class LargestRectangleInHistogram:
    @staticmethod
    def max_area(heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                max_area = max(max_area, height * (i - left))
            stack.append(i)
        return max_area


class MaxRectangleInBinaryMatrixSolver(MaxRectangleSolver):
    def solve(self, grid: Grid) -> int:
        matrix = grid.to_binary_matrix()
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        height = [0] * grid.width()
        for row in matrix:
            for col, val in enumerate(row):
                height[col] = height[col] + 1 if val == 1 else 0
            area = LargestRectangleInHistogram.max_area(height)
            max_area = max(max_area, area)
        return max_area


class InputParser:
    def __init__(self, lines: Iterator[str]) -> None:
        self.lines = lines

    def __iter__(self) -> Iterator[Tuple[int, int, List[str]]]:
        for line in self.lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            H, W = map(int, parts)
            if H == 0 and W == 0:
                break
            grid_data = [next(self.lines).rstrip('\n') for _ in range(H)]
            yield H, W, grid_data


class MainProgram:
    def __init__(self, input_lines: Iterator[str]) -> None:
        self.parser = InputParser(input_lines)
        self.solver: MaxRectangleSolver = MaxRectangleInBinaryMatrixSolver()

    def run(self) -> None:
        for H, W, data in self.parser:
            grid = CharGrid(data)
            result = self.solver.solve(grid)
            print(result)


def main():
    import sys
    program = MainProgram(iter(sys.stdin))
    program.run()


if __name__ == "__main__":
    main()