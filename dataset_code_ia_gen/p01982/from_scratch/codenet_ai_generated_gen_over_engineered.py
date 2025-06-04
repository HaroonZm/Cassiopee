class GeneralizedLeapYear:
    def __init__(self, divisors):
        self.divisors = divisors
        self.n = len(divisors)

    def is_leap_year(self, year):
        # Find the smallest i such that year % A_i == 0
        for i, d in enumerate(self.divisors, start=1):
            if year % d == 0:
                # If i is odd, leap year; else not
                return i % 2 == 1
        # If no divisor found
        return self.n % 2 == 0

    def count_leap_years(self, l, r):
        # Counts how many years in [l, r] are generalized leap years
        count = 0
        for year in range(l, r + 1):
            if self.is_leap_year(year):
                count += 1
        return count


class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        while True:
            line = input().strip()
            if line == '0 0 0':
                break
            n, l, r = map(int, line.split())
            divisors = [int(input().strip()) for _ in range(n)]
            self.datasets.append((n, l, r, divisors))
        return self.datasets


class OutputHandler:
    @staticmethod
    def print_results(results):
        for res in results:
            print(res)


class Solver:
    def __init__(self):
        self.parser = InputParser()
        self.output_handler = OutputHandler()

    def solve(self):
        datasets = self.parser.parse()
        results = []

        for n, l, r, divisors in datasets:
            gl = GeneralizedLeapYear(divisors)
            count = gl.count_leap_years(l, r)
            results.append(count)

        self.output_handler.print_results(results)


if __name__ == '__main__':
    Solver().solve()