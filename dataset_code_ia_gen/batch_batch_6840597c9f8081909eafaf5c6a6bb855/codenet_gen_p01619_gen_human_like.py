N, M = map(int, input().split())
MOD = 1000000

# dp[i][j] = nombre de chemins pour atteindre le point (i,j)
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N + 1):
    for j in range(M + 1):
        if i > 0:
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
        if j > 0:
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD

print(dp[N][M] % MOD)