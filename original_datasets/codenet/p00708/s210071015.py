import sys
import copy
import heapq
from collections import deque
import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize

# ===CODE===
def main():
    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def calc_dist(x1, y1, z1, r1, x2, y2, z2, r2):
        tmp = ((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2 + (float(z1) - float(z2)) ** 2) ** (1 / 2)
        tmp = max(0, tmp - float(r1) - float(r2))
        return tmp

    while True:
        n = int(input())
        if n == 0:
            exit(0)
        tree = UnionFind(n)

        data = [input().split() for i in range(n)]

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((calc_dist(data[i][0], data[i][1], data[i][2], data[i][3], data[j][0], data[j][1],
                                        data[j][2], data[j][3]), i, j))

        edges.sort()

        ans = 0
        for d, s, t in edges:
            if not tree.same(s, t):
                tree.union(s, t)
                ans += d

        print("{:.3f}".format(ans))

# ===main===
if __name__ == '__main__':
    main()