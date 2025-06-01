INF=10**20
n,m=map(int,input().split())
dist=[int(input()) for _ in range(n)]
weth=[int(input()) for _ in range(m)]
dp=[INF]*(n+1)
dp[0]=0
for i in range(m):
    for j in range(n,0,-1):
        dp[j]=min(dp[j],dp[j-1]+dist[j-1]*weth[i])
print(dp[n])