MOD = 10**9 + 7
S = input()
n = len(S)

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
        dp[i][j] %= MOD

print(dp[0][n-1] % MOD)