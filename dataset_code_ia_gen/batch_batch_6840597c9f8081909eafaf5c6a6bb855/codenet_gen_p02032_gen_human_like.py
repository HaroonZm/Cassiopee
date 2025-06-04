import sys
import math

def prime_factors(n):
    factors = {}
    # Check divisibility by 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # Check odd numbers
    f = 3
    max_f = int(math.isqrt(n)) + 1
    while f <= max_f and n > 1:
        while n % f == 0:
            factors[f] = factors.get(f, 0) + 1
            n //= f
            max_f = int(math.isqrt(n)) + 1
        f += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def main():
    N = int(sys.stdin.readline())
    pf = prime_factors(N)

    # Minimum number of declarations is always 1 for any N>1
    # because you can declare N's square-free cofactor (or the largest factor chosen smartly)
    # Actually from examples, minimum equals the number of distinct prime factors (at least 1)
    # But example shows min=2 for N=18=2*3^2 => distinct primes=2 -> min=2
    # Example N=99=3^2*11 => min=2
    # N=10000000019 prime => min=1

    min_decl = len(pf)

    # Maximum declarations: play game by declaring prime powers in increasing order of exponents
    # According to problem example, max = sum of exponents
    max_decl = sum(pf.values())

    print(min_decl, max_decl)

if __name__ == "__main__":
    main()