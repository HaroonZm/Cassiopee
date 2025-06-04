class FlagColor:
    WHITE = 'W'
    BLUE = 'B'
    RED = 'R'


class FlagRow:
    def __init__(self, colors: str):
        self.colors = colors
        self.length = len(colors)

    def repaint_cost(self, target_color: str) -> int:
        return sum(1 for c in self.colors if c != target_color)


class Flag:
    def __init__(self, rows: list[FlagRow]):
        self.rows = rows
        self.N = len(rows)
        self.M = rows[0].length if self.N > 0 else 0

    def min_repainting_to_russian_flag(self) -> int:
        # We have to partition rows into three contiguous segments:
        # top rows painted WHITE (1 or more rows)
        # middle rows painted BLUE (1 or more rows)
        # bottom rows painted RED (1 or more rows)
        # Find indices white_end and blue_end with 1 ≤ white_end < blue_end < N
        # white rows: [0, white_end-1], blue rows: [white_end, blue_end-1], red rows: [blue_end, N-1]
        min_cost = float('inf')
        # Precompute repaint costs per row per color
        cost_by_color = {FlagColor.WHITE: [], FlagColor.BLUE: [], FlagColor.RED: []}
        for row in self.rows:
            for color in cost_by_color.keys():
                cost_by_color[color].append(row.repaint_cost(color))

        for white_end in range(1, self.N - 1):
            for blue_end in range(white_end + 1, self.N):
                cost_white = sum(cost_by_color[FlagColor.WHITE][:white_end])
                cost_blue = sum(cost_by_color[FlagColor.BLUE][white_end:blue_end])
                cost_red = sum(cost_by_color[FlagColor.RED][blue_end:])
                total_cost = cost_white + cost_blue + cost_red
                if total_cost < min_cost:
                    min_cost = total_cost
        return min_cost


class InputParser:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.raw_rows = []

    def parse(self):
        first_line = input().strip()
        self.N, self.M = map(int, first_line.split())
        for _ in range(self.N):
            self.raw_rows.append(input().strip())

    def to_flag(self) -> Flag:
        rows = [FlagRow(colors) for colors in self.raw_rows]
        return Flag(rows)


def main():
    parser = InputParser()
    parser.parse()
    flag = parser.to_flag()
    print(flag.min_repainting_to_russian_flag())


if __name__ == '__main__':
    main()