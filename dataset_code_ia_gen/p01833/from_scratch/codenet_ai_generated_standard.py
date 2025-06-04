import sys
from collections import deque
input = sys.stdin.readline

N,A,B,C=map(int,input().split())
Aset=set(map(int,input().split()))
Bset=set(map(int,input().split()))
Cset=set(map(int,input().split()))
M=int(input())
g=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)

grades = [0]*(N+1)
for a in Aset: grades[a] = 1
for b in Bset: grades[b] = 2
for c in Cset: grades[c] = 3

INF = 10**9
distA=[INF]*(N+1)
distB=[INF]*(N+1)
distC=[INF]*(N+1)

def bfs(starts,dist):
    q=deque()
    for s in starts:
        dist[s]=0
        q.append(s)
    while q:
        u=q.popleft()
        d=dist[u]
        for w in g[u]:
            if dist[w]>d+1:
                dist[w]=d+1
                q.append(w)

bfs(Aset,distA)
bfs(Bset,distB)
bfs(Cset,distC)

res_cost = INF
res_id = N+1
for i in range(1,N+1):
    cost = distA[i]+distB[i]+distC[i]-2
    if cost<res_cost or (cost==res_cost and i<res_id):
        res_cost=cost
        res_id=i
print(res_cost,res_id)