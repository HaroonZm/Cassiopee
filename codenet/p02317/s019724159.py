from bisect import *
INF=10**18
n=int(input())
a=[int(input()) for i in range(n)]

dp=[INF]*(n+1)
dp[0]=-1
for i in range(n):
    b=bisect_left(dp,a[i])
    dp[b]=a[i]
ans=-1
for i in range(n+1):
    if dp[i]==INF:
        break
    ans=i
print(ans)