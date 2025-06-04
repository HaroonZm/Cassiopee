t = input()
b = input()

MOD = 1000000007
n = len(t)
m = len(b)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        if t[i-1] == b[j-1]:
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

print(dp[n][m] % MOD)