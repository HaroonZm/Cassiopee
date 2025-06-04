N, W = list(map(int, input().split()))
items = []
for _ in range(N):
    items.append(tuple(map(int, input().split())))
dp = [[-1] * (W + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0
for w in range(W + 1):
    dp[0][w] = 0
from itertools import product
for i, w in product(range(N), range(W + 1)):
    dp[i + 1][w] = dp[i][w]
    value, weight = items[i]
    if w - weight >= 0:
        dp[i + 1][w] = max(dp[i][w], dp[i][w - weight] + value)
print(dp[-1][-1])