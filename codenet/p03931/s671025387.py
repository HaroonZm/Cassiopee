mod=10**9+7
n,x=map(int,input().split())
a=list(map(int,input().split()))
dp=[[[0]*256 for j in range(n+1)] for k in range(2)]
dp[0][0][0]=1
for i in range(n):
  for j in range(n+1):
    for k in range(256):
      dp[(i+1)&1][j][k]=dp[i&1][j][k]
  for j in range(n):
    for k in range(256):
      dp[(i+1)&1][j+1][k^a[i]]+=dp[i&1][j][k]
      if mod<=dp[(i+1)&1][j][k^a[i]]:
        dp[(i+1)&1][j][k^a[i]]-=mod

ans=0
fac=[1]*(n+1)
for i in range(1,n+1):
  fac[i]=fac[i-1]*i
  if mod<=fac[i]:
    fac[i]-=mod
for j in range(n+1):
  ans+=dp[n&1][j][x]*fac[j]
  ans%=mod

print(ans)