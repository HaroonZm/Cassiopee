from sys import stdin
from itertools import starmap

N, W = map(int, stdin.readline().split())
A = [tuple(map(int, line.split())) for line in [stdin.readline() for _ in range(N)]]
dp = [0] * (W + 1)

for value, weight in A:
    for j in range(W, weight - 1, -1):
        if (candidate := dp[j - weight] + value) > dp[j]:
            dp[j] = candidate

print(max(dp))