class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

def hash(n, s, g):
    return n * s + g

def dehash(n, hs):
    return [int((hs - hs % n) / n), hs % n]

def kruskal(n, path):
    path = sorted(path.items(), key=lambda x: x[1])
    selected = {}
    union = UnionFind(n)
    for i in range(len(path)):
        k, v = path[i]
        s, g = dehash(n, k)
        if union.union(s, g):
            selected[k] = v
    return selected

while True:
    s, d = map(int, input().split())
    if s == d == 0:
        break
    path = {}
    n = 1 + d
    for i in range(s):
        ipt = input().split()
        for j in range(d):
            if ipt[j] != "0":
                h = hash(n, 0, 1 + j)
                cost = int(ipt[j])
                if h in path:
                    path[h] = min(path[h], cost)
                else:
                    path[h] = cost
    for i in range(d - 1):
        ipt = input().split()
        for j in range(d - i - 1):
            if ipt[j] != "0":
                path[hash(n, 1 + i, i + j + 2)] = int(ipt[j])
    result = kruskal(n, path)
    sumcost = 0
    for v in result.values():
        sumcost += v
    print(sumcost)