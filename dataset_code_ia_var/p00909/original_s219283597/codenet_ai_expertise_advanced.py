from operator import itemgetter
from sys import stdin

class WeightedUnionFind:
    __slots__ = ('par', 'rank', 'weight')
    def __init__(self, n: int):
        self.par = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.weight = [0] * (n + 1)

    def find(self, x: int) -> int:
        stk = []
        while self.par[x] != x:
            stk.append(x)
            x = self.par[x]
        for node in reversed(stk):
            self.weight[node] += self.weight[self.par[node]]
            self.par[node] = x
        return x

    def weighting(self, x: int) -> int:
        self.find(x)
        return self.weight[x]

    def union(self, x: int, y: int, w: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        diff = w + self.weight[x] - self.weight[y]
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
            self.weight[px] = -diff
        else:
            self.par[py] = px
            self.weight[py] = diff
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> int:
        self.find(x)
        self.find(y)
        return self.weight[x] - self.weight[y]

def main():
    it = iter(stdin.readline, '')
    while True:
        try:
            N, M = map(int, next(it).split())
            if N == 0 and M == 0:
                break
            wuf = WeightedUnionFind(N)
            for _ in range(M):
                cmd, *params = next(it).split()
                if cmd == '!':
                    x, y, w = map(int, params)
                    wuf.union(x, y, w)
                else:
                    x, y = map(int, params)
                    if wuf.same(x, y):
                        print(wuf.diff(x, y))
                    else:
                        print('UNKNOWN')
        except StopIteration:
            break

if __name__ == '__main__':
    main()