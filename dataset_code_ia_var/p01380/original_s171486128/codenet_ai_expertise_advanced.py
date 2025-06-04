from sys import stdin
from itertools import accumulate

N = int(stdin.readline())
tasks = sorted(tuple(map(int, line.split()))[::-1] for line in stdin.read().splitlines())

INF = float('inf')
dp = [0] + [INF] * N

for b, a in tasks:
    for i in range(N, 0, -1):
        if dp[i-1] + a <= b:
            dp[i] = min(dp[i], dp[i-1] + a)

print(max(i for i, t in enumerate(dp) if t < INF))