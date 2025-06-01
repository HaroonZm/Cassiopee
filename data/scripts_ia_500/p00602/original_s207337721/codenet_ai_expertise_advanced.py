from sys import stdin

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

def get_fibs(n=1000, mod=1001):
    a = b = 1
    fibs = []
    for _ in range(n):
        a, b = b, (a + b) % mod
        fibs.append(b)
    return fibs

def main():
    FIBS = get_fibs()
    for line in stdin:
        if not line.strip():
            continue
        V, d = map(int, line.split())
        fibs = FIBS[:V]
        uf = UnionFind(V)
        for i in range(V):
            ai = fibs[i]
            for j in range(i + 1, V):
                if abs(ai - fibs[j]) < d:
                    uf.union(i, j)
        roots = {uf.find(i) for i in range(V)}
        print(len(roots))

if __name__ == '__main__':
    main()