# Author: cr4zjh0bp
# Created: Fri Mar 20 22:48:43 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

class WUnionFind:
    def __init__(self, n, sum_unity=0):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.diff_weight = [sum_unity for _ in range(n)]
        self._size = [1 for _ in range(n)]
        self._edges = 0

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.find(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return r
        
    def unite(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.diff_weight[x] = -w
            self._size[y] += self._size[x]
            self._edges += 1
        else:
            self.par[y] = x
            self.diff_weight[y] = w
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self._size[x] += self._size[y]
            self._edges += 1

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
    
    def size(self, x):
        x = self.find(x)
        return self._size[x]
    
    def trees(self):
        return self.n - self._edges

    def same(self, x, y):
        return self.find(x) == self.find(y)

while True:
    n, m = na()
    if n == 0 and m == 0:
        break
    wuf = WUnionFind(n)
    for i in range(m):
        que = nas()
        if que[0] == '!':
            a, b, w = list(map(int, que[1:]))
            a -= 1
            b -= 1
            wuf.unite(a, b, w)
        elif que[0] == '?':
            a, b = list(map(int, que[1:]))
            a -= 1
            b -= 1
            if wuf.same(a, b):
                print(wuf.diff(a, b))
            else:
                print("UNKNOWN")