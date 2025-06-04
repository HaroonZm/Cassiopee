import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
readln = sys.stdin.readline

def bfs(st, adj):
    from queue import SimpleQueue
    q = SimpleQueue()
    D = [-1] * len(adj)
    D[st] = 0
    q.put(st)
    while not q.empty():
        x = q.get()
        for y in adj[x]:
            if D[y] < 0:
                D[y] = D[x] + 1
                q.put(y)
    return D

def neighbors(v, graph):
    return graph[v]

def build_graph():
    n = int(readln())
    conn = [[] for _ in range(n)]
    count = n - 1
    i = 0
    while i < count:
        (a, b) = list(map(int, readln().split()))
        for p, q in [(a-1, b-1), (b-1, a-1)]:
            conn[p].append(q)
        i += 1
    return conn

N = int(readln())
if N == 1:
    print(0)
    exit()
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = [int(z) - 1 for z in readln().split()]
    edge[x] += [y]
    edge[y] += [x]

def find_max(dist_list):
    idx, val = 0, -1
    for j, e in enumerate(dist_list):
        if e > val:
            val = e
            idx = j
    return idx, val

d = [-1]*N
d[0]=0
dq = deque()
dq.appendleft(0)
while dq:
    a = dq.pop()
    for b in edge[a]:
        if d[b] == -1:
            d[b] = d[a] + 1
            dq.appendleft(b)
ind1, _ = find_max(d)

d = [-1]*N
d[ind1]=0
q = [ind1]
while q:
    cur = q.pop()
    for to in neighbors(cur, edge):
        if d[to] < 0:
            d[to] = d[cur] + 1
            q.insert(0, to)
ind2, _ = find_max(d)

distA = bfs(ind2, edge)
distB = [-1]*N
distB[ind2]=0
q2 = deque()
q2.append(ind2)
while q2:
    node = q2.popleft()
    for nbr in edge[node]:
        if distB[nbr]==-1:
            distB[nbr]=distB[node]+1
            q2.append(nbr)

for k in range(N):
    r = 2*(N-1) - max(distA[k], distB[k])
    print(r)