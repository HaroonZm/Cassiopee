class VerticalLine:
    def __init__(self, position: int, label: int):
        self.position = position
        self.label = label

    def __repr__(self):
        return f"VerticalLine(pos={self.position}, label={self.label})"

class HorizontalLine:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"HorizontalLine({self.a},{self.b})"


class Amidakuji:
    def __init__(self, w: int):
        self.w = w
        self.vertical_lines = [VerticalLine(i + 1, i + 1) for i in range(w)]
        self.horizontal_lines = []

    def add_horizontal_line(self, a: int, b: int):
        # Validate input
        if a < 1 or b < 1 or a > self.w or b > self.w or a == b:
            raise ValueError(f"Invalid horizontal line endpoints: {a},{b}")
        self.horizontal_lines.append(HorizontalLine(a, b))

    def perform_swap(self, a: int, b: int):
        # Find VerticalLine instances at positions a and b
        va = None
        vb = None
        for v in self.vertical_lines:
            if v.position == a:
                va = v
            if v.position == b:
                vb = v
        # Swap their labels (simulate horizontal swap jumps)
        if va is not None and vb is not None:
            va.label, vb.label = vb.label, va.label

    def execute(self):
        # Sort horizontal lines by their input order (assuming given in order)
        # Applying each horizontal line's swap of labels between lines at a and b
        for hline in self.horizontal_lines:
            self.perform_swap(hline.a, hline.b)

    def get_results(self):
        # Output the label under each vertical line by ascending position (left to right)
        # Sorted by position since vertical_lines could be unordered
        sorted_lines = sorted(self.vertical_lines, key=lambda v: v.position)
        return [v.label for v in sorted_lines]

class AmidakujiFactory:
    @staticmethod
    def create_from_input(input_data: str):
        lines = input_data.strip().split('\n')
        w = int(lines[0])
        n = int(lines[1])
        amidakuji = Amidakuji(w)
        for i in range(n):
            a_str, b_str = lines[2 + i].strip().split(',')
            amidakuji.add_horizontal_line(int(a_str), int(b_str))
        return amidakuji

class AmidakujiSolver:
    def __init__(self, amidakuji: Amidakuji):
        self.amidakuji = amidakuji

    def solve(self):
        self.amidakuji.execute()
        return self.amidakuji.get_results()

def main():
    import sys
    input_data = sys.stdin.read()
    amidakuji = AmidakujiFactory.create_from_input(input_data)
    solver = AmidakujiSolver(amidakuji)
    result = solver.solve()
    for r in result:
        print(r)

if __name__ == "__main__":
    main()