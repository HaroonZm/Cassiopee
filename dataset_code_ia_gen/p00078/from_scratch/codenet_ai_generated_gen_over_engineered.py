class MagicSquareFactory:
    def __init__(self, n: int):
        self.n = n
        self.square = [[0] * n for _ in range(n)]

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n

    def left_down(self, row: int, col: int):
        # Move one down and one left, wrapping around
        new_row = (row + 1) % self.n
        new_col = (col - 1) % self.n
        return new_row, new_col

    def right_down(self, row: int, col: int):
        # Move one down and one right, wrapping around per problem spec:
        new_row = row + 1
        new_col = col + 1
        if new_col == self.n:
            new_col = 0
        if new_row == self.n:
            new_row = 0
        return new_row, new_col

    def iterate_positions(self):
        # Iterator for all positions for extensibility
        for r in range(self.n):
            for c in range(self.n):
                yield r, c

    def generate(self):
        # Place 1 at central cell in middle row +1 (1 below center)
        center_col = self.n // 2
        # According to problem: 1 is placed "just below the center cell"
        current_row = self.n // 2 + 1
        if current_row == self.n:
            current_row = 0
        current_col = center_col
        self.square[current_row][current_col] = 1

        for num in range(2, self.n * self.n + 1):
            # Proposed next cell: right down diagonal by 1 cell
            next_row, next_col = self.right_down(current_row, current_col)

            # Check if occupied, if yes place left down from current pos
            if self.square[next_row][next_col] != 0:
                next_row, next_col = self.left_down(current_row, current_col)

            self.square[next_row][next_col] = num
            current_row, current_col = next_row, next_col
        return self.square

class MagicSquarePrinter:
    def __init__(self, square):
        self.square = square

    def format_row(self, row):
        # Format numbers right aligned, 4 width decimal
        return " ".join(f"{num:>4d}" for num in row)

    def print(self):
        lines = [self.format_row(row) for row in self.square]
        return "\n".join(lines)

class MagicSquareProcessor:
    def __init__(self):
        self.results = []

    @staticmethod
    def validate_n(n: int):
        if not (3 <= n <= 15):
            raise ValueError("n must be between 3 and 15 inclusive")
        if n % 2 == 0:
            raise ValueError("n must be odd")

    def process(self, ns):
        for n in ns:
            if n == 0:
                break
            self.validate_n(n)
            factory = MagicSquareFactory(n)
            square = factory.generate()
            self.results.append(square)

    def output(self):
        return "\n\n".join(MagicSquarePrinter(square).print() for square in self.results)

def main():
    import sys
    inputs = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        inputs.append(int(line))
        if int(line) == 0:
            break
    processor = MagicSquareProcessor()
    processor.process(inputs)
    print(processor.output())

if __name__ == "__main__":
    main()