import sys
sys.setrecursionlimit(10**6 + 1)  # Just in case!

class UnionFindTree:  # Disjoint set structure, not the most beautiful name but ok
    # Some union-find voodoo (was confused at first, but seems to work)
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # parents
        self.rank = [0 for _ in range(n)]  # depths, all zero to start

    def find(self, x):
        # with path compression (pretty classic, but not obvious actually)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        if X == Y:
            return
        if self.rank[X] < self.rank[Y]:
            self.parent[X] = Y
        else:
            self.parent[Y] = X
            if self.rank[X] == self.rank[Y]:
                self.rank[X] += 1  # rank increase, kinda awkward sometimes

    def same(self, x, y):
        return self.find(x) == self.find(y)

while True:
    line = input().strip()
    if not line:
        continue  # empty lines sometimes, dunno why
    NQ = list(map(int, line.split()))
    if len(NQ) != 2:
        continue  # defensive (I've regretted not doing this before)
    N, Q = NQ
    if N == 0 and Q == 0:
        break
    # sometimes people use 1-based, correcting
    parents = [0]
    for _ in range(N - 1):
        p = int(input())
        parents.append(p - 1)

    queries = []
    marked = set()
    for _ in range(Q):
        parts = input().split()
        if not parts: continue  # hmm
        k = parts[0]
        v = int(parts[1])-1
        if k == "Q":
            queries.append((k, v))
        elif k == "M":
            if v not in marked:
                marked.add(v)
                queries.append((k, v))

    uf = UnionFindTree(N)
    for i in range(1, N):
        if i not in marked:
            pr = uf.find(parents[i])  # get parent root
            uf.parent[i] = pr
            # rank thing - unsure if correct
            uf.rank[pr] = max(uf.rank[pr], uf.parent[i]+1)

    ans = 0
    for t in reversed(queries):
        k, v = t
        if k == "Q":
            # 1-based for output (annoying)
            ans += uf.find(v) + 1
        else:
            if not uf.same(v, parents[v]):
                p = uf.find(parents[v])
                uf.parent[v] = p
                uf.rank[p] = max(uf.rank[p], uf.parent[v]+1)
    print(ans)