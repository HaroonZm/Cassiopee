class Tile:
    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol

    def is_black(self) -> bool:
        return self.symbol in {'.', '@'}

    def is_start(self) -> bool:
        return self.symbol == '@'


class Grid:
    def __init__(self, width: int, height: int, lines: list[str]):
        self.width = width
        self.height = height
        self.tiles = [[Tile(x, y, lines[y][x]) for x in range(width)] for y in range(height)]

    def get_tile(self, x: int, y: int) -> Tile:
        return self.tiles[y][x]

    def neighbors(self, tile: Tile) -> list[Tile]:
        candidates = [
            (tile.x - 1, tile.y),
            (tile.x + 1, tile.y),
            (tile.x, tile.y - 1),
            (tile.x, tile.y + 1)
        ]
        valid_neighbors = []
        for nx, ny in candidates:
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor_tile = self.get_tile(nx, ny)
                if neighbor_tile.is_black():
                    valid_neighbors.append(neighbor_tile)
        return valid_neighbors

    def find_start(self) -> Tile:
        for y in range(self.height):
            for x in range(self.width):
                tile = self.tiles[y][x]
                if tile.is_start():
                    return tile
        raise ValueError("No starting tile '@' found in grid.")


class ReachabilityAnalyzer:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.visited = set()

    def position_key(self, tile: Tile) -> tuple[int, int]:
        return (tile.x, tile.y)

    def dfs(self, tile: Tile) -> int:
        stack = [tile]
        count = 0
        while stack:
            current = stack.pop()
            pos = self.position_key(current)
            if pos not in self.visited:
                self.visited.add(pos)
                count += 1
                neighbors = self.grid.neighbors(current)
                for neighbor in neighbors:
                    if self.position_key(neighbor) not in self.visited:
                        stack.append(neighbor)
        return count


class InputReader:
    def __init__(self, input_lines: list[str]):
        self.lines = input_lines
        self.current_line = 0

    def has_next(self) -> bool:
        return self.current_line < len(self.lines)

    def next_line(self) -> str:
        line = self.lines[self.current_line]
        self.current_line += 1
        return line.strip()

    def read_dataset(self) -> tuple[int, int, list[str]] | None:
        while self.has_next():
            line = self.next_line()
            if not line:
                continue
            W, H = map(int, line.split())
            if W == 0 and H == 0:
                return None
            layout = [self.next_line() for _ in range(H)]
            return W, H, layout
        return None


class RedBlackSolver:
    def __init__(self, input_data: list[str]):
        self.input_reader = InputReader(input_data)

    def solve(self) -> list[int]:
        results = []
        while True:
            data = self.input_reader.read_dataset()
            if data is None:
                break
            W, H, layout = data
            grid = Grid(W, H, layout)
            start_tile = grid.find_start()
            analyzer = ReachabilityAnalyzer(grid)
            count = analyzer.dfs(start_tile)
            results.append(count)
        return results


def main():
    import sys
    input_data = [line.rstrip('\n') for line in sys.stdin]
    solver = RedBlackSolver(input_data)
    results = solver.solve()
    for res in results:
        print(res)


if __name__ == "__main__":
    main()