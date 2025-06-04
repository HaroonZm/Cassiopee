n=int(input())
c=[input() for _ in range(n)]
MOD=10**9+7

U=[0]*(n+1)
for i in range(n):
    if c[i]=='U':
        U[i+1]=U[i]+1
    else:
        U[i+1]=0

dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    ndp=[0]*(n+1)
    if c[i-1]=='-':
        s=0
        for j in range(i):
            s=(s+dp[j])%MOD
        for j in range(i+1):
            ndp[j]=s
    elif c[i-1]=='U':
        s=0
        for j in range(i):
            s=(s+dp[j])%MOD
            ndp[j]=s
        ndp[i]=0
    else: # D
        s=0
        for j in range(i,-1,-1):
            s=(s+dp[j])%MOD
            ndp[j]=s
    dp=ndp

print(dp[0]%MOD)