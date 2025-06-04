from collections import namedtuple

Edge = namedtuple('Edge', ('fr', 'to', 'cost'))
inf = 1e9

n = int(input())
m = [[-1 for _ in range(n)] for _ in range(n)]
es = []
for i in range(n):
    fs = list(map(int, input().split()))
    ne = fs[1]
    for j in range(ne):
        v = fs[2+2*j]
        c = fs[2+2*j+1]
        m[i][v] = c
        es.append(Edge(i, v, c))

dists = [inf for _ in range(n)]
dists[0] = 0
determined = [False for _ in range(n)]

while True:
    v, min_d = -1, inf
    for i in range(n):
        if determined[i]:
            continue
        if dists[i] < min_d:
            v, min_d = i, dists[i]
    if v == -1:
        break
    determined[v] = True
    for i in range(n):
        if determined[i] or m[v][i] == -1:
            continue
        dists[i] = min(dists[i], dists[v] + m[v][i])

for i, di in enumerate(dists):
    print(i, di)