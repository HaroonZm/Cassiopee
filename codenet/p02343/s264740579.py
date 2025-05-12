class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, idx):
        if self.par[idx] == -1:
            return idx

        self.par[idx] = self.root(self.par[idx])
        return self.par[idx]

    def unite(self, idx1, idx2):
        idx1_par = self.root(idx1)
        idx2_par = self.root(idx2)

        if idx1_par == idx2_par:
            return

        if self.size[idx1_par] >= self.size[idx2_par]:
            self.size[idx1_par] += self.size[idx2_par]
            self.par[idx2_par] = idx1_par
        else:
            self.size[idx2_par] += self.size[idx1_par]
            self.par[idx1_par] = idx2_par

    def same(self, idx1, idx2):
        return self.root(idx1) == self.root(idx2)

n, q = map(int, input().split())

uf = UnionFind(n)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:  # unite
        uf.unite(x, y)
    else:  # same
        if uf.same(x, y):
            print(1)
        else:
            print(0)