import sys

class UnionFind:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        for i in range(size):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    n, w, h = map(int, input().split())
    uf = UnionFind(n)
    x_map = {}
    y_map = {}
    edge_slime = False

    for i in range(n):
        line = sys.stdin.readline()
        x, y = map(int, line.split())
        if x == 1 or x == w:
            edge_slime = True
        if y == 1 or y == h:
            edge_slime = True

        if x in x_map:
            uf.unite(x_map[x], i)
        else:
            x_map[x] = i
        if y in y_map:
            uf.unite(y_map[y], i)
        else:
            y_map[y] = i

    roots = set()
    for i in range(n):
        roots.add(uf.find(i))

    if len(roots) == 1:
        print(n - 1)
    else:
        ans = n - len(roots)
        if edge_slime:
            ans += len(roots) - 1
        else:
            ans += len(roots)
        print(ans)

if __name__ == '__main__':
    main()