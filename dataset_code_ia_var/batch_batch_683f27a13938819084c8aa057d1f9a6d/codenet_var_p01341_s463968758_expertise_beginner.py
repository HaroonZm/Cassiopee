class UnionFind:
    def __init__(self, size):
        self.parent = [-1 for i in range(size)]

    def find(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.parent[x_root] < self.parent[y_root]:
                self.parent[x_root] += self.parent[y_root]
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] += self.parent[x_root]
                self.parent[x_root] = y_root

    def is_disjoint(self, x, y):
        return self.find(x) != self.find(y)

def solve():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    piles = []
    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        piles.append((x, y))
    fences = []
    for i in range(M):
        p, q = map(int, sys.stdin.readline().split())
        p -= 1
        q -= 1
        x1, y1 = piles[p]
        x2, y2 = piles[q]
        length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        fences.append((length, p, q))
    fences.sort(reverse=True)
    uf = UnionFind(N)
    answer = 0
    for length, p, q in fences:
        if uf.is_disjoint(p, q):
            uf.union(p, q)
        else:
            answer += length
    print(answer)

solve()