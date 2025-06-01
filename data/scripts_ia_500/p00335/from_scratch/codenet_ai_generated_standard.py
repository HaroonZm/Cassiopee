N=int(input())
p=list(map(int,input().split()))
dp=[float('inf')] * (N+1)
dp[0]=0
for i in range(N):
    # flip only left pancake if at left end
    if i==0:
        cost=dp[i]+p[i]
        if cost<dp[i+1]: dp[i+1]=cost
    # flip only right pancake if at right end
    if i==N-1:
        cost=dp[i]+p[i]
        if cost<dp[i+1]: dp[i+1]=cost
    # flip adjacent pancakes i and i+1
    if i+1<N:
        cost=dp[i]+p[i]+p[i+1]
        if cost<dp[i+2]: dp[i+2]=cost
print(dp[N])