import sys
import math
from collections import deque
import copy

MOD = 10 ** 9 + 7
H, W = map(int, input().split())

a = [["#" for _ in range(W + 2)]]
for i in range(H):
    p = deque(list(input()))
    p.appendleft("#")
    p.append("#")
    a.append(list(p))
a.append(["#" for _ in range(W + 2)])

dp = [[0 for _ in range(W + 10)] for _ in range(H + 10)]
dp[0][1] = 1
for i in range(1, H + 1):
    for l in range(1, W + 1):
        if a[i][l] != "#":
            dp[i][l] = (dp[i][l - 1] + dp[i - 1][l]) % MOD
print(dp[H][W] % MOD)