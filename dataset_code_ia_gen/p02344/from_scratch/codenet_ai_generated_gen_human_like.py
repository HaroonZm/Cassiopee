import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.weight = [0] * n  # weight[i]: difference between i and its parent (val[parent[i]] - val[i])

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            px = self.find(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = px
            return px

    def weight_of(self, x):
        self.find(x)
        return self.weight[x]

    def unite(self, x, y, w):
        # w = val[y] - val[x]
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        # Union by size
        if self.parent[rx] > self.parent[ry]:
            rx, ry = ry, rx
            w = -w
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx
        # adjust weight: val[ry] + weight[ry] = val[rx] + ?
        self.weight[ry] = self.weight[x] - self.weight[y] + w

    def diff(self, x, y):
        # return val[y] - val[x]
        if self.find(x) != self.find(y):
            return None
        return self.weight[y] - self.weight[x]

n, q = map(int, input().split())
wuf = WeightedUnionFind(n)

for _ in range(q):
    line = input().split()
    if line[0] == '0':
        _, x, y, z = line
        x, y, z = int(x), int(y), int(z)
        wuf.unite(x, y, z)
    else:
        _, x, y = line
        x, y = int(x), int(y)
        res = wuf.diff(x, y)
        if res is None:
            print('?')
        else:
            print(res)