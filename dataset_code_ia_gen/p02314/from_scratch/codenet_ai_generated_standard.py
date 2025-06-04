n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [float('inf')] * (n + 1)
dp[0] = 0
for coin in coins:
    for x in range(coin, n + 1):
        if dp[x - coin] + 1 < dp[x]:
            dp[x] = dp[x - coin] + 1
print(dp[n])