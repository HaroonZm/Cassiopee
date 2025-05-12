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

class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N

    def max_flow(self, s, t):
        r = 0
        e = self.E

        def f(c):
            v = self.v
            v[c] = 1
            if c == t:
                return 1
            for i in range(self.N):
                if v[i] == 0 and e[c][i] > 0 and f(i) > 0:
                    e[c][i] -= 1
                    e[i][c] += 1
                    return 1
            return 0

        while True:
            self.v = [0] * self.N
            if f(s) == 0:
                break
            r += 1

        return r

def main():
    rr = []

    def f(n,m):
        a = [LI_() for _ in range(m)]
        s,t = LI_()
        e = [[0]*n for _ in range(n)]
        for x,y in a:
            e[x][y] = 1
            e[y][x] = 1
        fl = Flow(e, n)
        r = fl.max_flow(s,t)
        re = []
        for i in range(m):
            x,y = a[i]
            if e[y][x] == 0:
                re.append(i+1)
        return [r,len(re)] + re

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.extend(f(n,m))
        # print('rr', rr[-1])
        break

    return '\n'.join(map(str,rr))

print(main())