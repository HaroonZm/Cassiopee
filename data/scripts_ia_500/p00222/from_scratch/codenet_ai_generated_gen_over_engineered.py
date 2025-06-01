import sys
import bisect
from typing import List, Optional, Iterator

class PrimeSieve:
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve = self._create_sieve()
        self.primes = self._extract_primes()

    def _create_sieve(self) -> List[bool]:
        sieve = [True] * (self.limit + 1)
        sieve[0], sieve[1] = False, False
        for current in range(2, int(self.limit ** 0.5) + 1):
            if sieve[current]:
                for multiple in range(current * current, self.limit + 1, current):
                    sieve[multiple] = False
        return sieve

    def _extract_primes(self) -> List[int]:
        return [num for num, is_prime in enumerate(self._sieve) if is_prime]

    def is_prime(self, num: int) -> bool:
        if num <= self.limit:
            return self._sieve[num]
        # For extensibility, we could implement a fallback primality test here
        return False

class QuadrupleTwinPrimeFinder:
    def __init__(self, upper_bound: int):
        self.upper_bound = upper_bound
        self.sieve = PrimeSieve(upper_bound)
        self.quadruple_max_primes = self._precompute_quadruple_primes()

    def _precompute_quadruple_primes(self) -> List[int]:
        """
        Precompute the largest prime in each quadruple twin prime up to upper_bound.
        Return a sorted list of these maximum primes.
        """
        stores = []
        # Because the quadruple is (a, a+2, a+6, a+8), max is a+8 <= upper_bound
        max_start = self.upper_bound - 8
        for a in range(2, max_start + 1):
            if (self.sieve.is_prime(a) and
                self.sieve.is_prime(a + 2) and
                self.sieve.is_prime(a + 6) and
                self.sieve.is_prime(a + 8)):
                stores.append(a + 8)
        return sorted(stores)

    def max_quadruple_size_leq(self, n: int) -> Optional[int]:
        """
        Returns the maximum quadruple twin prime size <= n.
        If no quadruple twin primes exist <= n, returns None.
        """
        idx = bisect.bisect_right(self.quadruple_max_primes, n)
        if idx == 0:
            return None
        return self.quadruple_max_primes[idx - 1]

class InputProcessor:
    def __init__(self, finder: QuadrupleTwinPrimeFinder):
        self.finder = finder

    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            n_str = line.strip()
            if n_str == '0':
                break
            n = int(n_str)
            max_size = self.finder.max_quadruple_size_leq(n)
            # According to problem constraints, there's always at least one quadruple prime <= n if n >= 13
            # but just in case, we'll output max_size or a fallback
            yield str(max_size if max_size is not None else 0)

def main():
    # We consider the maximum n in the input is up to 10,000,000 as per problem statement.
    max_input_limit = 10_000_000
    finder = QuadrupleTwinPrimeFinder(max_input_limit)
    processor = InputProcessor(finder)
    output_lines = processor.process(sys.stdin)
    print('\n'.join(output_lines))

if __name__ == '__main__':
    main()