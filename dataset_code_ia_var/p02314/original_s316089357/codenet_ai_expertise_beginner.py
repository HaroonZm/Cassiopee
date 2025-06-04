INF = 1000000000000000000
n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = []
for i in range(n + 1):
    dp.append(INF)
dp[0] = 0
for i in range(m):
    coin = c[i]
    for j in range(coin, n + 1):
        if dp[j - coin] + 1 < dp[j]:
            dp[j] = dp[j - coin] + 1
print(dp[n])