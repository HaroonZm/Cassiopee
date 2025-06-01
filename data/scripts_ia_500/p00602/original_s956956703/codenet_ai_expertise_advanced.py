import sys
sys.setrecursionlimit(10**7)
MOD = 1001

class UnionFind:
    __slots__ = ('parents',)

    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        parents = self.parents
        while parents[x] >= 0:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def unite(self, x, y):
        parents = self.parents
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if parents[x] > parents[y]:
            x, y = y, x
        parents[x] += parents[y]
        parents[y] = x

    def group_count(self):
        return sum(p < 0 for p in self.parents)

def solve(V, d, fib):
    uf = UnionFind(V)
    f = fib[:V]
    for i in range(V):
        fi = f[i]
        for j in range(i + 1, V):
            if abs(fi - f[j]) < d:
                uf.unite(i, j)
    print(uf.group_count())

def main():
    input = sys.stdin.readline
    fib = [2, 3]
    for _ in range(2, 1005):
        fib.append((fib[-1] + fib[-2]) % MOD)

    while True:
        line = input()
        if not line:
            break
        Vd = line.split()
        if len(Vd) < 2:
            break
        V, d = map(int, Vd)
        solve(V, d, fib)

if __name__ == '__main__':
    main()