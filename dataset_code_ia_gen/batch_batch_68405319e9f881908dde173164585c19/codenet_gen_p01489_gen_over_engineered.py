class Modulo:
    def __init__(self, modulus: int):
        self.modulus = modulus

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.modulus

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.modulus

    def pow(self, base: int, exponent: int) -> int:
        result = 1
        base %= self.modulus
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % self.modulus
            base = (base * base) % self.modulus
            exponent >>= 1
        return result


class IkaSequence:
    def __init__(self, modulo: Modulo):
        self.modulo = modulo

    def _fib(self, n: int) -> int:
        # Fast doubling method for Fibonacci
        def fib_fast_doubling(k: int):
            if k == 0:
                return (0, 1)
            a, b = fib_fast_doubling(k >> 1)
            c = self.modulo.mul(a, self.modulo.mul(2, b) - a + self.modulo.modulus)
            d = self.modulo.mul(a, a) + self.modulo.mul(b, b)
            d %= self.modulo.modulus
            if k & 1:
                return (d, (c + d) % self.modulo.modulus)
            else:
                return (c, d)
        return fib_fast_doubling(n)[0]

    def ika_number_by_index(self, k: int) -> int:
        """
        Returns the k-th smallest Ika number modulo the modulus.
        Sequence of Ika numbers corresponds to all numbers
        of form F(x) * F(z - x) for 0 < x < z where F is Fibonacci,
        but sequence given in problem is sorted set {1,2,3,5,8,13,...} including all products,
        which reduces to Fibonacci numbers and their products; problem only matches Fib numbers.

        The enumeration of possible Ika numbers equals all Fibonacci numbers >= 1 ordered.

        The k-th smallest Ika number = Fib(k+1) because:
        Ika numbers are exactly Fib(n) for n >= 2.

        The problem is reduced to:
        Output Fib(K+1) mod 1,000,000,007
        """
        return self._fib(k + 1) % self.modulo.modulus


def main():
    import sys

    MOD = 10**9 + 7
    modulo = Modulo(MOD)
    ika_seq = IkaSequence(modulo)

    K = int(sys.stdin.readline().strip())
    print(ika_seq.ika_number_by_index(K))


if __name__ == "__main__":
    main()