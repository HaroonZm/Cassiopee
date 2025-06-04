import sys
from functools import reduce
from itertools import chain
input = sys.stdin.readline

N = int(input())
Log_N = (N-1).bit_length()

prev = [list(map(lambda _: -1, range(Log_N+1))) for _ in range(N)]
graph = [[] for _ in range(N)]

[graph.__setitem__(i, a:=list(map(int, input().split()))[1:]) or [prev.__setitem__(x, prev[x][:1]+[i]+prev[x][2:]) for x in a] for i in range(N)]

Q = int(input())
Query = [tuple(map(int, input().split())) for _ in range(Q)]

Depth = [-1]*N
def BFS(g):
    S, d, seen = {0}, 0, set()
    Depth[0] = 0
    while S:
        d += 1
        S = {nxt for p in S for nxt in g[p] if Depth[nxt]==-1 and not seen.add(nxt)}
        for s in S: Depth[s] = d
BFS(graph)

[[prev[i].__setitem__(k+1, (lambda x: -1 if x==-1 else prev[x][k])(prev[i][k])) for i in range(N)] for k in range(Log_N)]

def LCA(u, v):
    if Depth[u] > Depth[v]:
        u, v = v, u
    f = lambda v, z: prev[v][z[0]] if z[1] else v
    diff = Depth[v] - Depth[u]
    v = reduce(lambda acc, z: f(acc, z), enumerate(map(lambda k: (diff>>k)&1, range(Log_N+1))), v)
    if u == v: return u
    for k in reversed(range(Log_N)):
        p = (prev[u][k], prev[v][k])
        u, v = (u, v) if p[0]==p[1] else p
    return prev[u][0]

print('\n'.join(map(str, map(lambda ab: LCA(*ab), Query))))