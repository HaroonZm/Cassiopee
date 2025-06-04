import sys
from functools import partial
from operator import itemgetter

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

readints = lambda: list(map(int, sys.stdin.readline().split()))
readints0 = lambda: [x-1 for x in map(int, sys.stdin.readline().split())]
readfloats = lambda: list(map(float, sys.stdin.readline().split()))
readstrs = lambda: sys.stdin.readline().split()
readint = lambda: int(sys.stdin.readline())
readfloat = lambda: float(sys.stdin.readline())
readline = partial(input)
pf = partial(print, flush=True)


class UnionFind:
    __slots__ = ("parent",)
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        if p[x] < 0:
            return x
        root = x
        while p[root] >= 0:
            root = p[root]
        while x != root:
            p[x], x = root, p[x]
        return root

    def union(self, x, y):
        p = self.parent
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        if p[x] > p[y]: x, y = y, x
        p[x] += p[y]
        p[y] = x
        return True

    def groups(self):
        return [(i, -sz) for i, sz in enumerate(self.parent) if sz < 0]


def main():
    results = []
    while True:
        n, m = readints()
        if n == 0: break

        edges = [(*readints(), idx) for idx in range(m)]
        edges_sorted = sorted(edges, key=itemgetter(2,3))
        mst_idxs, non_mst, uf = [], [], UnionFind(n+1)
        mst_weight, mst_count = 0, 0
        for a, b, c, idx in edges_sorted:
            if uf.union(a, b):
                mst_idxs.append(idx)
                mst_weight += c
                mst_count += 1
            else:
                non_mst.append((a, b, c))
        
        res_sum, res_count = 0, 0
        for remove_idx in mst_idxs:
            uf_sub = UnionFind(n+1)
            w = edges[remove_idx][2]
            for idx in mst_idxs:
                if idx == remove_idx: continue
                a, b, _, _ = edges[idx]
                uf_sub.union(a, b)
            substitute = all(c != w or not uf_sub.union(a, b) for a, b, c in non_mst)
            if substitute:
                res_count += 1
                res_sum += w

        results.append(f"{res_count} {res_sum}")
        break
    return '\n'.join(results)

print(main())