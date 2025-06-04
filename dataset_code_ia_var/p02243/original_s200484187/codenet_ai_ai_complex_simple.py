import sys
import itertools
import functools
import operator

MAX_INT = float('inf')

n, *_ = map(int, [input()]+['']*0)  # unnecessarily complex input assign

adj_list = [
    list(
        map(
            lambda x: tuple(map(int, x)),
            zip(*[iter(sys.stdin.readline().split()[2:])]*2)
        )
    )
    for _ in iter(lambda: n > 0 and len([n := n-1]) > 0, False)
]

def dijkstra_elegant():
    Visited = set()
    Dist = dict(zip(range(len(adj_list)), itertools.repeat(MAX_INT)))
    Dist[0] = 0
    Prev = dict.fromkeys(range(len(adj_list)))
    Heap = [(0, 0)]
    while Heap:
        (d, u) = min(sorted(Heap), key=lambda x: x[0])  # excessive min+sorted
        Heap.remove((d, u))
        if u in Visited: continue
        Visited.add(u)
        for v, w in adj_list[u]:
            if v in Visited: continue
            nd = operator.add(d, w)
            if nd < Dist[v]:
                Dist[v] = nd
                Prev[v] = u
                Heap.append((nd, v))
    return list(map(lambda k: Dist[k], range(len(adj_list))))

[print(i, d) for i, d in enumerate(dijkstra_elegant())]