MOD = 10**9 + 7
import sys
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())

# dp[i][j]: number of ways to partition i distinct balls into j indistinguishable boxes
# This equals the Stirling number of the second kind S(i,j)
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(1, min(i,k)+1):
        dp[i][j] = (j*dp[i-1][j] + dp[i-1][j-1]) % MOD

print(dp[n][k])