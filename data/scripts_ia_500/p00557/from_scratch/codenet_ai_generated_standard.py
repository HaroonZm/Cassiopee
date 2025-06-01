import sys
sys.setrecursionlimit(10**7)
H,W=map(int,input().split())
e=[list(map(int,input().split())) for _ in range(H)]
pos=[[-1]*W for _ in range(H)]
flow_map = {}
for i in range(H):
    for j in range(W):
        flow_map[e[i][j]]=(i,j)
        
def neighbors(i,j):
    for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
        if 0<=ni<H and 0<=nj<W:
            yield ni,nj

dp = [[-1]*W for _ in range(H)]
def sinks(i,j):
    if dp[i][j]>=0:
        return dp[i][j]
    low = []
    for ni,nj in neighbors(i,j):
        if e[ni][nj]<e[i][j]:
            low.append(sinks(ni,nj))
    if not low:
        dp[i][j]=1
    else:
        dp[i][j]=sum(low)
    return dp[i][j]

S = set()
for i in range(H):
    for j in range(W):
        sinks(i,j)

count=0
for i in range(H):
    for j in range(W):
        if dp[i][j]>=2:
            count+=1
print(count)