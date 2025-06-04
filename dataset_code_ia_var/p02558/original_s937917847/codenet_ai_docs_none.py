import sys

input = sys.stdin.buffer.readline

class UnionFindTree:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    N, Q = map(int, input().split())
    uft = UnionFindTree(N)
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t == 0:
            uft.unite(u, v)
        else:
            print(int(uft.is_same(u, v)))

if __name__ == "__main__":
    main()