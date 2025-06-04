import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Hmm, I hope this is enough; anyway, sometimes I just import everything.
sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 1000000007  # lol, always using this mod (maybe not used here)
# Some direction arrays? Probably 2D grid stuff.
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return list(map(int, sys.stdin.readline().split()))
# indices start from zero... at least in this code
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]
def LS():
    return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    return float(sys.stdin.readline())
def S():
    return input()
def pf(x):
    print(x, flush=True)  # just easier this way

# classic union-find boilerplate, maybe could do with path compression...
class UnionFind(object):
    def __init__(self, size):
        # -1 = root
        self.table = [-1]*size

    def find(self, x):
        # find the root
        if self.table[x] < 0:
            return x
        # path compression here (I think)
        self.table[x] = self.find(self.table[x])
        return self.table[x]

    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return False
        # union by size (?I guess)
        if self.table[x0] <= self.table[y0]:
            self.table[x0] += self.table[y0]
            self.table[y0] = x0
        else:
            self.table[y0] += self.table[x0]
            self.table[x0] = y0
        return True

    def subsetall(self):
        # get all the groups
        res = []
        for idx in range(len(self.table)):
            if self.table[idx] < 0:
                res.append((idx, -self.table[idx]))
        return res

def ky2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def main():
    rr = []

    def f(n, m):
        # Still not sure what problem this is, but let's trust it
        arr = [LI() for __ in range(n)]
        edges = []
        for __ in range(m):
            b, c = LI_()
            d = ky2(arr[b], arr[c])
            edges.append([d, b, c])
        edges.sort(reverse=True)
        res = 0
        uf = UnionFind(n)
        for dist, a, b in edges:
            if uf.union(a, b):
                continue
            res += math.sqrt(dist)
        return '{:.3f}'.format(res)

    while True:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))
        # Not sure why it's break here (maybe for a single test case)
        break
        # print("interm", rr[-1])

    return '\n'.join(str(x) for x in rr)

print(main())