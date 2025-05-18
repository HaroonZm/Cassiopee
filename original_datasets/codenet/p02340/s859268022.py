n, k = map(int, input().split())
MOD = pow(10,9)+7
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1,k+1):
    for j in range(n+1):
        if j-i >= 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % MOD
        else:
            dp[i][j] = dp[i-1][j]
print(dp[k][n])