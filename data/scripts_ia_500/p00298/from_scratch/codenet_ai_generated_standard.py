N=int(input())
c=[0]*N
w=[0]*N
for i in range(N):
    x,y=map(int,input().split())
    c[i],w[i]=x,y
dp=[float('inf')]*(N+1)
dp[0]=0
for i in range(N):
    total=w[i]
    max_c=c[i]
    dp[i+1]=min(dp[i]+1,dp[i+1])
    for j in range(i-1,-1,-1):
        total+=w[j]
        if c[j]<total:
            break
        dp[i+1]=min(dp[i+1],dp[j])
print(dp[N])