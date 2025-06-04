import sys
import math

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 2
    if n > 1:
        factors.add(n)
    return factors

def key_number(n):
    factors = prime_factors(n)
    max_factor = max(factors)
    total_others = sum(factors) - max_factor
    return max_factor - total_others

for line in sys.stdin:
    a,b = map(int,line.split())
    if a == 0 and b == 0:
        break
    print('a' if key_number(a) > key_number(b) else 'b')