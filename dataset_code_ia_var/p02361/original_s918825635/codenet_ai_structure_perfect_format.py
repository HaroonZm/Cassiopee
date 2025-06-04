from collections import defaultdict
from collections import deque
from sys import stdin

def sp(G, R, V):
    d = {}
    INF = float('inf')
    for i in range(V):
        d[i] = INF
    d[R] = 0
    q = deque([R])
    while q:
        u = q.popleft()
        for v in G[u]:
            if d[v[0]] > d[u] + v[1]:
                d[v[0]] = d[u] + v[1]
                q.append(v[0])
    return d

V, E, R = [int(x) for x in stdin.readline().split(' ')]
G = defaultdict(list)
for _ in range(E):
    s, t, w = [int(x) for x in stdin.readline().split(' ')]
    G[s].append((t, w))
d = sp(G, R, V)
for k in range(V):
    if d[k] == float('inf'):
        print("INF")
    else:
        print(d[k])