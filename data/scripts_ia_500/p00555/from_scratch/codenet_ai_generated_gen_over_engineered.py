class GridCell:
    def __init__(self, has_equipment: bool):
        self.has_equipment = has_equipment

    def is_available(self) -> bool:
        return not self.has_equipment


class GridRow:
    def __init__(self, cells: list[GridCell]):
        self.cells = cells

    def count_consecutive_segments(self, length: int) -> int:
        count = 0
        continuous = 0
        for cell in self.cells:
            if cell.is_available():
                continuous += 1
            else:
                continuous = 0
            if continuous >= length:
                count += 1
        return count


class RefreshmentAreaFinder:
    def __init__(self, grid: list[GridRow], N: int, M: int, D: int):
        self.grid = grid
        self.N = N
        self.M = M
        self.D = D

    def count_horizontal_spaces(self) -> int:
        total = 0
        for row in self.grid:
            total += row.count_consecutive_segments(self.D)
        return total

    def count_vertical_spaces(self) -> int:
        total = 0
        for col_idx in range(self.M):
            vertical_cells = [self.grid[row_idx].cells[col_idx] for row_idx in range(self.N)]
            col = GridRow(vertical_cells)
            total += col.count_consecutive_segments(self.D)
        return total

    def total_available_spaces(self) -> int:
        horizontal_count = self.count_horizontal_spaces()
        vertical_count = self.count_vertical_spaces()
        return horizontal_count + vertical_count


class InputParser:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.D = 0
        self.grid = []

    def parse_header(self, line: str):
        parts = line.strip().split()
        self.N, self.M, self.D = map(int, parts)

    def parse_grid_line(self, line: str) -> GridRow:
        cells = [GridCell(char == '#') for char in line.strip()]
        return GridRow(cells)

    def parse_all(self):
        import sys
        first_line = sys.stdin.readline()
        self.parse_header(first_line)
        self.grid = []
        for _ in range(self.N):
            line = sys.stdin.readline()
            row = self.parse_grid_line(line)
            self.grid.append(row)

    def get_data(self):
        return self.N, self.M, self.D, self.grid


def main():
    parser = InputParser()
    parser.parse_all()
    N, M, D, grid = parser.get_data()
    finder = RefreshmentAreaFinder(grid, N, M, D)
    result = finder.total_available_spaces()
    print(result)


if __name__ == '__main__':
    main()