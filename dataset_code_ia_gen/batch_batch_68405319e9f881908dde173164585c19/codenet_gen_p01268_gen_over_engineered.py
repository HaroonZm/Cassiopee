import sys
import bisect
from abc import ABC, abstractmethod
from typing import List, Iterator, Tuple


class PrimeGenerator(ABC):
    """
    Abstract base class for generating primes greater than a lower bound.
    Potentially extendable strategy patterns for prime generation.
    """
    @abstractmethod
    def primes_above(self, lower_bound: int) -> Iterator[int]:
        pass


class SievePrimeGenerator(PrimeGenerator):
    """
    Generates primes above a certain value using a segmented sieve.
    """
    def __init__(self, upper_limit: int = 200000):
        self.upper_limit = upper_limit
        self._sieve = None
        self._primes = []
        self._generate_sieve()

    def _generate_sieve(self):
        limit = self.upper_limit
        sieve = [True] * (limit + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        self._sieve = sieve
        self._primes = [i for i in range(limit + 1) if sieve[i]]

    def primes_above(self, lower_bound: int) -> Iterator[int]:
        idx = bisect.bisect_right(self._primes, lower_bound)
        for prime in self._primes[idx:]:
            yield prime


class MatsuzakiNumberCalculator:
    """
    Core calculator of Matsuzaki numbers.
    Decomposes the problem with a strategy to compute the P-th sum
    of two primes both greater than N.
    """
    def __init__(self, prime_generator: PrimeGenerator):
        self.prime_gen = prime_generator

    def _collect_primes_above(self, N: int) -> List[int]:
        # Collect primes > N
        return list(self.prime_gen.primes_above(N))

    def calculate_matsuzaki_number(self, N: int, P: int) -> int:
        primes = self._collect_primes_above(N)
        # Since P ≤ 100, no need to consider too many sums, just enough pairs.
        # We can limit pairs candidates to the first around 200 primes for safety
        # to cover counts of sums ≥ 100
        limited_primes = primes[:200]

        # Generate all sums p1 + p2 with p1 <= p2 (to avoid duplicates)
        # but counts duplicates if multiple decompositions exist.
        # As the problem states, repetitions count multiple times.

        # We will collect sums in a list, sorted after generation.
        sums = []
        for i, p1 in enumerate(limited_primes):
            for p2 in limited_primes[i:]:
                sums.append(p1 + p2)

        sums.sort()

        # P-th element is sums[P-1]
        return sums[P - 1]


class MatsuzakiIOProcessor:
    """
    Handles I/O processing and orchestrates calculation.
    """
    def __init__(self, calculator: MatsuzakiNumberCalculator):
        self.calc = calculator

    def process_input(self):
        for line in sys.stdin:
            line = line.strip()
            if line == '':
                continue
            N_str, P_str = line.split()
            N, P = int(N_str), int(P_str)
            if N == -1 and P == -1:
                break
            result = self.calc.calculate_matsuzaki_number(N, P)
            print(result)


def main():
    prime_generator = SievePrimeGenerator(upper_limit=200000)
    calculator = MatsuzakiNumberCalculator(prime_generator)
    processor = MatsuzakiIOProcessor(calculator)
    processor.process_input()


if __name__ == "__main__":
    main()