class CubeInstallation:
    class Dimensions:
        def __init__(self, width: int, depth: int):
            self.width = width
            self.depth = depth

    class Heights:
        def __init__(self, front_view: 'list[int]', side_view: 'list[int]'):
            self.front = front_view
            self.side = side_view

        def validate(self, dims: 'CubeInstallation.Dimensions') -> None:
            if len(self.front) != dims.width or len(self.side) != dims.depth:
                raise ValueError("Front or side heights do not match the given dimensions")

    class InstallationGrid:
        def __init__(self, dims: 'CubeInstallation.Dimensions', heights: 'CubeInstallation.Heights'):
            self.dims = dims
            self.heights = heights
            self.grid = [[0] * dims.width for _ in range(dims.depth)]

        def compute_optimal_layout(self) -> None:
            # Fill each cell with the minimal height that meets both front and side constraints at this position
            for r in range(self.dims.depth):
                for c in range(self.dims.width):
                    # The max height is limited by front view column c and side view row r
                    self.grid[r][c] = min(self.heights.front[c], self.heights.side[r])

        def total_cubes(self) -> int:
            return sum(sum(row) for row in self.grid)

    class InputParser:
        @staticmethod
        def parse_dataset(lines: 'list[str]') -> tuple:
            w, d = map(int, lines[0].strip().split())
            if w == 0 and d == 0:
                return None
            front_heights = list(map(int, lines[1].strip().split()))
            side_heights = list(map(int, lines[2].strip().split()))
            return CubeInstallation.Dimensions(w, d), CubeInstallation.Heights(front_heights, side_heights)

    def __init__(self):
        self.datasets = []

    def add_dataset(self, dims: 'CubeInstallation.Dimensions', heights: 'CubeInstallation.Heights'):
        heights.validate(dims)
        self.datasets.append((dims, heights))

    def minimal_cubes_per_dataset(self) -> 'list[int]':
        results = []
        for dims, heights in self.datasets:
            grid = CubeInstallation.InstallationGrid(dims, heights)
            grid.compute_optimal_layout()
            results.append(grid.total_cubes())
        return results

def main():
    installation = CubeInstallation()
    import sys

    buffer = []
    lines_needed = 3
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        buffer.append(line)
        if len(buffer) == lines_needed:
            parsed = CubeInstallation.InputParser.parse_dataset(buffer)
            buffer.clear()
            if parsed is None:
                break
            dims, heights = parsed
            installation.add_dataset(dims, heights)

    results = installation.minimal_cubes_per_dataset()
    for r in results:
        print(r)

if __name__ == "__main__":
    main()