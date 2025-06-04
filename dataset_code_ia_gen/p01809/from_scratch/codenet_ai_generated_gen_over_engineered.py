class RationalRepresentationBaseFinder:
    def __init__(self, numerator: int, denominator: int):
        self.p = numerator
        self.q = denominator
        self._validate_input()

    def _validate_input(self):
        if not (0 < self.p < self.q):
            raise ValueError("Input must satisfy 0 < p < q")
        if not (2 <= self.q < 10**9):
            raise ValueError("Denominator must be less than 10^9 and at least 2")

    def _prime_factorization(self, n: int) -> dict:
        factors = {}
        candidate = 2
        while candidate * candidate <= n:
            while n % candidate == 0:
                factors[candidate] = factors.get(candidate, 0) + 1
                n //= candidate
            candidate += 1 if candidate == 2 else 2
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors

    def _remove_common_factors(self):
        # Simplify fraction by gcd
        from math import gcd
        g = gcd(self.p, self.q)
        self.p //= g
        self.q //= g

    def _get_min_base(self) -> int:
        self._remove_common_factors()
        denominator_factors = self._prime_factorization(self.q)
        # The base must contain all prime factors of q for finite representation
        # Thus minimal base = product of distinct prime factors in q
        minimal_base = 1
        for prime_factor in denominator_factors.keys():
            minimal_base *= prime_factor
        return minimal_base

    def find_min_base(self) -> int:
        return self._get_min_base()


def main():
    import sys
    p, q = map(int, sys.stdin.read().strip().split())
    finder = RationalRepresentationBaseFinder(p, q)
    print(finder.find_min_base())


if __name__ == "__main__":
    main()