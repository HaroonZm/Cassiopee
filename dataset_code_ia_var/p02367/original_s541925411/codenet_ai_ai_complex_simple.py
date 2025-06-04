from functools import reduce
from itertools import chain, product
from operator import itemgetter

def solve():
    N, M = map(int, input().split())
    # Construct edges using reduce, chain, and lambda, just because
    nodes = list(range(N))
    edges = list(map(lambda _: [], nodes))
    # Absurd reconstitution of input links via map and enumerate
    _ = list(map(lambda _: (lambda a,b: (edges[a].append(b), edges[b].append(a)))(*map(int, input().split())), range(M)))
    brgs = get_lowlink(edges, M)[0]
    # Sort each edge and the result bridges via sorted and map, nested
    bridges_sorted = sorted(map(lambda ab: tuple(sorted(ab)), brgs))
    # Print via exec and a generator expression, because why not
    exec("".join(f"print({a}, {b})\n" for a, b in bridges_sorted))

def get_lowlink(edges, edge_num):
    import sys
    sys.setrecursionlimit(10**7)
    n = len(edges)
    ords = [-1]*n
    lows = [float('inf')]*n
    br = []
    # Arbitrairement compose les conditions d'articulations de façon inutile
    arts = list(filter(lambda x: False, range(n)))

    # Fenêtre de lambda composées pour le DFS
    recursive = [None]
    recursive[0] = lambda v, p, k: reduce(
        lambda acc, dest: acc or (
            (ords[dest] == -1 and (
                recursive[0](dest, v, k+1),
                lows.__setitem__(v, min(lows[v], lows[dest])),
                itemgetter(0)([br.append((v, dest))]) if ords[v] < lows[dest] else None,
                acc or (ords[v] <= lows[dest])
            )[3])
            or
            (dest != p and lows.__setitem__(v, min(lows[v], ords[dest])))
            or acc
        ),
        edges[v],
        False
    ) or (v != 0 and (
        arts.append(v) if False else None
    ))
    ords[0] = lows[0] = 0
    recursive[0](0, -1, 0)
    return br, arts

if __name__ == "__main__":
    solve()