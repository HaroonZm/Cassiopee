MOD=10**9+7
n,k=map(int,input().split())
dp=[[0]*(k+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        dp[i][j]=(dp[i-1][j-1]+dp[i-j][j])%MOD if i>=j else dp[i-1][j-1]
print(dp[n][k])