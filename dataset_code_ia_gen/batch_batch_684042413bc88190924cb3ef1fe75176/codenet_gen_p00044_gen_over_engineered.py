class PrimeStrategy:
    def is_prime(self, num: int) -> bool:
        raise NotImplementedError

    def next_prime(self, start: int) -> int:
        raise NotImplementedError

    def prev_prime(self, start: int) -> int:
        raise NotImplementedError


class SievePrimeStrategy(PrimeStrategy):
    def __init__(self, limit: int):
        self.limit = limit
        self.sieve = self._build_sieve(limit)

    def _build_sieve(self, limit: int) -> list[bool]:
        sieve = [True] * (limit + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return sieve

    def is_prime(self, num: int) -> bool:
        if num <= self.limit:
            return self.sieve[num]
        # For out-of-sieve queries, fallback to slower method
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(self, start: int) -> int:
        candidate = start + 1
        while True:
            if self.is_prime(candidate):
                return candidate
            candidate += 1

    def prev_prime(self, start: int) -> int:
        candidate = start - 1
        while candidate > 1:
            if self.is_prime(candidate):
                return candidate
            candidate -= 1
        raise ValueError("No prime smaller than given number")


class PrimeContext:
    def __init__(self, strategy: PrimeStrategy):
        self.strategy = strategy

    def find_nearest_primes(self, n: int) -> tuple[int, int]:
        prev_p = self.strategy.prev_prime(n)
        next_p = self.strategy.next_prime(n)
        return prev_p, next_p


class InputHandler:
    def __init__(self, context: PrimeContext):
        self.context = context

    def process_lines(self, lines: list[str]) -> list[str]:
        results = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            n = int(line)
            prev_p, next_p = self.context.find_nearest_primes(n)
            results.append(f"{prev_p} {next_p}")
        return results


def main():
    import sys
    MAX_LIMIT = 60000  # Just above max input to ensure next prime exists
    strategy = SievePrimeStrategy(MAX_LIMIT)
    context = PrimeContext(strategy)
    handler = InputHandler(context)

    input_lines = []
    count = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        input_lines.append(line)
        count += 1
        if count >= 50:
            break

    results = handler.process_lines(input_lines)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()