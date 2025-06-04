from sys import stdin
from itertools import islice

N, W = map(int, stdin.readline().split())
items = [tuple(map(int, line.split())) for line in islice(stdin, N)]
v, w = zip(*[(0, 0)] + items)

dp = [0] * (W + 1)
for i in range(1, N + 1):
    wi, vi = w[i], v[i]
    ndp = dp[:]
    for j in range(1, W + 1):
        if wi <= j:
            ndp[j] = max(dp[j], ndp[j - wi] + vi, dp[j - wi] + vi)
    dp = ndp

print(dp[W])