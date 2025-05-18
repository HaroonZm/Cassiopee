class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = list(range(N))

    def root(self, x):
        path_to_root = []
        while self.parent[x] != x:
            path_to_root.append(x)
            x = self.parent[x]
        for node in path_to_root:
            self.parent[node] = x  # パス圧縮
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        self.parent[self.root(x)] = self.root(y)

    def __str__(self):
        groups = {}
        for x in range(self.N):
            root = self.root(x)
            if root in groups.keys():
                groups[root].append(x)
            else:
                groups[root] = [x]
        result = ""
        for root in groups.keys():
            result += str(groups[root]) + "\n"
        return result

n, q = map(int, input().split())
u = UnionFind(n)
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        u.unite(x, y)
    else:
        if u.same(x, y):
            print(1)
        else:
            print(0)