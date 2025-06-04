import sys
import math
import itertools
import random
from functools import partial

# Utilisation de l'import dynamique pour éviter les imports inutilisés
imported_modules = [
    "string", "fractions", "heapq", "collections", "re",
    "array", "bisect", "time", "copy"
]
for mod in imported_modules:
    globals()[mod] = __import__(mod)

sys.setrecursionlimit(10**7)
inf = float('inf')
eps = 1e-10
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonctions utilitaires vectorisées et généralisées
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI0(): return [x-1 for x in LI()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

class UnionFind:
    __slots__ = ("parent",)
    def __init__(self, size):
        self.parent = [-1]*size

    def find(self, x):
        px = self.parent[x]
        if px < 0: return x
        root = self.find(px)
        self.parent[x] = root
        return root

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def subsetall(self):
        return [(i, -v) for i, v in enumerate(self.parent) if v < 0]

def main():
    results = []
    input_func = sys.stdin.readline

    while True:
        n, m = map(int, input_func().split())
        if n == 0: break

        edge_list = sorted([tuple(reversed(LI())) for _ in range(m)])
        edge_list += [(inf, 1, i) for i in range(2, n+1)]

        min_res = inf

        for idx in range(m):
            uf = UnionFind(n+1)
            max_t = uc = 0
            for t, x, y in itertools.islice(edge_list, idx, None):
                if uf.union(x, y):
                    max_t = t
                    uc += 1
                    if uc == n-1: break
            if max_t == inf: break
            res = max_t - edge_list[idx][0]
            min_res = min(min_res, res)
        results.append(str(-1 if min_res == inf else min_res))

    return '\n'.join(results)

if __name__ == "__main__":
    print(main())