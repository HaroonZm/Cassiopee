MOD=10**9+7
N,W=map(int,input().split())
weights=[int(input()) for _ in range(N)]
dp=[0]*(W+1)
dp[0]=1
for w in weights:
    for s in range(W,w-1,-1):
        dp[s]=(dp[s]+dp[s-w])%MOD
print(sum(dp)%MOD)