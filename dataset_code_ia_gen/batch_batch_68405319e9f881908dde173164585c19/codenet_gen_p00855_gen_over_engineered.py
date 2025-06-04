from typing import List, Iterator, Optional
import bisect

class PrimeSieve:
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve: List[bool] = []
        self._primes: List[int] = []
        self._generate_sieve()

    def _generate_sieve(self):
        sieve = [True] * (self.limit + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(self.limit**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, self.limit + 1, i):
                    sieve[j] = False
        self._sieve = sieve
        self._primes = [i for i, prime in enumerate(sieve) if prime]

    def is_prime(self, n: int) -> bool:
        if n <= self.limit:
            return self._sieve[n]
        # Fallback for numbers greater than limit (not needed here)
        return False

    def primes(self) -> List[int]:
        return self._primes

    def nth_prime(self, n: int) -> int:
        # 1-based indexing
        return self._primes[n - 1]

class PrimeGap:
    def __init__(self, primes: List[int]):
        self.primes = primes
        self.start_map = {}  # Map start of gap composite to gap length and endpoints
        self.end_map = {}    # Map end of gap composite to gap length and endpoints
        self._build_gaps()

    def _build_gaps(self):
        for i in range(len(self.primes) - 1):
            p1 = self.primes[i]
            p2 = self.primes[i + 1]
            gap_length = p2 - p1
            if gap_length > 1:
                # composite numbers lying between p1 and p2 are from p1+1 to p2-1
                for composite_candidate in range(p1 + 1, p2):
                    self.start_map[composite_candidate] = gap_length
                    self.end_map[composite_candidate] = gap_length

    def gap_length_containing(self, num: int) -> int:
        # Returns length of prime gap that contains num or 0 if none
        return self.start_map.get(num, 0)

class PrimeGapContext:
    """Context to hold all abstractions and provide a single interface."""

    MAX_LIMIT = 1299709  # given upper bound in problem statement

    def __init__(self):
        self.sieve = PrimeSieve(PrimeGapContext.MAX_LIMIT)
        self.prime_gap = PrimeGap(self.sieve.primes())

    def query_gap_length(self, num: int) -> int:
        if num <= 1:
            return 0
        if self.sieve.is_prime(num):
            return 0
        # num composite, check prime gap length
        return self.prime_gap.gap_length_containing(num)

class InputProcessor:
    def __init__(self, context: PrimeGapContext):
        self.context = context

    def iter_input(self, inputs: Iterator[str]) -> Iterator[int]:
        for line in inputs:
            line = line.strip()
            if line == '0':
                break
            try:
                val = int(line)
                if val > 1:
                    yield val
            except ValueError:
                continue

    def process(self, inputs: Iterator[str]) -> Iterator[int]:
        for num in self.iter_input(inputs):
            yield self.context.query_gap_length(num)

def main():
    import sys
    context = PrimeGapContext()
    processor = InputProcessor(context)
    inputs = (line for line in sys.stdin)
    results = processor.process(inputs)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()