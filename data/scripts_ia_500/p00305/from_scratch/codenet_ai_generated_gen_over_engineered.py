class PixelMatrix:
    def __init__(self, n: int, pixels: list[list[int]]):
        self.n = n
        self.pixels = pixels
        self.prefix_sum = self._compute_prefix_sum()

    def _compute_prefix_sum(self) -> list[list[int]]:
        ps = [[0]*(self.n+1) for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                ps[i][j] = (self.pixels[i-1][j-1]
                            + ps[i-1][j]
                            + ps[i][j-1]
                            - ps[i-1][j-1])
        return ps

    def rectangle_sum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # Sum of pixels in rectangle corners (r1,c1) to (r2,c2), 1-indexed inclusive
        return (self.prefix_sum[r2][c2]
                - self.prefix_sum[r1-1][c2]
                - self.prefix_sum[r2][c1-1]
                + self.prefix_sum[r1-1][c1-1])

class FrameExtractor:
    def __init__(self, pixel_matrix: PixelMatrix):
        self.pixel_matrix = pixel_matrix
        self.n = pixel_matrix.n

    def extract_max_frame_sum(self) -> int:
        max_sum = float('-inf')
        # We treat frames as rectangles with at least width and height >= 1
        # Frame thickness is 1 pixel
        # For each possible top-left (r1,c1) and bottom-right (r2,c2)
        # Compute frame sum: sum of outer perimeter pixels
        
        pm = self.pixel_matrix

        for r1 in range(1, self.n+1):
            for c1 in range(1, self.n+1):
                for r2 in range(r1, self.n+1):
                    for c2 in range(c1, self.n+1):
                        height = r2 - r1 + 1
                        width = c2 - c1 + 1
                        if height <= 0 or width <= 0:
                            continue

                        # Sum of outer frame:
                        # Top row + bottom row + left column + right column
                        # minus 4 corners counted twice

                        # sum of rectangle
                        total = pm.rectangle_sum(r1, c1, r2, c2)

                        # inner rectangle (frame hollow part) to subtract
                        if height > 2 and width > 2:
                            inner_sum = pm.rectangle_sum(r1+1, c1+1, r2-1, c2-1)
                        else:
                            inner_sum = 0

                        frame_sum = total - inner_sum
                        if frame_sum > max_sum:
                            max_sum = frame_sum
        return max_sum

class InputParser:
    @staticmethod
    def parse() -> PixelMatrix:
        import sys
        input = sys.stdin.readline
        N_line = ''
        while N_line.strip() == '':
            N_line = input()
        N = int(N_line.strip())
        pixels = []
        count = 0
        while count < N:
            line = ''
            while line.strip() == '':
                line = input()
            row = list(map(int, line.strip().split()))
            if len(row) != N:
                # Read again until enough pixels in a row
                while len(row) < N:
                    extra_line = input()
                    row.extend(map(int, extra_line.strip().split()))
            pixels.append(row[:N])
            count += 1
        return PixelMatrix(N, pixels)

class Solution:
    def __init__(self):
        self.pixel_matrix = None

    def run(self):
        self.pixel_matrix = InputParser.parse()
        extractor = FrameExtractor(self.pixel_matrix)
        answer = extractor.extract_max_frame_sum()
        print(answer)

if __name__ == "__main__":
    Solution().run()