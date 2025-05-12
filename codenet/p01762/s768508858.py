import sys
from collections import deque
def bfs(s,g,n):
    bfs_map = [-1]*n
    bfs_map[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in v[x]:
            for y in v[x]:
                if c[x][y] > 0 and bfs_map[y] < 0:
                    bfs_map[y] = bfs_map[x]+1
                    q.append(y)
    return bfs_map

def update(s,g,bfs_map):
    f = float("inf")
    p = [[None]*2 for i in range(bfs_map[g])]
    y = g
    for i in range(bfs_map[g])[::-1]:
        p[i][1] = y
        for x in v[y]:
            if c[x][y] > 0 and bfs_map[x] == i:
                if c[x][y] < f:
                    f = c[x][y]
                y = x
                p[i][0] = x
                break
        else:
            return 0
    for x,y in p:
        c[x][y] -= f
        c[y][x] += f
    return f

def dinic(s,g,n):
    f = 0
    while 1:
        bfs_map = bfs(s,g,n)
        if bfs_map[g] < 0:
            return f
        cap = update(s,g,bfs_map)
        while cap > 0:
            f += cap
            cap = update(s,g,bfs_map)

n = int(sys.stdin.readline())
d = [int(x) for x in sys.stdin.readline().split()]
c = [[0]*(n+1) for i in range(n+1)]
v = [[] for i in range(n+1)]
for i in range(1,n):
    if d[i-1] > 0:
        v[i].append(n)
        v[n].append(i)
        c[i][n] = float("inf")

for i in range(n-1):
    a,b,p = [int(x) for x in sys.stdin.readline().split()]
    v[a].append(b)
    v[b].append(a)
    c[a][b] = p
    c[b][a] = p

print(dinic(0,n,n+1))