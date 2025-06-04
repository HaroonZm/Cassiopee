from math import gcd
from functools import reduce

class ElectronFlyParameters:
    def __init__(self, a1: int, m1: int, a2: int, m2: int, a3: int, m3: int):
        self.a1 = a1
        self.m1 = m1
        self.a2 = a2
        self.m2 = m2
        self.a3 = a3
        self.m3 = m3
        self._validate()

    def _validate(self):
        if not (1 < self.a1 < 2**15 and 1 < self.m1 < 2**15 and
                1 < self.a2 < 2**15 and 1 < self.m2 < 2**15 and
                1 < self.a3 < 2**15 and 1 < self.m3 < 2**15):
            raise ValueError("Parameters out of bounds")
        if gcd(self.a1, self.m1) != 1 or gcd(self.a2, self.m2) != 1 or gcd(self.a3, self.m3) != 1:
            # The problem states these being coprime guarantees return
            pass

class ModularCycleFinder:
    def __init__(self, a: int, m: int):
        assert gcd(a, m) == 1, "a and m must be coprime"
        self.a = a
        self.m = m

    def cycle_length(self) -> int:
        """
        Finds the smallest positive integer k such that a^k ≡ 1 (mod m)
        This is the multiplicative order of a modulo m.
        """
        # Since a and m are coprime, multiplicative order exists.
        # We can use a method to find multiplicative order:
        # Order divides Euler's totient function φ(m)
        phi = self._euler_totient(self.m)
        # Find divisors of phi to test them in ascending order
        for d in self._divisors(phi):
            if pow(self.a, d, self.m) == 1:
                return d
        # Fallback (should not happen for coprime)
        return phi

    def _euler_totient(self, n: int) -> int:
        result = n
        p = 2
        temp = n
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                result -= result // p
            p += 1 if p == 2 else 2
        if temp > 1:
            result -= result // temp
        return result

    def _divisors(self, n: int):
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
            i += 1
        divs.sort()
        return divs

class ElectronFlyCycleController:
    def __init__(self, params: ElectronFlyParameters):
        self.params = params
        self.cycle_finders = [
            ModularCycleFinder(params.a1, params.m1),
            ModularCycleFinder(params.a2, params.m2),
            ModularCycleFinder(params.a3, params.m3),
        ]

    def compute_minimum_return_time(self) -> int:
        # Calculate order for each coordinate transition
        orders = [finder.cycle_length() for finder in self.cycle_finders]
        # The fly returns to (1, 1, 1) when all three coordinates simultaneously return to 1
        # The overall cycle length is the lcm of these orders
        return self._lcm_multiple(orders)

    def _lcm(self, x: int, y: int) -> int:
        return x * y // gcd(x, y)

    def _lcm_multiple(self, values):
        return reduce(self._lcm, values, 1)

class InputProcessor:
    def __init__(self):
        self.data_sets = []

    def read_input(self):
        while True:
            line = input().strip()
            if line == '':
                continue
            parts = list(map(int, line.split()))
            if len(parts) != 6:
                # Ignore malformed input (should not happen)
                continue
            if parts == [0, 0, 0, 0, 0, 0]:
                break
            self.data_sets.append(parts)

    def get_data_sets(self):
        for data in self.data_sets:
            yield ElectronFlyParameters(*data)

class OutputPresenter:
    def __init__(self):
        self.results = []

    def collect(self, result: int):
        self.results.append(result)

    def display(self):
        for result in self.results:
            print(result)

def main():
    processor = InputProcessor()
    processor.read_input()
    presenter = OutputPresenter()
    for params in processor.get_data_sets():
        controller = ElectronFlyCycleController(params)
        result = controller.compute_minimum_return_time()
        presenter.collect(result)
    presenter.display()

if __name__ == "__main__":
    main()