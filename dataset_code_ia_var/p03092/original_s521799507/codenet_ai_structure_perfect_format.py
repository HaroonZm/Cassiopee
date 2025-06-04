import sys
input = sys.stdin.readline

import numpy as np

N, A, B = map(int, input().split())
P = [int(x) for x in input().split()]

INF = 10 ** 18
dp = np.full(N + 1, INF, dtype=np.int64)
dp[0] = 0

for p in P:
    dp[p] = dp[:p].min()
    dp[p + 1:] += B
    dp[:p] += A

answer = dp.min()
print(answer)