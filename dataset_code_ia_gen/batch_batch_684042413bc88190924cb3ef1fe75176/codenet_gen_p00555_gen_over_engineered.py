class RefreshmentAreaProblem:
    class Grid:
        def __init__(self, n: int, m: int, grid_map: list[str]):
            self.n = n
            self.m = m
            self.grid_map = grid_map

        def is_cell_free(self, row: int, col: int) -> bool:
            return self.grid_map[row][col] == '.'

        def segment_free(self, start_row: int, start_col: int, length: int, direction: 'Coordinates.Direction') -> bool:
            for k in range(length):
                if direction == Coordinates.Direction.HORIZONTAL:
                    if not self.is_cell_free(start_row, start_col + k):
                        return False
                else:
                    if not self.is_cell_free(start_row + k, start_col):
                        return False
            return True

    class Coordinates:
        from enum import Enum
        class Direction(Enum):
            HORIZONTAL = 0
            VERTICAL = 1

    def __init__(self, n: int, m: int, d: int, grid_map: list[str]):
        self.n = n
        self.m = m
        self.d = d
        self.grid = self.Grid(n, m, grid_map)

    def count_positions(self) -> int:
        count = 0
        # Count horizontal candidates
        for r in range(self.n):
            for c in range(self.m - self.d + 1):
                if self.grid.segment_free(r, c, self.d, self.Coordinates.Direction.HORIZONTAL):
                    count += 1
        # Count vertical candidates
        for c in range(self.m):
            for r in range(self.n - self.d + 1):
                if self.grid.segment_free(r, c, self.d, self.Coordinates.Direction.VERTICAL):
                    count += 1
        
        # Special case: if d == 1, count each free cell once (not in the problem constraints but general)
        # Here d >= 2 by problem statement, so no need to handle overlapped counting

        return count


def main():
    class InputProcessor:
        @staticmethod
        def parse_input():
            n, m, d = map(int, input().split())
            grid_map = [input() for _ in range(n)]
            return n, m, d, grid_map

    class OutputProcessor:
        @staticmethod
        def output_result(result: int):
            print(result)

    n, m, d, grid_map = InputProcessor.parse_input()
    problem = RefreshmentAreaProblem(n, m, d, grid_map)
    result = problem.count_positions()
    OutputProcessor.output_result(result)


if __name__ == "__main__":
    main()