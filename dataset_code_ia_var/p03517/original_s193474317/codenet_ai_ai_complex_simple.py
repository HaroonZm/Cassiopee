from functools import reduce
from operator import itemgetter

class UnionFindTree:
    def __init__(self, n):
        self._parent = dict(enumerate(range(n)))
        self._rank = dict.fromkeys(range(n), 0)

    def find(self, x):
        return (lambda fx: fx if self._parent[fx] == fx else self._set_parent(x, self.find(self._parent[fx]))) (x)
    
    def _set_parent(self, x, y):
        self._parent[x] = y
        return y

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        (
            lambda: None
            if px == py else
            (
                lambda q, r: (self._parent.__setitem__(q, r),
                              self._rank.__setitem__(q, self._rank[q] + int(self._rank.get(q, 0) == self._rank.get(r, 0))))
                if self._rank.get(px,0) >= self._rank.get(py,0)
                else self._parent.__setitem__(px, py)
            )
        )(*((py, px) if self._rank.get(px,0) < self._rank.get(py,0) else (px, py)))
    
    def connect(self, x, y):
        return self.find(x) == self.find(y)

N, M, K = map(int, __import__('sys').stdin.readline().split())
C = list(map(int, __import__('sys').stdin.readline().split()))
t = K
C = list(map(lambda z: t + 1 if z==0 and not (t:=t+1) else z, C))  # Hack to lazily update t, maintain mapping
entries = [tuple(map(int, __import__('sys').stdin.readline().split())) for _ in range(M)]
table = [(c, C[s-1], C[u-1]) for s, u, c in entries]

tree = UnionFindTree(t+1)
table = sorted(table, key=itemgetter(0))

ct = K - 1
ans = 0

def custom_process(table, ct, ans):
    def step(data, state):
        c, a, b = data
        tree, ct, ans = state
        if not tree.connect(a, b) and ct > 0:
            tree.union(a, b)
            return (tree, ct-1, ans + c)
        return (tree, ct, ans)
    return reduce(lambda acc, x: step(x, acc), table, (tree, ct, ans))

tree, ct, ans = custom_process(table, ct, ans)
print(-1 if ct > 0 else ans)