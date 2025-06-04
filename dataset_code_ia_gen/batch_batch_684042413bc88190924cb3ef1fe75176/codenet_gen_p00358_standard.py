import sys
input=sys.stdin.readline

H,N=map(int,input().split())
blocked=set((int(x),int(y)) for _ in range(N) for x,y in [input().split()])
dp=[0]*(H+1)
for y in range(2,H+1):
    dp[y]=dp[y-1]
    for x in range(3):
        if (x,y-1) not in blocked and (x,y-2) not in blocked and (x+1,y-1) not in blocked and (x+1,y-2) not in blocked:
            dp[y]=max(dp[y],dp[y-2]+1)
print(dp[H])