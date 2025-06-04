import sys

def main():
    input = sys.stdin.readline

    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n

        def find(self, x):
            while self.parent[x] >= 0:
                if self.parent[self.parent[x]] >= 0:
                    self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, x, y):
            x_root = self.find(x)
            y_root = self.find(y)
            if x_root != y_root:
                if self.parent[x_root] > self.parent[y_root]:
                    x_root, y_root = y_root, x_root
                self.parent[x_root] += self.parent[y_root]
                self.parent[y_root] = x_root
            return x_root

    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((i, x, y))

    Y = []
    for i in range(N):
        Y.append(points[i][2])

    points.sort(key=lambda tup: tup[1])

    uf = UnionFind(N)
    stack = []
    for i, x, y in points:
        my = i
        while stack and Y[stack[-1]] < y:
            if Y[stack[-1]] < Y[my]:
                my = stack[-1]
            uf.union(stack.pop(), i)
        stack.append(my)

    ans = []
    for i in range(N):
        root = uf.find(i)
        ans.append(-uf.parent[root])

    for a in ans:
        print(a)

main()