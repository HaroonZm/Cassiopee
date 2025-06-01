INF = 10**20
n, m = map(int, input().split())
dist = list(map(int, (input() for _ in range(n))))
weth = list(map(int, (input() for _ in range(m))))
dp = [0] + [INF] * n
for w in weth:
    for j in range(n, 0, -1):
        dp[j] = min(dp[j], dp[j - 1] + dist[j - 1] * w)
print(dp[n])