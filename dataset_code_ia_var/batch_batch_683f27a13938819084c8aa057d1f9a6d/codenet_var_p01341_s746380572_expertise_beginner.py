import sys

sys.setrecursionlimit(10000000)

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_zero_indexed():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def calc_distance_squared(a, b):
    # a and b are lists or tuples of size 2
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.parent[x_root] <= self.parent[y_root]:
            self.parent[x_root] += self.parent[y_root]
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] += self.parent[x_root]
            self.parent[x_root] = y_root
        return True

def main():
    results = []
    while True:
        nm = read_int_list()
        n = nm[0]
        m = nm[1]
        if n == 0 and m == 0:
            break
        points = []
        for _ in range(n):
            points.append(read_int_list())
        edges = []
        for _ in range(m):
            a, b = read_int_list_zero_indexed()
            d2 = calc_distance_squared(points[a], points[b])
            edges.append([d2, a, b])
        edges.sort(reverse=True)
        answer = 0.0
        uf = UnionFind(n)
        for d2, a, b in edges:
            if uf.union(a, b):
                continue
            answer += d2 ** 0.5
        results.append("{:.3f}".format(answer))
        break
    return "\n".join(results)

print(main())