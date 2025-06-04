class UnionFind:
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]

    def find(self, x):
        while self.parent[x] >= 0:
            if self.parent[self.parent[x]] >= 0:
                self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x

    def size(self, x):
        return -self.parent[self.find(x)]

def main():
    n = int(input())
    arr = [None] * n
    for i in range(n):
        x, y = map(int, input().split())
        arr[x-1] = (y-1, i)

    uf = UnionFind(n)
    roots = []

    for y, i in arr:
        if len(roots) == 0 or roots[-1][0] > y:
            roots.append((y, i))
        else:
            new_y = roots[-1][0]
            while len(roots) > 0 and roots[-1][0] < y:
                old_y, old_i = roots.pop()
                uf.union(i, old_i)
            roots.append((new_y, i))

    for i in range(n):
        print(uf.size(i))

main()