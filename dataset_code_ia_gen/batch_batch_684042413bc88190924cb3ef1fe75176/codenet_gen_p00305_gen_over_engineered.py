class PixelGrid:
    def __init__(self, size: int, pixels: list[list[int]]):
        self.size = size
        self.grid = pixels
        self.prefix_sum = self._compute_prefix_sum()

    def _compute_prefix_sum(self) -> list[list[int]]:
        # Compute 2D prefix sums for O(1) sub-rectangle sum queries
        ps = [[0] * (self.size + 1) for _ in range(self.size + 1)]
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                ps[i][j] = (self.grid[i-1][j-1] + ps[i-1][j] +
                            ps[i][j-1] - ps[i-1][j-1])
        return ps

    def rectangle_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # r1,c1 and r2,c2 are 0-based inclusive indices
        # Use prefix sums to get sum in O(1)
        ps = self.prefix_sum
        return (ps[r2+1][c2+1] - ps[r1][c2+1] -
                ps[r2+1][c1] + ps[r1][c1])

class FrameExtractor:
    def __init__(self, pixel_grid: PixelGrid):
        self.grid = pixel_grid
        self.n = pixel_grid.size
        self.max_sum = None

    def _frame_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # Calculate the frame sum for rectangle (r1,c1)-(r2,c2)
        # Frame width 1 pixel (border only)
        if r2 < r1 or c2 < c1:
            return float('-inf')
        top = self.grid.rectangle_sum(r1, c1, r1, c2)
        bottom = self.grid.rectangle_sum(r2, c1, r2, c2) if r2 > r1 else 0
        left = self.grid.rectangle_sum(r1+1, c1, r2-1, c1) if r2 - r1 > 1 else 0
        right = self.grid.rectangle_sum(r1+1, c2, r2-1, c2) if (r2 - r1 > 1 and c2 > c1) else 0
        return top + bottom + left + right

    def find_max_frame_sum(self) -> int:
        max_sum = float('-inf')
        n = self.n
        # Enumerate all rectangles that can form a frame
        # Consider rectangles of size 1x1 up to NxN
        for r1 in range(n):
            for r2 in range(r1, n):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        # Valid frame must be at least 1 pixel wide and high
                        # According to problem, even 1x1 or 1x2 etc are frames
                        # So no lower bound other than r1<=r2 and c1<=c2
                        frame_val = self._frame_sum(r1, c1, r2, c2)
                        if frame_val > max_sum:
                            max_sum = frame_val
        self.max_sum = max_sum
        return max_sum

class InputReader:
    def __init__(self):
        self.n = 0
        self.pixels = []

    def read(self):
        self.n = int(input())
        self.pixels = [list(map(int, input().split())) for _ in range(self.n)]

class Solution:
    def __init__(self):
        self.reader = InputReader()

    def run(self):
        self.reader.read()
        pixel_grid = PixelGrid(self.reader.n, self.reader.pixels)
        extractor = FrameExtractor(pixel_grid)
        print(extractor.find_max_frame_sum())

if __name__ == "__main__":
    Solution().run()