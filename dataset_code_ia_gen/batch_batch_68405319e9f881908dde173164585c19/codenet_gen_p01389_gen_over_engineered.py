class GridPosition:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def neighbors(self, max_row: int, max_col: int):
        if self.row + 1 < max_row:
            yield GridPosition(self.row + 1, self.col)
        if self.col + 1 < max_col:
            yield GridPosition(self.row, self.col + 1)

class CicadaGrid:
    def __init__(self, height: int, width: int, grid_data: list[str]):
        self.height = height
        self.width = width
        self.grid = [[int(ch) for ch in line] for line in grid_data]

    def cicadas_at(self, pos: GridPosition) -> int:
        return self.grid[pos.row][pos.col]

class PathCostCalculator:
    def __init__(self, cicada_grid: CicadaGrid):
        self.grid = cicada_grid
        self.dp = [[None for _ in range(self.grid.width)] for _ in range(self.grid.height)]

    def min_cicada_path_cost(self) -> int:
        # Start position (0,0) has no cicadas (by problem statement)
        self.dp[0][0] = 0
        for r in range(self.grid.height):
            for c in range(self.grid.width):
                pos = GridPosition(r, c)
                current_cost = self.dp[r][c]
                if current_cost is None:
                    continue
                for neighbor in pos.neighbors(self.grid.height, self.grid.width):
                    new_cost = current_cost + self.grid.cicadas_at(neighbor)
                    if self.dp[neighbor.row][neighbor.col] is None or self.dp[neighbor.row][neighbor.col] > new_cost:
                        self.dp[neighbor.row][neighbor.col] = new_cost
        # End position (H-1, W-1) also no cicadas by problem statement
        return self.dp[self.grid.height - 1][self.grid.width - 1]

class CicadaPathFinderFacade:
    def __init__(self, input_data: str):
        lines = input_data.strip().split('\n')
        h, w = map(int, lines[0].split())
        grid_lines = lines[1:]
        self.grid = CicadaGrid(h, w, grid_lines)
        self.calculator = PathCostCalculator(self.grid)

    def find_min_unpleasantness(self) -> int:
        return self.calculator.min_cicada_path_cost()

def main():
    import sys
    input_text = sys.stdin.read()
    facade = CicadaPathFinderFacade(input_text)
    print(facade.find_min_unpleasantness())

if __name__ == "__main__":
    main()