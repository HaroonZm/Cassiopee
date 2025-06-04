class RectanglePatternMatcher:
    class Rectangle:
        def __init__(self, height, width, data):
            self.height = height
            self.width = width
            self.data = data  # 2D list

        def get_subrectangle(self, top, left, h, w):
            # extract subrectangle starting at (top,left) with height h and width w
            return [row[left:left + w] for row in self.data[top:top + h]]

    class IntegralImage:
        def __init__(self, matrix):
            self.H = len(matrix)
            self.W = len(matrix[0]) if self.H > 0 else 0
            self.integral = [[0] * (self.W + 1) for _ in range(self.H + 1)]
            for i in range(1, self.H + 1):
                row_sum = 0
                for j in range(1, self.W + 1):
                    row_sum += matrix[i - 1][j - 1]
                    self.integral[i][j] = self.integral[i - 1][j] + row_sum

        def query_sum(self, top, left, bottom, right):
            # sum of rectangle from (top,left) to (bottom,right), inclusive, 0-based indices
            return (self.integral[bottom + 1][right + 1] - self.integral[bottom + 1][left] -
                    self.integral[top][right + 1] + self.integral[top][left])

    class PatternMatcher:
        @staticmethod
        def match(big_rect, pattern_rect):
            """Return all top-left coordinates in big_rect where pattern_rect matches exactly."""
            matches = []
            for i in range(big_rect.height - pattern_rect.height + 1):
                for j in range(big_rect.width - pattern_rect.width + 1):
                    sub_b = big_rect.get_subrectangle(i, j, pattern_rect.height, pattern_rect.width)
                    if sub_b == pattern_rect.data:
                        matches.append((i, j))
            return matches

    def __init__(self, A, B, C):
        # A,B,C are instances of Rectangle
        self.A = A
        self.B = B
        self.C = C
        self.integralA = self.IntegralImage(self.A.data)

    def solve(self):
        # Find all matches of pattern C in B
        positions = self.PatternMatcher.match(self.B, self.C)

        if not positions:
            return "NA"

        max_score = None
        h, w = self.C.height, self.C.width
        for top, left in positions:
            score = self.integralA.query_sum(top, left, top + h - 1, left + w - 1)
            if max_score is None or score > max_score:
                max_score = score

        return max_score


class InputParser:
    @staticmethod
    def parse():
        H, W = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(H)]
        B = [list(map(int, input().split())) for _ in range(H)]
        h, w = map(int, input().split())
        C = [list(map(int, input().split())) for _ in range(h)]
        return H, W, A, B, h, w, C


def main():
    H, W, A_data, B_data, h, w, C_data = InputParser.parse()

    A = RectanglePatternMatcher.Rectangle(H, W, A_data)
    B = RectanglePatternMatcher.Rectangle(H, W, B_data)
    C = RectanglePatternMatcher.Rectangle(h, w, C_data)

    solver = RectanglePatternMatcher(A, B, C)
    result = solver.solve()
    print(result)


if __name__ == "__main__":
    main()