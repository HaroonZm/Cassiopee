class RemainderTracker:
    def __init__(self):
        self.position_map = {}

    def seen(self, remainder):
        return remainder in self.position_map

    def add(self, remainder, position):
        self.position_map[remainder] = position

    def get_position(self, remainder):
        return self.position_map[remainder]


class DecimalExpansion:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.quotient_integer = numerator // denominator
        self.remainder = numerator % denominator
        self.decimal_digits = []
        self.remainder_tracker = RemainderTracker()

    def expand(self):
        pos = 0
        while True:
            self.remainder *= 10
            digit = self.remainder // self.denominator
            self.decimal_digits.append(str(digit))
            self.remainder %= self.denominator

            if self.remainder == 0:
                # Terminating decimal
                return self.decimal_digits, None

            if self.remainder_tracker.seen(self.remainder):
                # Repetition found
                repeat_start = self.remainder_tracker.get_position(self.remainder)
                return self.decimal_digits, repeat_start

            self.remainder_tracker.add(self.remainder, pos)
            pos += 1


class RecurringDecimalFormatter:
    def __init__(self, digits, repeat_start):
        self.digits = digits
        self.repeat_start = repeat_start

    def format(self):
        if self.repeat_start is None:
            # No repetition, just print digits as a single line string
            return ["".join(self.digits)]
        else:
            # two lines output
            before = "".join(self.digits[:self.repeat_start])
            recurring = "".join(self.digits[self.repeat_start:])
            line1 = before + recurring
            # line 2: spaces for before, then ^ for recurring length
            line2 = " " * len(before) + "^" * len(recurring)
            return [line1, line2]


class InputProcessor:
    def __init__(self):
        self.datasets = []

    def read(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            p, q = line.split()
            p, q = int(p), int(q)
            # Validate constraints per problem statement
            if 0 < p < q < 10**6:
                self.datasets.append((p, q))

    def get_datasets(self):
        return self.datasets


class DecimalDivisionSolver:
    def __init__(self):
        self.input_processor = InputProcessor()

    def run(self):
        self.input_processor.read()
        for p, q in self.input_processor.get_datasets():
            expansion = DecimalExpansion(p, q)
            digits, repeat_start = expansion.expand()
            formatter = RecurringDecimalFormatter(digits, repeat_start)
            output_lines = formatter.format()
            for line in output_lines:
                print(line)


if __name__ == "__main__":
    solver = DecimalDivisionSolver()
    solver.run()