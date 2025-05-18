N,P=map(int,input().split())
xs=[]
ys=[]
dp=[[[1e9 for i in range(N+1)] for j in range(N+1)] for k in range(N+1)]
memo=[[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    x,y=map(int,input().split())
    xs.append(x)
    ys.append(y)

for start in range(N):
    preuse=0
    for now in range(start,N+1):
        if(now==start):
            preuse=0
            memo[start][now]=0
        else:
            nx=max(0,xs[now-1]-preuse)
            preuse=max(0,ys[now-1]-nx)
            memo[start][now]=memo[start][now-1]+preuse

dp[0][0][0]=0
for now in range(N):
    for l in range(now+1):
        for score in range(N):
           dp[now+1][l][score+1]=min(dp[now+1][l][score+1],dp[now][l][score]+memo[l][now+1]-memo[l][now])
           dp[now+1][now+1][score]=min(dp[now+1][now+1][score],dp[now][l][score])

ans=0
for l in range(N+1):
    for score in range(N):
        if(dp[N][l][score]<=P):
            ans=max(ans,score)

print(ans)