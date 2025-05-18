# https://onlinejudge.u-aizu.ac.jp/beta/room.html#ACPC2018Day3/problems/C

import collections

n = int(input().rstrip())

g = [[] for i in range(n)]
deg = [0 for i in range(n)]

for i in range(n):
    u, v = map(lambda x: x-1, map(int, input().rstrip().split(' ')))
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

q = collections.deque()

for i in range(n):
    if deg[i] == 1:
        q.append(i)

isPushed = [False for i in range(n)]

while len(q) > 0:
    v = q.popleft()
    isPushed[v] = True
    for nv in g[v]:
        deg[nv] -= 1

        if deg[nv] == 1:
            q.append(nv)

q = int(input().rstrip())

for _ in range(q):
    a, b = map(lambda x: x-1, map(int, input().rstrip().split(' ')))
    if isPushed[a] or isPushed[b]:
        print(1)
    else:
        print(2)