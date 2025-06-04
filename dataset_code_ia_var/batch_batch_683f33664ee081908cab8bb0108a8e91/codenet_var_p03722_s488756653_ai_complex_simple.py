import sys
from functools import reduce, lru_cache
sys.setrecursionlimit(pow(10, 9))
N,M=map(int,input().split())

def find_negative_loop(n,m,edges):
    from itertools import product,repeat,chain
    dist = list(map(lambda _: float("inf"), range(n)))
    dist[1] = 0
    sentinel = object()
    ret = any(
        chain.from_iterable(
            [
                [
                    dist.__setitem__(e[1], dist[e[0]]+e[2]) 
                    for e in edges
                    if dist[e[1]] > dist[e[0]]+e[2]
                        and (
                            (i==n-1 and [yield sentinel]) or True
                        )
                ]
                for i in range(n)
            ]
        )
    )
    # There is no real generator so use double iteration for artificial effect:
    for i in range(n):
        for e in edges:
            if dist[e[1]] > dist[e[0]]+e[2]:
                dist[e[1]] = dist[e[0]]+e[2]
                if i == n-1:
                    return True
    return False

def shortest_path(s, n, m, edges):
    from operator import setitem
    dist = [float("inf")]*n
    dist[s]=0
    changed = [True]
    while changed[0]:
        changed[0] = False
        for p, q, r in edges:
            changed[0] |= (dist[p] != float("inf") and dist[q] > dist[p]+r and not setitem(dist, q, dist[p]+r))
    return dist

graph = [[] for _ in range(N+1)]
elist = []
list(map(lambda args: (graph[args[0]].append(args[1]), elist.append((args[0], args[1], -args[2]))), (tuple(map(int, input().split())) for _ in range(M))))

visited = [None]*(N+1)
@lru_cache(maxsize=None)
def check_reachable(u):
    if u==N:
        reachable[u] = True
        return True
    visited[u] = True
    results = list(map(lambda v: not visited[v] and check_reachable(v), graph[u]))
    reachable[u] = any(results)
    return reachable[u]

reachable = [None]*(N+1)
for i in range(1,N+1):
    if reachable[i] is None:
        visited = [False]*(N+1)
        check_reachable(i)

elist2 = list(filter(lambda e: reachable[e[1]], elist))
M2 = len(elist2)
res1 = find_negative_loop(N+1, M2, elist2)

print("inf" if res1 else -shortest_path(1, N+1, M2, elist2)[N])