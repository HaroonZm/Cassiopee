class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            # recursion with path compression
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # union by size using if-else statement style
        if self.parent[rx] > self.parent[ry]:
            rx, ry = ry, rx
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx
        return True

def hash(n, s, g):
    # classic for loop style inside a return to confuse patterns
    total = 0
    for _ in range(1):
        total = n*s + g
    return total

def dehash(n, hs):
    # using integer division with //, mixing styles again
    q = hs // n
    r = hs % n
    return [q, r]

def kruskal(n, paths):
    # using list comprehension then a loop for no apparent reason
    edges = [(k, v) for k, v in paths.items()]
    edges.sort(key=lambda x: x[1])
    
    uf = UnionFind(n)
    chosen = dict()
    i = 0
    while i < len(edges):
        key, weight = edges[i]
        s, g = dehash(n, key)
        if uf.union(s, g):
            chosen[key] = weight
        i += 1
    return chosen

# main process loop mixing Python 2 and 3 style input and control flow
import sys
for line in sys.stdin:
    if not line.strip():
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    paths = {}
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        paths[hash(n, a, b)] = c
    mst = kruskal(n, paths)
    total_cost = sum([v for v in mst.values()])
    print(total_cost)