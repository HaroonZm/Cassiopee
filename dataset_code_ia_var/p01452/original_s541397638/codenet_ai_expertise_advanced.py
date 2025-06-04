import sys
import math
import functools

sys.setrecursionlimit(1 << 25)
inf = float('inf')
eps = 1e-13
mod = 10**9 + 7

dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

@functools.lru_cache(maxsize=None)
def inv(x):
    return pow(x, mod - 2, mod)

# Precompute factorials and their modular inverses.
@functools.lru_cache(maxsize=None)
def fact(n):
    if n == 0: return 1
    return n * fact(n-1) % mod

@functools.lru_cache(maxsize=None)
def inv_fact(n):
    return inv(fact(n))

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact(n) * inv_fact(k) % mod * inv_fact(n - k) % mod

def main():
    rr = []

    def f(n, m, k):
        res = 0
        for i in range(k + 1):
            j = k - i
            mt = comb(n + m + k * 2, n + i * 2)
            lk = (comb(n + i * 2, i) - comb(n + i * 2, i - 1)) % mod if i > 0 else 1
            rk = (comb(m + j * 2, j) - comb(m + j * 2, j - 1)) % mod if j > 0 else 1
            res = (res + mt * lk % mod * rk % mod) % mod
        return res

    while True:
        n, m, k = LI()
        if n == 0:
            break
        rr.append(f(n, m, k))
        break

    return '\n'.join(map(str, rr))

print(main())