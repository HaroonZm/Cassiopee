class EuclideanAlgorithmStep:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
        self.remainder = dividend % divisor

    def __str__(self):
        return f"{self.dividend} ÷ {self.divisor} の余りは {self.remainder}"


class EuclideanAlgorithm:
    def __init__(self, a, b):
        self.original_a = a
        self.original_b = b
        self.steps = []
        self.gcd = None

    def compute_gcd(self):
        x, y = self.original_a, self.original_b
        step_count = 0
        while y != 0:
            step = EuclideanAlgorithmStep(x, y)
            self.steps.append(step)
            x, y = y, step.remainder
            step_count += 1
        self.gcd = x
        return self.gcd, step_count

    def __str__(self):
        step_descriptions = "\n".join(f"Step {i+1}: {str(step)}" for i, step in enumerate(self.steps))
        return f"Computing GCD of {self.original_a} and {self.original_b}:\n{step_descriptions}\nResult GCD: {self.gcd}, Steps: {len(self.steps)}"


class GCDInputParser:
    def __init__(self, input_lines):
        self.input_lines = input_lines

    def parse(self):
        for line in self.input_lines:
            a, b = map(int, line.strip().split())
            if a == 0 and b == 0:
                break
            yield a, b


class GCDProcessor:
    def __init__(self, input_lines):
        self.parser = GCDInputParser(input_lines)

    def process(self):
        results = []
        for a, b in self.parser.parse():
            algorithm = EuclideanAlgorithm(a, b)
            gcd, steps = algorithm.compute_gcd()
            results.append((gcd, steps))
        return results


def main():
    import sys
    input_lines = sys.stdin.readlines()
    processor = GCDProcessor(input_lines)
    results = processor.process()
    for gcd, steps in results:
        print(gcd, steps)


if __name__ == "__main__":
    main()