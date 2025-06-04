class GridLoader:
    def __init__(self, row_count=12, col_count=12):
        self.row_count = row_count
        self.col_count = col_count

    def load_all(self):
        grids = []
        current_grid = []
        while True:
            try:
                line = input()
                if line == "":
                    if current_grid:
                        grids.append(Grid(current_grid))
                        current_grid = []
                else:
                    if len(line.strip()) == self.col_count:
                        current_grid.append(line.strip())
                    else:
                        # skip invalid line length lines
                        pass
            except EOFError:
                if current_grid:
                    grids.append(Grid(current_grid))
                break
        return grids


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0]) if lines else 0
        self.cells = [[c == '1' for c in line] for line in lines]

    def get_cell(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.cells[row][col]
        else:
            return False


class IslandCounter:
    def __init__(self, grid):
        self.grid = grid
        self.visited = [[False] * self.grid.width for _ in range(self.grid.height)]

    def count_islands(self):
        count = 0
        for row in range(self.grid.height):
            for col in range(self.grid.width):
                if self.should_visit(row, col):
                    self.dfs(row, col)
                    count += 1
        return count

    def should_visit(self, row, col):
        return self.grid.get_cell(row, col) and not self.visited[row][col]

    def dfs(self, row, col):
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if not (0 <= r < self.grid.height and 0 <= c < self.grid.width):
                continue
            if self.visited[r][c]:
                continue
            if not self.grid.get_cell(r, c):
                continue
            self.visited[r][c] = True
            neighbors = self.get_neighbors(r, c)
            stack.extend(neighbors)

    def get_neighbors(self, row, col):
        # Up, Down, Left, Right neighbors only (no diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.grid.height and 0 <= nc < self.grid.width:
                neighbors.append((nr, nc))
        return neighbors


def main():
    loader = GridLoader()
    grids = loader.load_all()
    for grid in grids:
        counter = IslandCounter(grid)
        print(counter.count_islands())


if __name__ == "__main__":
    main()