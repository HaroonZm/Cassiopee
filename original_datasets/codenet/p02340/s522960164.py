import math
def comb(n, k):
    if n < 0 or k < 0 or n < k: return 0
    return math.factorial(n) // math.factorial(n-k) // math.factorial(k)

n,k = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [[0] * (n+1)] * (k+1)

dp[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        if j >= i: dp[i][j] = (dp[i-1][j] + dp[i][j-i])%MOD
        else: dp[i][j] = dp[i-1][j]

print(dp[k][n])