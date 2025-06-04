import sys
sys.setrecursionlimit(100000)

class UnionFind:
    def __init__(self, n):
        super().__init__()
        self.par = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            return self.root(self.par[x])

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            elif self.rank[x] > self.rank[y]:
                self.par[y] = x
            else:
                self.par[x] = y
                self.rank[y] += 1

def distance(cell1, cell2):
    c_dis = 0
    for i in range(3):
        c_dis += (cell1[i] - cell2[i]) ** 2
    c_dis = c_dis ** 0.5 - (cell1[3] + cell2[3])
    if c_dis > 0:
        return c_dis
    else:
        return 0

while True:
    n = int(input())
    if n == 0:
        break
    union = UnionFind(n)
    cell_list = [list(map(float, input().split())) for _ in range(n)]
    distance_list = []
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(cell_list[i], cell_list[j])
            distance_list.append([d, i, j])
    distance_list.sort()
    total_dis = 0
    for dis in distance_list:
        if not union.is_same(dis[1], dis[2]):
            union.unite(dis[1], dis[2])
            total_dis += dis[0]
    print(format(total_dis, ".3f"))