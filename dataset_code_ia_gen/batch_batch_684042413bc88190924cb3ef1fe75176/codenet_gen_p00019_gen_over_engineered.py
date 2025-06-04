class InputParser:
    def __init__(self, source):
        self.source = source

    def get_integer(self):
        line = self.source.readline()
        return int(line.strip())


class FactorialCalculator:
    def __init__(self, max_n=20):
        self.max_n = max_n
        self.memo = {0: 1, 1: 1}

    def factorial(self, n):
        if not (1 <= n <= self.max_n):
            raise ValueError(f"Input {n} out of bounds (1 to {self.max_n})")
        return self._factorial_recursive(n)

    def _factorial_recursive(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = n * self._factorial_recursive(n - 1)
        return self.memo[n]


class OutputHandler:
    def __init__(self, destination):
        self.destination = destination

    def print_result(self, result):
        self.destination.write(f"{result}\n")


class FactorialApp:
    def __init__(self, input_source, output_dest):
        self.parser = InputParser(input_source)
        self.calculator = FactorialCalculator()
        self.output = OutputHandler(output_dest)

    def run(self):
        n = self.parser.get_integer()
        fact = self.calculator.factorial(n)
        self.output.print_result(fact)


if __name__ == "__main__":
    import sys
    app = FactorialApp(sys.stdin, sys.stdout)
    app.run()