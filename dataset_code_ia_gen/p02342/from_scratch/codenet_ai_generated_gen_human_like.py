MOD = 10**9 + 7

def stirling_second_kind(n, k):
    # S(n, k) = k * S(n-1, k) + S(n-1, k-1)
    # with S(0,0)=1, S(n,0)=0 for n>0, S(0,k)=0 for k>0
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            dp[i][j] = (j * dp[i-1][j] + dp[i-1][j-1]) % MOD
    return dp[n][k]

n, k = map(int, input().split())
print(stirling_second_kind(n, k))