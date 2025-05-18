n,m=map(int,input().split())
dp=[0]*(m+1)
for _ in range(n):
    v,w=map(int,input().split())
    for i in range(w,m+1):dp[i]=max(dp[i],dp[i-w]+v)
print(dp[m])