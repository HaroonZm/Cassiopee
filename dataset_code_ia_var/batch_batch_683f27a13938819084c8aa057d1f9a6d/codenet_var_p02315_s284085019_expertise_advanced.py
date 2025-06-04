from sys import stdin
from itertools import accumulate

n, w = map(int, stdin.readline().split())
items = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

dp = [-1] * (w + 1)
dp[0] = 0

for value, weight in items:
    for j in range(w, weight - 1, -1):
        if dp[j - weight] >= 0:
            dp[j] = max(dp[j], dp[j - weight] + value)

print(max(dp))