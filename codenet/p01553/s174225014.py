N=int(input())
dp=[[0]*(N+1) for i in range(N+1)]
dp[0][0]=1
MOD=10**9+7
for i in range(N):
    s=input()
    for j in range(i+1):
        if s=="-":
            nj=j
            dp[i+1][nj]+=dp[i][j]
            dp[i+1][nj]%=MOD
        elif s=="U":#実際には下がる
            nj=j+1
            dp[i+1][nj]+=dp[i][j]
            dp[i+1][nj]%=MOD

            nj=j
            x=j
            dp[i+1][nj]+=dp[i][j]*x
            dp[i+1][nj]%=MOD
        elif s=="D":#実際には上がる
            nj=j
            x=j
            dp[i+1][nj]+=dp[i][j]*x
            dp[i+1][nj]%=MOD

            if nj==0:
                continue
            nj=j-1
            x=j*j
            dp[i+1][nj]+=dp[i][j]*x
            dp[i+1][nj]%=MOD
print(dp[N][0])