import sys
from operator import itemgetter

stdin = sys.stdin
inf = float('inf')
mod = 10**9 + 7

ni   = lambda: int(stdin.readline())
na   = lambda: list(map(int, stdin.readline().split()))
nas  = lambda: stdin.readline().split()

class WUnionFind:
    __slots__ = ('n', 'par', 'rank', 'diff_weight', '_size', '_edges')

    def __init__(self, n, sum_unity=0):
        self.n = n
        self.par = list(range(n))
        self.rank = [0]*n
        self.diff_weight = [sum_unity]*n
        self._size = [1]*n
        self._edges = 0

    def find(self, x):
        path = []
        while self.par[x] != x:
            path.append(x)
            x = self.par[x]
        for node in path:
            self.diff_weight[node] += self.diff_weight[self.par[node]]
            self.par[node] = x
        return x

    def unite(self, x, y, w):
        x_root = self.find(x)
        y_root = self.find(y)
        w += self.weight(x) - self.weight(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.par[x_root] = y_root
            self.diff_weight[x_root] = -w
            self._size[y_root] += self._size[x_root]
        else:
            self.par[y_root] = x_root
            self.diff_weight[y_root] = w
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
            self._size[x_root] += self._size[y_root]
        self._edges += 1

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

    def size(self, x):
        return self._size[self.find(x)]

    def trees(self):
        return self.n - self._edges

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    input_na = na
    input_nas = nas
    while True:
        try:
            n, m = input_na()
        except Exception:
            break
        if n == 0 and m == 0:
            break
        wuf = WUnionFind(n)
        for _ in range(m):
            que = input_nas()
            match que:
                case ["!", a, b, w]:
                    a, b, w = int(a)-1, int(b)-1, int(w)
                    wuf.unite(a, b, w)
                case ["?", a, b]:
                    a, b = int(a)-1, int(b)-1
                    print(wuf.diff(a, b) if wuf.same(a, b) else "UNKNOWN")
                case _:
                    continue

if __name__ == "__main__":
    main()