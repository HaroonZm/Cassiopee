class HexGrid:
    def __init__(self, width: int, height: int, grid_data: list[list[int]]):
        self.width = width
        self.height = height
        self.grid = grid_data
        self.visited = [[False]*width for _ in range(height)]
        # Directions differ based on row parity (odd/even), zero-based row indexing internally
        # For odd rows (y odd in problem, means zero-based y even)
        self.directions_odd = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1)]
        # For even rows (y even in problem, means zero-based y odd)
        self.directions_even = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1)]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, x: int, y: int) -> list[tuple[int,int]]:
        # y is zero-based row index
        if (y + 1) % 2 == 1:  # original input y is odd, zero-based y is y, so if odd row (1-based)
            directions = self.directions_odd
        else:
            directions = self.directions_even
        results = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny):
                results.append((nx, ny))
        return results


class IlluminationWallsCalculator:
    def __init__(self, hex_grid: HexGrid):
        self.hex_grid = hex_grid
        # For clarity and extension, we encapsulate BFS/exterior detection here
        self.exterior = [[False]*hex_grid.width for _ in range(hex_grid.height)]

    def mark_exterior(self):
        from collections import deque

        q = deque()

        # We start BFS from all cells on the grid edges that are empty (0),
        # because exterior space is considered outside the building clusters.
        for x in range(self.hex_grid.width):
            for y in [0, self.hex_grid.height - 1]:
                if self.hex_grid.grid[y][x] == 0 and not self.exterior[y][x]:
                    q.append((x, y))
                    self.exterior[y][x] = True
        for y in range(self.hex_grid.height):
            for x in [0, self.hex_grid.width - 1]:
                if self.hex_grid.grid[y][x] == 0 and not self.exterior[y][x]:
                    q.append((x, y))
                    self.exterior[y][x] = True

        while q:
            x, y = q.popleft()
            for nx, ny in self.hex_grid.neighbors(x, y):
                if not self.exterior[ny][nx] and self.hex_grid.grid[ny][nx] == 0:
                    self.exterior[ny][nx] = True
                    q.append((nx, ny))

    def calculate_illumination_length(self) -> int:
        self.mark_exterior()
        total_length = 0
        for y in range(self.hex_grid.height):
            for x in range(self.hex_grid.width):
                if self.hex_grid.grid[y][x] == 1:
                    # Check all neighbors. For neighbors that are exterior empty space,
                    # add 1 meter for that wall side.
                    for nx, ny in self.hex_grid.neighbors(x, y):
                        if self.hex_grid.grid[ny][nx] == 0 and self.exterior[ny][nx]:
                            total_length += 1
                    # Also if on edge, count those walls facing outside of grid as illuminated walls
                    # Because the building cell edge with no neighbor also counts
                    if y == 0:
                        # Check if top neighbors exist outside grid? Actually neighbors function only returns in bounds
                        # So here we just count edges that outside grid would be exterior
                        top_neighbors = self.top_edge_neighbors(x, y)
                        total_length += top_neighbors
                    if y == self.hex_grid.height - 1:
                        bottom_neighbors = self.bottom_edge_neighbors(x, y)
                        total_length += bottom_neighbors
                    if x == 0:
                        left_neighbors = self.left_edge_neighbors(x, y)
                        total_length += left_neighbors
                    if x == self.hex_grid.width - 1:
                        right_neighbors = self.right_edge_neighbors(x, y)
                        total_length += right_neighbors
        return total_length

    def top_edge_neighbors(self, x: int, y: int) -> int:
        # Since no neighbor above grid, those walls count.
        # The hexagon edges conceptually touching outside grid are counted.
        # Hexagon has six edges. We count those edges that have no neighbor because of edge.
        # But since neighbors function only returns inside grid cells, the missing neighbors are outside and exterior.
        count = 0
        # We consider all neighbors that would be "above"?
        # For simplicity, let's just count the missing neighbors that neighbor function would have returned but are off grid.
        # The problem does not consider diagonal "above" neighbors explicitly beyond rules, so treat no neighbor as exterior for these edges.
        # So, number of edges that are missing neighbors when neighbor would be out of grid.
        # But because we count neighbors only inside grid, missing neighbors = edges exposed to outside.
        # Instead of trying to count edges, we only consider edges to outside that don't have neighbor inside grid.
        # This is already covered by neighbors checks plus exterior marking, so no extra counting needed here.
        return 0

    def bottom_edge_neighbors(self, x: int, y: int) -> int:
        return 0

    def left_edge_neighbors(self, x: int, y: int) -> int:
        return 0

    def right_edge_neighbors(self, x: int, y: int) -> int:
        return 0


class IlluminationSolution:
    def __init__(self):
        self.hex_grid = None
        self.calculator = None

    def read_input(self):
        import sys
        W, H = map(int, sys.stdin.readline().split())
        grid_data = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
        self.hex_grid = HexGrid(W, H, grid_data)

    def execute(self):
        self.calculator = IlluminationWallsCalculator(self.hex_grid)
        result = self.calculator.calculate_illumination_length()
        print(result)


if __name__ == "__main__":
    IlluminationSolution().read_input()
    IlluminationSolution().execute()