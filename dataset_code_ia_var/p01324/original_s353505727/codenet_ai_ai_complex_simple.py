from functools import reduce
from operator import add, ge, itemgetter
from itertools import chain, tee, zip_longest, accumulate, count as itercount
from collections import defaultdict
from math import inf

class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1]*n
        self.w = [0]*n

    def find(self, x):
        stack = []
        while self.p[x] >= 0:
            stack.append(x)
            x = self.p[x]
        root = x
        def propagate():
            last = root
            for z in reversed(stack):
                self.w[z] += self.w[self.p[z]]
                self.p[z] = last
                last = z
        propagate() if stack else None
        return root

    def union(self, x, y, w):
        fx, fy = list(map(self.find, (x, y)))
        w = w + self.w[x] - self.w[y]
        swap = lambda: (fy, fx, -w) if self.p[fx] > self.p[fy] else (fx, fy, w)
        x_, y_, w_ = swap()
        if fx == fy: return
        self.p[x_] += self.p[y_]
        self.p[y_] = x_
        self.w[y_] = w_
        
    def weig(self, x):
        _=self.find(x)
        return self.w[x]
    
    def diff(self, x, y):
        return self.weig(y) - self.weig(x)
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

def group_indices(*seqs):
    seen = {}
    idx = count = 0
    for s in chain(*seqs):
        if s not in seen:
            seen[s] = count
            count += 1
    return seen

def eq(x, y): return x == y

def quit_if(cond): [exit() for _ in [0] if cond]

while True:
    n = int(input())
    quit_if(n==0)
    Q = []
    names = set()
    for _ in range(n):
        *_, a, _, p, b = input().split()
        Q.append((a, b, int(p[3:])))
        names |= {a, b}
    D = group_indices(names)
    UF = WeightedUnionFind(len(D))
    failed = False
    for a, b, p in Q:
        ia, ib = D[a], D[b]
        if UF.same(ia, ib):
            failed = failed or not eq(p, UF.diff(ia, ib))
            if failed:
                print("No"); break
        else:
            UF.union(ia, ib, p)
    else:
        print("Yes")