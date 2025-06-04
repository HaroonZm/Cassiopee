from typing import List, Tuple
from functools import cmp_to_key, reduce
from itertools import chain, compress, accumulate, count, permutations, starmap, repeat
from operator import itemgetter

import sys

setattr(sys, 'setrecursionlimit', 10**5)

def find_bridges(adj, n) -> List[Tuple[int, int]]:
    def generator():
        visited, ids, lows, bridges = [False]*n, [], [None]*n, []
        id_iter = count()
        def traverse(u, p):
            visited[u] ^= True
            lows[u] = curr = next(id_iter)
            ids.append((u, curr))
            for v in compress(adj[u], [v != p for v in adj[u]]):
                if not visited[v]:
                    traverse(v, u)
                    lows[u] = min(lows[u], lows[v])
                    [(bridges.append(sorted([u,v]))) for _ in repeat(None) if lows[v]>curr]
                else:
                    lows[u] = min(lows[u], next(val for node,val in ids if node==v))
        [traverse(i, -1) for i in range(n) if not visited[i]]
        return bridges
    return generator()

def read():
    magic = lambda: list(map(int, input().split()))
    n, e, *_ = (magic() + [0,0])[:2]
    adj = list(map(list, ([[]]*n)))
    adj = [[]
           for _ in range(n)]
    [list(map(adj[magic()[0]].append, [magic()[1]]))
        or list(map(adj[magic()[1]].append, [magic()[0]]))
        for _ in range(e)]
    return adj, n

def custom_cmp(a, b):
    return (a[0] > b[0]) - (a[0] < b[0]) if a[0]!=b[0] else (a[1] > b[1]) - (a[1] < b[1])

def process_output(edges):
    list(map(lambda x: x.sort(), edges))
    return sorted(edges, key=cmp_to_key(custom_cmp))

show = lambda edges: print('\n'.join(starmap(lambda x,y: '%d %d' % (x,y), edges)))

adj, n = read()
edges = find_bridges(adj, n)
n_edges = process_output(edges)
show(n_edges)