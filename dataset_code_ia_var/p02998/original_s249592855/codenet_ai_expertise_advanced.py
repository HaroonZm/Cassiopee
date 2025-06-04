import sys
from functools import partial
from collections import defaultdict

input = sys.stdin.readline
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

class UnionFind:
    __slots__ = ('n', 'parents')
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        px = self.parents
        while px[x] >= 0:
            if px[px[x]] >= 0:
                px[x] = px[px[x]]
            x = px[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px = self.parents
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        if px[x] > px[y]:
            x, y = y, x
        px[x] += px[y]
        px[y] = x
        return True

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, p in enumerate(self.parents) if p < 0]

    def group_count(self) -> int:
        return sum(1 for p in self.parents if p < 0)

def main():
    N = I()
    M = 10**5
    XY = [0] * (2 * M)
    uf = UnionFind(2 * M)
    for _ in range(N):
        x, y = MI()
        x -= 1
        y = y - 1 + M
        XY[x] += 1
        XY[y] += 1
        uf.union(x, y)
    ddx = defaultdict(int)
    ddy = defaultdict(int)
    dde = defaultdict(int)
    for i, e in enumerate(XY):
        root = uf.find(i)
        if i < M:
            ddx[root] += 1
        else:
            ddy[root] += 1
        dde[root] += e
    ans = sum(ddx[k] * ddy[k] - v // 2 for k, v in dde.items())
    print(ans)

main()