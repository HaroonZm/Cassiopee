m,n=map(int,input().split())
p=[list(map(float,input().split())) for _ in range(m)]
dp=[-1]*(1<<n)
def dfs(mask):
    if dp[mask]>=0: return dp[mask]
    if mask==(1<<n)-1: return 1.0
    res=0.0
    for i in range(m):
        pos=0
        while pos<n and (mask&(1<<pos)): pos+=1
        q=p[i][pos]
        win=dfs(mask|(1<<pos))*q
        lose=dfs(mask)* (1-q)
        res=max(res,win+lose)
    dp[mask]=res
    return res
print(dfs(0))