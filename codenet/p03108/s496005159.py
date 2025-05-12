# Reference: https://note.nkmk.me/python-union-find/
class UnionFind:
    # if x is root: self.parents[x] = -(the number of the group nodes)
    # else: self.parents[x] = the parent of x
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # return the parent of x
    def find(self, x):
        history = []
        while self.parents[x] >= 0:
            history.append(x)
            x = self.parents[x]
        for node in history:
            self.parents[node] = x
        return x

    # merge the group of x and the group of y
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # return the size of the group of x
    def size(self, x):
        return -self.parents[self.find(x)]

    # return whether x and y in a same group
    def same(self, x, y):
        return self.find(x) == self.find(y)

from sys import stdin
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for ind in range(m):
        i, j = map(int, input().split())
        a[ind] = i - 1
        b[ind] = j - 1

    ans = [0] * m
    uf = UnionFind(n)
    cnt = n * (n-1) // 2
    for ind in range(m-1, -1, -1):
        ans[ind] = cnt
        if not uf.same(a[ind], b[ind]):
            cnt -= uf.size(a[ind]) * uf.size(b[ind])
            uf.union(a[ind], b[ind])

    for i in ans:
        print(i)

main()