class Tree():
    def __init__(self, n, edge):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - 1].append(e[1] - 1)
            self.tree[e[1] - 1].append(e[0] - 1)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        self.size = [1 for _ in range(self.n)]
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)
        for node in self.order[::-1]:
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                self.size[node] += self.size[adj]

    def heavylight_decomposition(self):
        self.order = [None for _ in range(self.n)]
        self.head = [None for _ in range(self.n)]
        self.head[self.root] = self.root
        self.next = [None for _ in range(self.n)]
        stack = [self.root]
        order = 0
        while stack:
            node = stack.pop()
            self.order[node] = order
            order += 1
            maxsize = 0
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                if maxsize < self.size[adj]:
                    maxsize = self.size[adj]
                    self.next[node] = adj
            for adj in self.tree[node]:
                if self.parent[node] == adj or self.next[node] == adj:
                    continue
                self.head[adj] = adj
                stack.append(adj)
            if self.next[node] is not None:
                self.head[self.next[node]] = self.head[node]
                stack.append(self.next[node])

    def range_hld(self, u, v, edge=False):
        res = []
        while True:
            if self.order[u] > self.order[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                res.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.parent[self.head[v]]
            else:
                res.append((self.order[u] + edge, self.order[v] + 1))
                return res

    def subtree_hld(self, u):
        return self.order[u], self.order[u] + self.size[u]

    def lca_hld(self, u, v):
        while True:
            if self.order[u] > self.order[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                v = self.parent[self.head[v]]
            else:
                return u

class BinaryIndexedTree():  #1-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def sum(self, idx):
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def add(self, idx, x):
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx & -idx

    def bisect_left(self, x):
        if x <= 0: return 0
        res, tmp = 0, 2**((self.n).bit_length() - 1)
        while tmp:
            if res + tmp <= self.n and self.tree[res + tmp] < x:
                x -= self.tree[res + tmp]
                res += tmp
            tmp >>= 1
        return res + 1

class RAQandRSQ():
    def __init__(self, n):
        self.bit1 = BinaryIndexedTree(n)
        self.bit2 = BinaryIndexedTree(n)

    def add(self, lt, rt, x):
        self.bit1.add(lt, -x * (lt - 1))
        self.bit1.add(rt, x * (rt - 1))
        self.bit2.add(lt, x)
        self.bit2.add(rt, -x)

    def sum(self, lt, rt):
        rsum = self.bit2.sum(rt - 1) * (rt - 1) + self.bit1.sum(rt - 1)
        lsum = self.bit2.sum(lt - 1) * (lt - 1) + self.bit1.sum(lt - 1)
        return rsum - lsum

import sys
input = sys.stdin.readline

from operator import add

N = int(input())
E = []

for i in range(N):
    k, *c = map(int, input().split())
    for j in range(k):
        E.append((i + 1, c[j] + 1))

t = Tree(N, E)
t.setroot(0)
t.heavylight_decomposition()

r = RAQandRSQ(N)

res = []

Q = int(input())

for _ in range(Q):
    q, *p = map(int, input().split())
    if q == 0:
        v, w = p
        for lt, rt in t.range_hld(0, v, edge=True):
            r.add(lt, rt, w)
    else:
        s = 0
        u, = p
        for lt, rt in t.range_hld(0, u, edge=True):
            s += r.sum(lt, rt)
        res.append(s)

print('\n'.join(map(str, res)))