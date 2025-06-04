class ChocolateBar:
    def __init__(self, height: int, width: int, grid: list[str]):
        self.height = height
        self.width = width
        self.grid = grid
        self.horizontal_cuts = [False] * (self.height - 1)
        self.vertical_cuts = [False] * (self.width - 1)

    def can_cut_horizontally(self, row: int) -> bool:
        # A horizontal cut is possible iff all segments in the groove line are empty
        # groove line is between row and row+1; check all columns
        for col in range(self.width):
            if self.grid[row][col] == '#' and self.grid[row + 1][col] == '#':
                # if both cells above and below are chocolate, groove in between (cut) must exist
                continue
            if self.grid[row][col] == '#' or self.grid[row + 1][col] == '#':
                # if one side is chocolate and other is no chocolate, no groove possible
                return False
        return True

    def can_cut_vertically(self, col: int) -> bool:
        # A vertical cut is possible iff all segments in the groove line are empty
        # groove line is between col and col+1; check all rows
        for row in range(self.height):
            if self.grid[row][col] == '#' and self.grid[row][col + 1] == '#':
                # chocolate segments on both sides => groove possible
                continue
            if self.grid[row][col] == '#' or self.grid[row][col + 1] == '#':
                # one side chocolate, one side no chocolate => no groove
                return False
        return True

    def find_valid_cuts(self):
        # Find all possible horizontal cuts first
        for row in range(self.height - 1):
            # To cut here, all columns must have chocolate in both rows or both empty in groove
            can_cut = True
            for col in range(self.width):
                if self.grid[row][col] == '#' and self.grid[row + 1][col] == '#':
                    # groove line possible here
                    continue
                if self.grid[row][col] == '#' or self.grid[row + 1][col] == '#':
                    can_cut = False
                    break
            self.horizontal_cuts[row] = can_cut

        # Find all possible vertical cuts
        for col in range(self.width - 1):
            can_cut = True
            for row in range(self.height):
                if self.grid[row][col] == '#' and self.grid[row][col + 1] == '#':
                    # groove line possible here
                    continue
                if self.grid[row][col] == '#' or self.grid[row][col + 1] == '#':
                    can_cut = False
                    break
            self.vertical_cuts[col] = can_cut

    def count_pieces(self) -> int:
        self.find_valid_cuts()

        # Identify horizontal segments: grouping rows separated by horizontal cuts
        horizontal_segments = []
        start = 0
        for i in range(self.height - 1):
            if self.horizontal_cuts[i]:
                horizontal_segments.append((start, i))
                start = i + 1
        horizontal_segments.append((start, self.height - 1))

        # Identify vertical segments similarly
        vertical_segments = []
        start = 0
        for j in range(self.width - 1):
            if self.vertical_cuts[j]:
                vertical_segments.append((start, j))
                start = j + 1
        vertical_segments.append((start, self.width - 1))

        # Count pieces as number of rectangle blocks (horizontal segments * vertical segments)
        # But pieces must actually contain chocolate (some rectangles may be empty)
        count = 0
        for h_start, h_end in horizontal_segments:
            for v_start, v_end in vertical_segments:
                if self.contains_chocolate(h_start, h_end, v_start, v_end):
                    count += 1
        return count

    def contains_chocolate(self, row_start, row_end, col_start, col_end) -> bool:
        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if self.grid[r][c] == '#':
                    return True
        return False


class ChocolateBarFactory:
    @staticmethod
    def from_input(h: int, w: int, lines: list[str]) -> ChocolateBar:
        return ChocolateBar(h, w, lines)


class ChocolateBarSolver:
    def __init__(self):
        self.results = []

    def solve(self):
        while True:
            h, w = map(int, input().strip().split())
            if h == 0 and w == 0:
                break
            lines = [input().rstrip('\n') for _ in range(h)]
            bar = ChocolateBarFactory.from_input(h, w, lines)
            result = bar.count_pieces()
            self.results.append(result)

    def output(self):
        for r in self.results:
            print(r)


if __name__ == "__main__":
    solver = ChocolateBarSolver()
    solver.solve()
    solver.output()