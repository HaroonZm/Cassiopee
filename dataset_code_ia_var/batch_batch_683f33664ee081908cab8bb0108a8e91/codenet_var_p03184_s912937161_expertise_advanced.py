import sys
from functools import lru_cache
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)

readline = sys.stdin.readline
int1 = lambda x: int(x) - 1

def MI(): return map(int, readline().split())
def MI1(): return map(int1, readline().split())
def LI(): return list(map(int, readline().split()))
def LI1(): return list(map(int1, readline().split()))

md = 10 ** 9 + 7
n_max = 2 * 10**5 + 10
fac = [1] * (n_max)
inv = [1] * (n_max)
for i in range(1, n_max):
    fac[i] = fac[i - 1] * i % md
inv[-1] = pow(fac[-1], md - 2, md)
for i in reversed(range(1, n_max)):
    inv[i - 1] = inv[i] * i % md

def com(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return fac[n] * inv[r] % md * inv[n - r] % md

def way(h, w):
    return com(h + w, h) if h >= 0 and w >= 0 else 0

def main():
    h, w, n = MI()
    rc = [LI1() for _ in range(n)]
    rc.sort(key=lambda x: x[0] + x[1])
    dp = [0] * n
    for i, (r, c) in enumerate(rc):
        dp[i] = (way(r, c) - sum(
            v * way(r - pr, c - pc) % md
            for v, (pr, pc) in zip(dp[:i], rc[:i])
        )) % md
    h, w = h - 1, w - 1
    ans = (way(h, w) - sum(
        v * way(h - r, w - c) % md
        for v, (r, c) in zip(dp, rc)
    )) % md
    print(ans)

main()