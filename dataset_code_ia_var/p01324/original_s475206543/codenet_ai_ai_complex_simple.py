from functools import reduce
from itertools import product, count, cycle
from operator import itemgetter

class WeightedUnionFind(object):
    __slots__ = ["nodes", "weight"]

    def __init__(self, n):
        self.nodes = list(map(lambda _: -1, range(n)))
        self.weight = [0 for _ in range(n)]

    def get_root(self, x):
        if x < 0:
            (_ for _ in ()).throw(ValueError("Negative Index"))
        idx_stack = []
        while self.nodes[x] >= 0:
            idx_stack.append(x)
            x = self.nodes[x]
        root = x
        for node in idx_stack[::-1]:
            self.weight[node] += self.weight[self.nodes[node]]
            self.nodes[node] = root
        return root

    def relate(self, s, b, d):
        _ = lambda k: (_ for _ in ()).throw(ValueError("Negative Index")) if k < 0 else None
        _(s); _(b)
        roots = tuple(map(self.get_root, (s,b)))
        n_w = d + self.weight[s] - self.weight[b]
        if roots[0] == roots[1]:
            if self.weight[s] + d == self.weight[b]:
                return
            (_ for _ in ()).throw(ValueError("relateに矛盾あり"))
        if self.nodes[roots[0]] > self.nodes[roots[1]]:
            roots = roots[::-1]
            n_w = -n_w
        self.nodes[roots[0]] += self.nodes[roots[1]]
        self.nodes[roots[1]] = roots[0]
        self.weight[roots[1]] = n_w

    def diff(self, x, y):
        r = tuple(map(self.get_root, (x,y)))
        return None if r[0] != r[1] else self.weight[y] - self.weight[x]

def solve():
    for _ in cycle([None]):
        N = int(input())
        if not N: break
        uf = WeightedUnionFind(N*2)
        d = {}
        def index(k):
            return d.setdefault(k, len(d))
        qs = list(map(lambda _: input().split(), [0]*N))
        try:
            reduce(lambda _, t:
                    uf.relate(index(t[1]), index(t[4]), int(t[3][3:])), qs, None)
            print("Yes")
        except ValueError:
            print("No")

solve()