from sys import stdin
from itertools import accumulate
import numpy as np

N, P = map(int, stdin.readline().split())
xs, ys = zip(*(map(int, stdin.readline().split()) for _ in range(N)))
xs = np.array(xs, dtype=np.int32)
ys = np.array(ys, dtype=np.int32)

memo = np.zeros((N+1, N+1), dtype=np.int32)
for start in range(N):
    preuse = 0
    for now in range(start+1, N+1):
        nx = max(0, xs[now-1] - preuse)
        preuse = max(0, ys[now-1] - nx)
        memo[start, now] = memo[start, now-1] + preuse

dp = np.full((N+1, N+1, N+1), int(1e9), dtype=np.int32)
dp[0, 0, 0] = 0

for now in range(N):
    for l in range(now+1):
        for score in range(N):
            # Take now
            ncost = dp[now, l, score] + memo[l, now+1] - memo[l, now]
            if ncost < dp[now+1, l, score+1]:
                dp[now+1, l, score+1] = ncost
            # Skip now
            if dp[now, l, score] < dp[now+1, now+1, score]:
                dp[now+1, now+1, score] = dp[now, l, score]

ans = max(score for l in range(N+1) for score in range(N+1) if dp[N, l, score] <= P)
print(ans)