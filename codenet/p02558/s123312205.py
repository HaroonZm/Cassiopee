class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    N, Q = map(int, input().split())

    uni = UnionFind(N)
    for i in range(Q):
        t, u, v = map(int, input().split())
        if t == 0:
            uni.unite(u, v)
        else:
            if uni.same(u, v):
                print(1)
            else:
                print(0)

main()