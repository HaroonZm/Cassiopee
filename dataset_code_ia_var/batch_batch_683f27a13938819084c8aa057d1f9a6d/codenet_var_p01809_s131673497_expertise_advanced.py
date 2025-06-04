from functools import reduce
from math import gcd, isqrt

def distinct_prime_factors(n):
    factors = set()
    for k in range(2, isqrt(n) + 1):
        while n % k == 0:
            factors.add(k)
            n //= k
    if n > 1:
        factors.add(n)
    return reduce(int.__mul__, factors, 1)

p, q = map(int, input().split())
q //= gcd(p, q)
print(distinct_prime_factors(q))