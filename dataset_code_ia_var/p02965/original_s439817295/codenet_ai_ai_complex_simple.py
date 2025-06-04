from functools import reduce
from operator import mul
from itertools import islice, count, chain
from collections import deque

MOD = 998244353
R = 2500100

def accumulate_mod(f, r, o):
    def generator():
        acc = 1
        yield acc
        for i in range(1, r):
            acc = (acc * i) % o
            yield acc
    return list(generator())

F = accumulate_mod([1], R, MOD)

inv = lambda x: pow(x, MOD-2, MOD)

def comb(n, k):
    try:
        return F[n] * inv(F[n-k]) * inv(F[k]) % MOD
    except IndexError:
        return 0

n, m = map(int, input().split())

def exotic_aggregate(n, m):
    base = (comb(n + 3*m - 1, n - 1) - n*comb(n + m - 2, n - 1)) % MOD
    if n <= m + 1:
        return base

    def skip_odd_triplets():
        for i in range(m + 1, min(3*m, n) + 1):
            q, r = divmod(3*m - i, 2)
            if r:
                continue
            yield i, q

    delta = sum((comb(n, i) * comb(q + n - 1, n - 1)) % MOD for i, q in skip_odd_triplets())
    return (base - delta) % MOD

def recursive_lazy_evaluation(n, m):
    return exotic_aggregate(n, m)

print(recursive_lazy_evaluation(n, m))