class PrimeCheckerInterface:
    def is_prime(self, number: int) -> bool:
        raise NotImplementedError()

class SieveOfEratosthenes(PrimeCheckerInterface):
    def __init__(self, limit: int):
        self.limit = limit
        self._sieve = [True] * (self.limit + 1)
        self._sieve[0] = False
        self._sieve[1] = False
        self._generate_sieve()

    def _generate_sieve(self):
        for i in range(2, int(self.limit**0.5) + 1):
            if self._sieve[i]:
                for j in range(i * i, self.limit + 1, i):
                    self._sieve[j] = False

    def is_prime(self, number: int) -> bool:
        if 0 <= number <= self.limit:
            return self._sieve[number]
        else:
            # fallback for numbers outside precomputed range
            if number < 2:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True

class PrimeFinder:
    def __init__(self, prime_checker: PrimeCheckerInterface):
        self.prime_checker = prime_checker

    def find_adjacent_primes(self, n: int) -> tuple[int, int]:
        lower_prime = self._find_lower_prime(n)
        higher_prime = self._find_higher_prime(n)
        return (lower_prime, higher_prime)

    def _find_lower_prime(self, n: int) -> int:
        for candidate in range(n - 1, 1, -1):
            if self.prime_checker.is_prime(candidate):
                return candidate
        # not expected to reach here for n>=3 per problem statement
        raise ValueError("No lower prime found")

    def _find_higher_prime(self, n: int) -> int:
        candidate = n + 1
        while True:
            if self.prime_checker.is_prime(candidate):
                return candidate
            candidate += 1

class InputOutputHandler:
    def __init__(self, prime_finder: PrimeFinder):
        self.prime_finder = prime_finder

    def process_inputs(self):
        import sys
        inputs = []
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            inputs.append(int(line))
            if len(inputs) >= 50:  # max 50 datasets as per problem
                break
        results = [self.prime_finder.find_adjacent_primes(n) for n in inputs]
        self._print_results(results)

    def _print_results(self, results: list[tuple[int, int]]):
        for lower, higher in results:
            print(f"{lower} {higher}")

def main():
    MAX_LIMIT = 100_000  # arbitrarily chosen upper bound to cover beyond 50,000 input max
    sieve = SieveOfEratosthenes(MAX_LIMIT)
    prime_finder = PrimeFinder(sieve)
    io_handler = InputOutputHandler(prime_finder)
    io_handler.process_inputs()

if __name__ == "__main__":
    main()