import sys
from collections import deque
readline = sys.stdin.readline

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res

def bfs(s):
    Q = deque(s)
    used = set(s)
    dist = [0]*N
    while Q:
        vn = Q.pop()
        for vf in Edge[vn]:
            if vf not in used:
                used.add(vf)
                dist[vf] = 1 + dist[vn]
                Q.appendleft(vf)
    return dist

N = int(readline())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

dist0 = bfs([0])
st = dist0.index(max(dist0))
dists = bfs([st])
en = dists.index(max(dists))
diste = bfs([en])
D = dists[en]
path = [i for i in range(N) if dists[i] + diste[i] == D]
distp = bfs(path)

table = [1]*(N+5)
mini = 0
for i in range(N):
    if distp[i] == 0:
        continue
    fi = dists[i]
    if 2*distp[i] == fi:
        mini = max(mini, fi-1)
    else:
        mini = max(mini, fi)
    fi = diste[i]
    if 2*distp[i] == fi:
        mini = max(mini, fi-1)
    else:
        mini = max(mini, fi)

for i in range(mini+1):
    table[i] = 0
table[1] = 1
table[2] = 1
for i in range(D+1, N+1):
    table[i] = 1

print(''.join(map(str, table[1:N+1])))