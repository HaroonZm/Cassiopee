class IntegralRectangle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        if not self.is_wide():
            raise ValueError(f"Rectangle height {height} must be less than width {width}")

    def is_wide(self) -> bool:
        return self.width > self.height

    def diagonal_length_sq(self) -> int:
        return self.height * self.height + self.width * self.width

    def __lt__(self, other: 'IntegralRectangle') -> bool:
        # Compare by diagonal length squared first
        dl_self = self.diagonal_length_sq()
        dl_other = other.diagonal_length_sq()
        if dl_self != dl_other:
            return dl_self < dl_other
        # If diagonals are equal, compare by height
        return self.height < other.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IntegralRectangle):
            return NotImplemented
        return self.height == other.height and self.width == other.width

    def __repr__(self):
        return f"IntegralRectangle(h={self.height}, w={self.width})"


class RectangleOrder:
    def __init__(self, max_dim: int = 150):
        # Cache all wide integral rectangles up to max_dim for quick lookup
        self.max_dim = max_dim
        self.all_rectangles = self._generate_all_wide_rectangles()
        self.sorted_rectangles = sorted(self.all_rectangles)
        # Use a dictionary for index lookup to improve efficiency
        self.rect_index_map = { (r.height, r.width): i for i,r in enumerate(self.sorted_rectangles) }

    def _generate_all_wide_rectangles(self) -> list:
        rectangles = []
        for h in range(1, self.max_dim + 1):
            for w in range(h + 1, self.max_dim + 1):
                rectangles.append(IntegralRectangle(h, w))
        return rectangles

    def next_rectangle(self, rect: IntegralRectangle) -> IntegralRectangle:
        # Get the index of rect in sorted list, then return the next rectangle in order
        idx = self.rect_index_map.get((rect.height, rect.width))
        if idx is None:
            # Safety check, but rectangle should always be in map
            raise ValueError("Rectangle not found in ordering")
        if idx + 1 == len(self.sorted_rectangles):
            raise ValueError("No larger rectangle available")
        return self.sorted_rectangles[idx + 1]


class ProblemSolver:
    def __init__(self):
        self.order = RectangleOrder()

    def parse_input_line(self, line: str) -> IntegralRectangle or None:
        h_str, w_str = line.strip().split()
        h, w = int(h_str), int(w_str)
        if h == 0 and w == 0:
            return None
        return IntegralRectangle(h, w)

    def solve_for_rect(self, rect: IntegralRectangle) -> IntegralRectangle:
        return self.order.next_rectangle(rect)

    def run(self):
        import sys
        input_lines = sys.stdin.read().strip().split('\n')
        results = []
        for line in input_lines:
            data = self.parse_input_line(line)
            if data is None:
                break
            next_rect = self.solve_for_rect(data)
            results.append(f"{next_rect.height} {next_rect.width}")
        print("\n".join(results))


if __name__ == "__main__":
    ProblemSolver().run()