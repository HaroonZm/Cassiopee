from math import gcd, isqrt
from functools import reduce

def prime_factors(n):
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
    if n > 1:
        yield n

def main():
    a, b = map(int, input().split())
    b //= gcd(a, b)
    factors = set(prime_factors(b))
    print(functools.reduce(int.__mul__, factors, 1) if b > 1 else 1)

import functools
main()