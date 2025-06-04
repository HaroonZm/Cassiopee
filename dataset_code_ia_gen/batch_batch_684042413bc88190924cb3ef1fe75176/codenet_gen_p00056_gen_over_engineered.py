class PrimeGenerator:
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve = None
        self._primes = None
        self._generate_primes()
        
    def _generate_primes(self):
        sieve = [True] * (self.limit + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(self.limit**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, self.limit + 1, i):
                    sieve[j] = False
        self._sieve = sieve
        self._primes = [i for i, prime in enumerate(sieve) if prime]
    
    def is_prime(self, num: int) -> bool:
        if 0 <= num <= self.limit:
            return self._sieve[num]
        # For numbers out of precalculated range: fallback (not expected here)
        if num < 2:
            return False
        for prime in self._primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                return False
        return True
    
    @property
    def primes(self):
        return self._primes


class GoldbachSolver:
    def __init__(self, max_limit: int = 50000):
        self.max_limit = max_limit
        self.prime_generator = PrimeGenerator(self.max_limit)
    
    def count_prime_sum_pairs(self, n: int) -> int:
        if n < 4:
            return 0
        count = 0
        primes = self.prime_generator.primes
        sieve = self.prime_generator._sieve
        # To avoid double counting, iterate up to n//2
        for prime in primes:
            if prime > n // 2:
                break
            complement = n - prime
            if sieve[complement]:
                count += 1
        return count


class InputOutputHandler:
    def __init__(self):
        self.solver = GoldbachSolver()
        
    def process_input(self):
        import sys
        for line in sys.stdin:
            n = line.strip()
            if not n.isdigit():
                continue
            n = int(n)
            if n == 0:
                break
            print(self.solver.count_prime_sum_pairs(n))


if __name__ == "__main__":
    io_handler = InputOutputHandler()
    io_handler.process_input()