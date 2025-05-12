import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
inf = float('inf')

n,m = map(int,input().split())
pathT = [{} for _ in range(n)]
for i in range(m):
    x,y,t = map(int,input().split())
    x -= 1
    y -= 1
    pathT[x][y] = t
    pathT[y][x] = t

import heapq 
def Dijkstra(edge,start):
    d = [[float('inf'),float('inf')] for _ in range(len(edge))]
    d[start][0] = 0
    pq = [(0,start,0)]
    heapq.heapify(pq)
    while pq:
        dist,p,flag = heapq.heappop(pq)
        toflag = flag or (p%n == n-1)
        if dist > d[p][flag]:continue
        for to,cost in edge[p].items():
            if d[to][toflag] <= dist + cost:continue
            d[to][toflag] = dist + cost
            heapq.heappush(pq, (d[to][toflag], to, toflag))
    return d

v0 = int(input())
a,b,c = map(int,input().split())
V = [v0]
v = v0
Vs = set()
while True:
    v = (a*v + b)%c
    if v in Vs:
        loop = V.index(v)
        break
    # print(v)
    V.append(v)
    Vs.add(v)
p = len(V)

path = [{} for _ in range(p*n)]
for now,nxtD in enumerate(pathT):
    for i,v in enumerate(V):
        for nxt,t in nxtD.items():
            if i+1 != p:
                path[i*n + now][(i+1)*n + nxt] = t*v
            else:
                path[i*n + now][loop*n + nxt] = t*v

d = Dijkstra(path,0)
ans = float('inf')
for i in range(p):
    ans = min(ans, d[i*n][1])
    # d2 = Dijkstra(path,i*n + n-1)
    # # res = float('inf')
    # for j in range(p):
    #     # res = min(res, d2[j*n])
    #     ans = min(ans, d[i*n + n-1] + d2[j*n])
print(ans)