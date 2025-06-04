class PrimeGenerator:
    def __init__(self, limit: int):
        self.limit = limit
        self._primes = []
        self._sieve = []

    def generate_primes(self):
        self._sieve = [True] * (self.limit + 1)
        self._sieve[0] = self._sieve[1] = False
        for num in range(2, self.limit + 1):
            if self._sieve[num]:
                self._primes.append(num)
                for multiple in range(num*num, self.limit + 1, num):
                    self._sieve[multiple] = False

    @property
    def primes(self):
        if not self._primes:
            self.generate_primes()
        return self._primes


class ConsecutivePrimeSumCounter:
    def __init__(self, primes: list):
        self.primes = primes
        self.prefix_sums = self._compute_prefix_sums()

    def _compute_prefix_sums(self):
        prefix = [0]
        for p in self.primes:
            prefix.append(prefix[-1] + p)
        return prefix

    def count_representations(self, n: int) -> int:
        count = 0
        length = len(self.primes)
        # Since the summation is prefix_sums[j] - prefix_sums[i] for i<j
        # We use two pointers i and j to find all segments equal to n
        left, right = 0, 1
        while left < length and right <= length:
            current_sum = self.prefix_sums[right] - self.prefix_sums[left]
            if current_sum == n:
                count += 1
                left += 1
                right += 1
            elif current_sum < n:
                right += 1
            else:
                left += 1
                if left == right:
                    right += 1
        return count


class ConsecutivePrimeSumApplication:
    def __init__(self, upper_limit=10_000):
        self.upper_limit = upper_limit
        self.prime_generator = PrimeGenerator(self.upper_limit)
        self.prime_generator.generate_primes()
        self.counter = ConsecutivePrimeSumCounter(self.prime_generator.primes)

    def process_numbers(self, numbers):
        results = []
        for n in numbers:
            if n == 0:
                break
            result = self.counter.count_representations(n)
            results.append(result)
        return results


def main():
    import sys

    app = ConsecutivePrimeSumApplication()
    inputs = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        inputs.append(n)
        if n == 0:
            break
    results = app.process_numbers(inputs)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()