class CombinationSumSolver:
    def __init__(self, digits=None):
        self.digits = digits if digits is not None else list(range(10))
        self._cache = {}

    def count_combinations(self, n, s):
        """
        Count combinations of n distinct digits summing up to s.
        """
        return self._count(n, s, 0)

    def _count(self, n, s, start_index):
        # Use memoization to prevent redundant calculations
        key = (n, s, start_index)
        if key in self._cache:
            return self._cache[key]
        if n == 0:
            result = 1 if s == 0 else 0
            self._cache[key] = result
            return result
        if s < 0 or n > len(self.digits) - start_index:
            self._cache[key] = 0
            return 0
        count = 0
        # Choose digit at start_index or skip it
        for i in range(start_index, len(self.digits)):
            digit = self.digits[i]
            count += self._count(n - 1, s - digit, i + 1)
        self._cache[key] = count
        return count


class InputProcessor:
    def __init__(self, solver):
        self.solver = solver

    def process_input(self):
        while True:
            line = self.read_line()
            if line is None:
                break
            n, s = self.parse_line(line)
            if n == 0 and s == 0:
                break
            result = self.solver.count_combinations(n, s)
            self.output_result(result)

    @staticmethod
    def read_line():
        try:
            return input()
        except EOFError:
            return None

    @staticmethod
    def parse_line(line):
        parts = line.strip().split()
        return int(parts[0]), int(parts[1])

    @staticmethod
    def output_result(result):
        print(result)


class Application:
    def __init__(self):
        self.solver = CombinationSumSolver()
        self.processor = InputProcessor(self.solver)

    def run(self):
        self.processor.process_input()


if __name__ == "__main__":
    app = Application()
    app.run()