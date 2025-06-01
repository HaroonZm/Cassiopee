class PrimeProvider:
    def __init__(self):
        self._primes = []
        self._max_checked = 1

    def _is_prime(self, num):
        if num < 2:
            return False
        for p in self._primes:
            if p * p > num:
                break
            if num % p == 0:
                return False
        return True

    def extend_primes_to(self, n):
        while len(self._primes) < n:
            self._max_checked += 1
            if self._is_prime(self._max_checked):
                self._primes.append(self._max_checked)

    def get_nth_prime(self, n):
        self.extend_primes_to(n)
        return self._primes[n - 1]

    def sum_first_n_primes(self, n):
        self.extend_primes_to(n)
        return sum(self._primes[:n])


class InputHandler:
    def __init__(self):
        self._data = []

    def read_input(self):
        import sys
        for line in sys.stdin:
            val = line.strip()
            if val == '':
                continue
            num = int(val)
            if num == 0:
                break
            self._data.append(num)

    def get_datasets(self):
        return self._data


class OutputHandler:
    def __init__(self, prime_provider):
        self._prime_provider = prime_provider

    def output_sums(self, datasets):
        for n in datasets:
            s = self._prime_provider.sum_first_n_primes(n)
            print(s)


class PrimeSumApp:
    def __init__(self):
        self._input_handler = InputHandler()
        self._prime_provider = PrimeProvider()
        self._output_handler = OutputHandler(self._prime_provider)

    def run(self):
        self._input_handler.read_input()
        data = self._input_handler.get_datasets()
        self._output_handler.output_sums(data)


if __name__ == "__main__":
    app = PrimeSumApp()
    app.run()