INF = 10 ** 18
n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(m):
    for j in range(c[i], n + 1):
        dp[j] = min(dp[j], dp[j - c[i]] + 1)

print(dp[n])