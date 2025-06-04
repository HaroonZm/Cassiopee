import sys
from heapq import heappush, heappop

class UnionFind:
    __slots__ = ('parent', 'rank')

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        px = self.parent
        if px[x] != x:
            px[x] = self.find(px[x])
        return px[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        rx, ry = self.rank[xr], self.rank[yr]
        if rx < ry:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if rx == ry:
                self.rank[xr] += 1
        return True

def kruskal(n, edges):
    uf = UnionFind(n)
    ans = 0
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            ans += w
    return ans

def main():
    input_ = sys.stdin.readline
    v, e = map(int, input_().split())
    edges = [tuple(map(int, input_().split()))[::-1] for _ in range(e)]
    print(kruskal(v, edges))

if __name__ == '__main__':
    main()