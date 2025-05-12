import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

# MOD = 998244353

class UnionFind:
    def __init__(self, size=None, nodes=None):
        """
        size か nodes どっちか指定。
        nodes は set、size は list を使う。
        :param int size:
        :param collections.Iterable nodes:
        """
        assert size is not None or nodes is not None
        if size is not None:
            self._parents = [i for i in range(size)]
            self._ranks = [0 for _ in range(size)]
            self._sizes = [1 for _ in range(size)]
        else:
            self._parents = {k: k for k in nodes}
            self._ranks = {k: 0 for k in nodes}
            self._sizes = {k: 1 for k in nodes}

    def unite(self, x, y):
        """
        x が属する木と y が属する木を併合
        :param x:
        :param y:
        """
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        # rank が小さい方が下
        if self._ranks[x] > self._ranks[y]:
            # x が root
            self._parents[y] = x
            self._sizes[x] += self._sizes[y]
        else:
            # y が root
            self._parents[x] = y
            self._sizes[y] += self._sizes[x]
            if self._ranks[x] == self._ranks[y]:
                self._ranks[y] += 1

    def root(self, x):
        """
        x が属する木の root
        :param x:
        """
        if self._parents[x] == x:
            return x
        self._parents[x] = self.root(self._parents[x])
        return self._parents[x]

    def size(self, x):
        """
        x が属する木のノード数
        :param x:
        """
        return self._sizes[self.root(x)]

def argsort(li, key=None, reverse=False):
    return [i for _, i in sorted(
        [(a, i) for i, a in enumerate(li)], key=(lambda t: key(t[0])) if key else None, reverse=reverse
    )]

N, M = list(map(int, sys.stdin.buffer.readline().split()))
A, B = list(zip(*[map(int, sys.stdin.buffer.readline().split()) for _ in range(N)]))
VU = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]

# from libs.debug import plot_graph
#
# plot_graph(VU)

graph = [[] for _ in range(N)]
for v, u in VU:
    v -= 1
    u -= 1
    graph[v].append(u)
    graph[u].append(v)

reqs = [max(a, b) for a, b in zip(A, B)]
uses = list(B)

idx = argsort([a - b for a, b in zip(A, B)])
uf = UnionFind(size=N)
seen = [False] * N
ans = [INF] * N
for v in idx:
    seen[v] = True
    roots = set()
    for u in graph[v]:
        if not seen[u]:
            continue
        roots.add(uf.root(u))

    use_all = uses[v]
    for r in roots:
        use_all += uses[r]

    # v が最後
    req_v = reqs[v] + use_all - uses[v]
    for r in roots:
        req_v = min(req_v, max(reqs[r], reqs[v] - uses[v]) + use_all - uses[r])

    for r in roots:
        uf.unite(v, r)
    reqs[uf.root(v)] = req_v
    uses[uf.root(v)] = use_all
ans = reqs[uf.root(0)]
print(ans)