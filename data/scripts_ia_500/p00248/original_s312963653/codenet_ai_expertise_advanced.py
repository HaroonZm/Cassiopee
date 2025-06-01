class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True

def main():
    import sys
    input = sys.stdin.readline
    while (line := input().strip()):
        n, m = map(int, line.split())
        if n == 0:
            break
        uf = UnionFind(n)
        degrees = [0]*n
        flag = False
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            degrees[u] += 1
            degrees[v] += 1
            if not uf.union(u, v):
                flag = True
        print("no" if flag or max(degrees) > 2 else "yes")
        
if __name__ == '__main__':
    main()