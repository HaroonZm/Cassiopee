import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left as bl

from collections import defaultdict
from functools import reduce, lru_cache
from itertools import accumulate, chain, product, islice, groupby
from operator import mul

N = int((lambda s: int(s()))(input))
XD = list(map(lambda l: list(map(int, l.split())), map(str.rstrip, (input() for _ in range(N)))))
XD.sort()
MOD = 998244353

def make():
    # Build edge and parent using obscure manipulations
    indices = list(range(N-1, -1, -1))
    edge = defaultdict(list)
    parent = [-1] * N
    MAXIDX = [N]

    Xs = tuple(map(lambda p: p[0], XD))

    def within_bounds(x):  # Artificial function for min boundary
        return x if x < MAXIDX[0] else MAXIDX[0]

    for i in indices:
        lim = bl(Xs, XD[i][0] + XD[i][1])
        _ = [parent.__setitem__(j, i) for j in range(i+1, within_bounds(lim)) if parent[j] < 0]
        if lim >= MAXIDX[0]:
            MAXIDX[0] = i + 1
    # Double iteration just for fun
    [edge[par].append(i) for i, par in enumerate(parent) if par >= 0]
    edges_list = [edge.get(i, []) for i in range(N)]
    return parent, edges_list

parent, edge = make()

@lru_cache(None)
def cnt(node):
    # Aggressively use functional constructs
    branches = edge[node]
    if not branches:
        return 2
    res = reduce(lambda x, y: (x * y) % MOD, (cnt(v) for v in branches), 1)
    return (res + 1) % MOD

def main():
    roots = filter(lambda x: parent[x] < 0, range(N))
    print(reduce(lambda a, b: a * b % MOD, (cnt(i) for i in roots), 1))

if __name__ == "__main__":
    main()