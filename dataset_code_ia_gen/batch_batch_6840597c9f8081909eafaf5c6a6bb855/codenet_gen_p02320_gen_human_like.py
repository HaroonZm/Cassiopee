N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)

for v, w, m in items:
    k = 1
    while m > 0:
        use = min(k, m)
        weight = w * use
        value = v * use
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
        m -= use
        k <<= 1

print(dp[W])