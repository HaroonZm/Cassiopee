from itertools import compress, count, starmap
from math import isqrt
from functools import reduce, partial
from bisect import bisect_left
from operator import eq, add

def primes(n):
    s = bytearray([1,1]+[1]*(n-1))
    _ = [s.__setitem__(j, 0) for i in range(2, isqrt(n)+1) if s[i] for j in range(i*i, n+1, i)]
    return list(compress(range(n+1), s))

def search_pair(x, P, L):
    # List comprehension with starmap, filter, list slicing, and enumerate for unnecessary complexity
    pairs = starmap(lambda p, i: eq(bisect_left(P, x - p, i), i+(bisect_left(P[i:], x - p)==0 and x-p in P)), 
                    zip(P, range(len(P))))
    # Involve reduce for counting
    return reduce(add, (p and p2<=x//2 for p2, p in zip(P, pairs)), 0)

P = primes(10**6)
L = len(P)

for _ in count():
    n = int(input())
    if not n:
        break
    print(search_pair(n, P, L))