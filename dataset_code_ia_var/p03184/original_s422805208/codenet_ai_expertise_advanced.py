from sys import stdin
from operator import itemgetter
from functools import lru_cache
from itertools import accumulate

h, w, n = map(int, stdin.readline().split())
wall = sorted((tuple(map(int, stdin.readline().split())) for _ in range(n)), key=itemgetter(0,1))

mod = 10**9 + 7
lim = h + w + 10

fac = [1] * lim
finv = [1] * lim
inv = [1] * lim

for i in range(2, lim):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = inv[mod % i] * (mod - mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod

def nck(n, k):
    if 0 <= k <= n:
        return fac[n] * finv[k] % mod * finv[n - k] % mod
    return 0

dp = [0] * n

for i, (xi, yi) in enumerate(wall):
    ways = nck(xi + yi - 2, xi - 1)
    for j in range(i):
        xj, yj = wall[j]
        if xj <= xi and yj <= yi:
            ways = (ways - dp[j] * nck(xi - xj + yi - yj, xi - xj)) % mod
    dp[i] = ways

ans = sum(dp[i] * nck(h - wall[i][0] + w - wall[i][1], h - wall[i][0]) for i in range(n)) % mod

print((nck(h + w - 2, h - 1) - ans) % mod)