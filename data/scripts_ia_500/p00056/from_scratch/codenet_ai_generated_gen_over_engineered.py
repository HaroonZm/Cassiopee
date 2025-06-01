class PrimeSieve:
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve = [True] * (self.limit + 1)
        self._sieve[0] = self._sieve[1] = False
        self._compute_sieve()

    def _compute_sieve(self):
        for i in range(2, int(self.limit ** 0.5) + 1):
            if self._sieve[i]:
                for j in range(i * i, self.limit + 1, i):
                    self._sieve[j] = False

    def is_prime(self, num: int) -> bool:
        if 0 <= num <= self.limit:
            return self._sieve[num]
        raise ValueError("Number out of sieve bounds")

    def primes(self):
        return (idx for idx, val in enumerate(self._sieve) if val)


class GoldbachCalculator:
    def __init__(self, max_n: int):
        self.max_n = max_n
        self.prime_sieve = PrimeSieve(self.max_n)
        self._memo = {}

    def count_prime_pairs(self, n: int) -> int:
        if n < 4 or n > self.max_n:
            return 0
        if n in self._memo:
            return self._memo[n]
        count = 0
        for p in self.prime_sieve.primes():
            if p > n // 2:
                break
            if self.prime_sieve.is_prime(n - p):
                count += 1
        self._memo[n] = count
        return count


class InputProcessor:
    def __init__(self, calculator: GoldbachCalculator):
        self.calculator = calculator

    def process(self):
        import sys
        for line in sys.stdin:
            n = line.strip()
            if not n.isdigit():
                continue
            n = int(n)
            if n == 0:
                break
            result = self.calculator.count_prime_pairs(n)
            print(result)


def main():
    MAX_N = 50000
    calculator = GoldbachCalculator(MAX_N)
    processor = InputProcessor(calculator)
    processor.process()


if __name__ == "__main__":
    main()