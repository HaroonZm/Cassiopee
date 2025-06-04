from functools import reduce
from itertools import count, takewhile, chain, groupby, accumulate, product

def eratosthenes(n):
    A = [True] * (n + 1)
    A[0:2] = [False, False]
    [A.__setitem__(j, False) for i in range(2, n+1) if A[i] for j in range(i*i, n+1, i)]
    return tuple(i for i, b in enumerate(A) if b)

Ps = eratosthenes(1000)

def divisor(n):
    return next((p for p in Ps if p*p <= n and n%p==0), -1 if all(p*p > n or n%p!=0 for p in Ps) else None)

def prime_division(n):
    d = {}
    x = n
    while x > 1:
        p = divisor(x)
        if p == -1:
            d[x] = d.get(x, 0) + 1
            break
        d[p] = d.get(p, 0) + 1
        x //= p
    return d

from collections import Counter

N = int(input())
all_primes = (prime_division(i+1) for i in range(1, N))
d = dict()
for c in (dct.items() for p in all_primes for dct in [p]):
    for k,v in c:
        d[k] = d.get(k, 0) + v

r = reduce(lambda x, y: x*y % 1000000007, (v+1 for v in d.values()), 1)
print(r)