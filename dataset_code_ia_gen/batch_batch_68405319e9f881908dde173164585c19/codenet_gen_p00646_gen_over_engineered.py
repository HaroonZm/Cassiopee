import sys
import math
from typing import Iterator, Tuple, Dict

class InputHandler:
    def __init__(self, source: Iterator[str]):
        self.source = source
    
    def __iter__(self) -> Iterator[int]:
        for line in self.source:
            value = int(line.strip())
            if value == 0:
                break
            yield value

class OutputHandler:
    def __init__(self):
        self.results = []
    
    def add_result(self, result: int):
        self.results.append(result)
    
    def flush(self):
        for res in self.results:
            print(res)

class PrimeSieve:
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve = self._build_sieve()
    
    def _build_sieve(self) -> list:
        sieve = [True] * (self.limit + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(self.limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i*i, self.limit + 1, i):
                    sieve[j] = False
        return sieve
    
    def get_primes(self) -> Iterator[int]:
        return (i for i, prime in enumerate(self._sieve) if prime)

class FactorizationEngine:
    def __init__(self, prime_limit: int = 10**6):
        self.prime_sieve = PrimeSieve(prime_limit)
        self.primes = list(self.prime_sieve.get_primes())
    
    def factorize(self, n: int) -> Dict[int, int]:
        factors = {}
        remaining = n
        for p in self.primes:
            if p * p > remaining:
                break
            count = 0
            while remaining % p == 0:
                remaining //= p
                count += 1
            if count > 0:
                factors[p] = count
        if remaining > 1:
            factors[remaining] = 1
        return factors

class PairCounter:
    def __init__(self, factorization_engine: FactorizationEngine):
        self.factorization_engine = factorization_engine
    
    def count_lcm_pairs(self, L: int) -> int:
        # Number of pairs (a,b) with a <= b and lcm(a,b) = L equals
        # product over primes of (2*exponent + 1) + 1 divided by 2
        factorization = self.factorization_engine.factorize(L)
        product = 1
        for exp in factorization.values():
            product *= (2 * exp + 1)
        return (product + 1) // 2

class Solver:
    def __init__(self, input_source: Iterator[str]):
        self.input_handler = InputHandler(input_source)
        self.output_handler = OutputHandler()
        self.factorization_engine = FactorizationEngine()
        self.pair_counter = PairCounter(self.factorization_engine)
    
    def run(self):
        for L in self.input_handler:
            result = self.pair_counter.count_lcm_pairs(L)
            self.output_handler.add_result(result)
        self.output_handler.flush()

if __name__ == "__main__":
    solver = Solver(sys.stdin)
    solver.run()