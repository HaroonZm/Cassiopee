from functools import reduce
from itertools import count, takewhile, accumulate
from operator import mul

n = int(input())

def identity(x): return x

def trivial_case(x): return x == 1

def breakable_prime_factors(num):
    z = 2
    while num > 1:
        exponent = 0
        while num % z == 0:
            num //= z
            exponent += 1
        if exponent:
            yield z, exponent
        z += 1
        if z > int(n ** 0.5) and num > 1:
            yield num, 1
            break

if trivial_case(n):
    print(0)
    exit()

factor_powers = dict(breakable_prime_factors(n))

def rounds_needed(e):
    return next(i for i, s in enumerate(accumulate(range(1, 100)), 1) if s > e)

ans = 0
for exp in factor_powers.values():
    ans += rounds_needed(exp) - 1

print(ans)