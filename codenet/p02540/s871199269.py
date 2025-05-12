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

from sys import stdin
input = stdin.buffer.readline

def main():
    n = int(input())

    l = [0] * n
    for i in range(n):
        x, y = map(int, input().split())
        l[x-1] = (y-1, i)

    uf = UnionFind(n)
    roots = []

    for y, i in l:
        if len(roots) == 0 or roots[-1][0] > y:
            roots.append((y, i))
        else:
            new_y = roots[-1][0]
            while len(roots) > 0 and roots[-1][0] < y:
                old_y, old_i = roots.pop()
                uf.union(i, old_i)
            roots.append((new_y, i))

    # O(uf.size(i)) = 1
    for i in range(n):
        print(uf.size(i))

main()