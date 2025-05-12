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

def main():
    rr = []

    def f(n,m):
        ee = [LI() + [_] for _ in range(m)]
        e = sorted(ee, key=lambda x: [x[2], x[3]])
        s = []
        ns = []
        uf = UnionFind(n+1)
        t = 0
        ttc = 0
        for a,b,c,i in e:
            if uf.union(a,b):
                s.append(i)
                t += c
                ttc += 1
            else:
                ns.append((a,b,c))

        r = 0
        rc = 0
        for si in s:
            tr = 0
            tc = 0
            uf = UnionFind(n+1)
            w = ee[si][2]
            for sj in s:
                if si == sj:
                    continue
                uf.union(ee[sj][0],ee[sj][1])
            sf = True
            for a,b,c in ns:
                if c == w and uf.union(a,b):
                    sf = False
                    break
            if sf:
                rc += 1
                r += w

        return '{} {}'.format(rc, r)

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        break

    return '\n'.join(map(str,rr))

print(main())