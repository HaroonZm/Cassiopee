class UnionFind:
    def __init__(self, n):
        self.parent = []
        self.size = []
        for i in range(n+1):
            self.parent.append(i)
            self.size.append(1)

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            self.parent[ra] = rb
            self.size[rb] += self.size[ra]
        else:
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]

def update(group, value):
    if counts[group] == 0 or value > maximum[group]:
        counts[group] = 1
        maximum[group] = value
    elif value == maximum[group]:
        counts[group] += 1

while True:
    n = int(input())
    if n == 0:
        break
    uf = UnionFind(n)
    fs = []
    for i in range(n):
        row = input().split()
        a = int(row[0])
        f1 = int(row[1])
        b = int(row[2])
        f2 = int(row[3])
        fs.append([f1, f2])
        uf.unite(i, a)
        uf.unite(i, b)
    counts = []
    maximum = []
    for _ in range(n):
        counts.append(0)
        maximum.append(0)
    for i in range(n):
        group = uf.find(i)
        update(group, fs[i][0])
        update(group, fs[i][1])
    answer = 1
    for i in range(n):
        if counts[i] > 0:
            answer = (answer * (counts[i] // 2)) % 10007
    print(answer)