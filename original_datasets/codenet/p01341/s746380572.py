import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

def ky2(a,b):
    return pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)

def main():
    rr = []

    def f(n,m):
        global fr
        a = [LI() for _ in range(n)]
        es = []
        for _ in range(m):
            b,c = LI_()
            es.append([ky2(a[b],a[c]), b, c])
        es.sort(reverse=True)
        r = 0
        uf = UnionFind(n)
        for k,b,c in es:
            if uf.union(b,c):
                continue
            r += pow(k,0.5)

        return '{:0.3f}'.format(r)

    while 1:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.append(f(n,m))
        break
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())