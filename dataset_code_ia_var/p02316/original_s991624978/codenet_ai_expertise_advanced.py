from sys import stdin
from itertools import islice

n, m = map(int, stdin.readline().split())
dp = [0] * (m + 1)

items = (tuple(map(int, line.split())) for line in islice(stdin, n))
for v, w in items:
    for i in range(w, m + 1):
        nv = dp[i - w] + v
        if nv > dp[i]:
            dp[i] = nv

print(dp[m])