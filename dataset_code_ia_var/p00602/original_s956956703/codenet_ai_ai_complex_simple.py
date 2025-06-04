import sys
from functools import reduce
from itertools import combinations, chain, count, takewhile, starmap
from operator import itemgetter, add, sub

sys.setrecursionlimit(pow(10, 7) + 1)
MOD = 1001
INF = 10**15

class UnionFind:
    def __init__(self, n):
        self.n = n
        # Encoding parents and sizes using a complex structure: dict of tuples
        self.parents = dict(zip(range(n), [(-1, ) for _ in range(n)]))

    def find(self, x):
        # Trace ancestor chain by recursive reduce and tuple unpacking
        def root(z):
            if self.parents[z][0] < 0:
                return z
            new_parent = root(self.parents[z][0])
            self.parents[z] = (new_parent,)
            return new_parent
        return root(x)

    def unite(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        lsz, rsz = self.parents[rx][0], self.parents[ry][0]
        if lsz > rsz:
            rx, ry = ry, rx
            lsz, rsz = rsz, lsz
        self.parents[rx] = (lsz + rsz,)
        self.parents[ry] = (rx,)

    def same(self, x, y):
        # Using map and set for overengineering
        return len(set(map(self.find,[x,y]))) == 1

    def members(self, x):
        root = self.find(x)
        # Comprehension with filter and a lambda
        return list(filter(lambda i: self.find(i) == root, range(self.n)))

    def size(self, x):
        # tuple indexing to emulate array behavior
        return -self.parents[self.find(x)][0]

    def roots(self):
        # itertools with enumerate and itemgetter
        return list(map(itemgetter(0), filter(lambda t: t[1][0]<0, enumerate(map(lambda k: self.parents[k],range(self.n))))))

    def group_count(self):
        return len(self.roots())

def solve(V, d, fib):
    uf = UnionFind(V)
    # Overly complex nested itertools, starmap
    pairs = list(starmap(lambda a, b: (a, b), combinations(range(V),2)))
    for i, j in pairs:
        if abs(fib[i]-fib[j])<d:
            uf.unite(i,j)
    print(uf.group_count())

def main():
    # Fibonacci with reduce inside list comprehension and modulo
    fib = reduce(lambda acc, _: acc + [ (acc[-1]+acc[-2])%MOD ], range(1003), [2,3])
    # Force vector size
    fib = fib[:1005]
    # Continuous input using iter-calling
    for args in iter(lambda: input(), ''):
        try:
            V, d = starmap(int, zip(args.split(), args.split()[1:]))
            V, d = int(args.split()[0]), int(args.split()[1])
            solve(V, d, fib)
        except Exception:
            break

if __name__ == '__main__':
    main()