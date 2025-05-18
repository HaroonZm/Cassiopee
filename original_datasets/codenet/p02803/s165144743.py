import sys
input = sys.stdin.readline
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

H,W=map(int,input().split())
S=[list(input().strip()) for _ in range(H)]
G=[[float("inf")]*H*W for _ in range(H*W)]
for i in range(H*W):
    G[i][i]=0
#print(S)
for h in range(H):
    for w in range(W-1):
        if S[h][w]=="." and S[h][w+1]==".":
            G[W*h+w][W*h+w+1]=1
            G[W*h+w+1][W*h+w]=1

for h in range(H-1):
    for w in range(W):
        if S[h][w]=="." and S[h+1][w]==".":
            G[W*h+w][W*(h+1)+w]=1
            G[W*(h+1)+w][W*h+w]=1

#print(G)
n=H*W
G=warshall_floyd(G)
#print(G)
ans=0
for h in range(H*W):
    for w in range(H*W):
        if G[h][w]!=float("inf"):
            ans=max(ans,G[h][w])
print(ans)