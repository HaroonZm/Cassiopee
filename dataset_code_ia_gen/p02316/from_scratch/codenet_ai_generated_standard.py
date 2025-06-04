N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (W + 1)
for v, w in items:
    for weight in range(w, W + 1):
        dp[weight] = max(dp[weight], dp[weight - w] + v)
print(dp[W])