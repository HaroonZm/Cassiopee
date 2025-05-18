import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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

class Ruiwa():
    def __init__(self, a):
        self.H = h = len(a)
        self.W = w = len(a[0])
        self.R = r = a
        for i in range(h):
            for j in range(1,w):
                r[i][j] += r[i][j-1]

        for i in range(1,h):
            for j in range(w):
                r[i][j] += r[i-1][j]

    def search(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0

        r = self.R
        rr = r[y2][x2]
        if x1 > 0 and y1 > 0:
            return rr - r[y1-1][x2] - r[y2][x1-1] + r[y1-1][x1-1]
        if x1 > 0:
            rr -= r[y2][x1-1]
        if y1 > 0:
            rr -= r[y1-1][x2]

        return rr

def main():
    n,m = LI()
    na = [LI() for _ in range(n)]
    xd = set()
    yd = set()
    for x,y in na:
        xd.add(x)
        yd.add(y)

    xl = sorted(list(xd))
    yl = sorted(list(yd))
    xx = {}
    yy = {}
    for i in range(len(xl)):
        xx[xl[i]] = i
    for i in range(len(yl)):
        yy[yl[i]] = i
    a = [[0]*(len(yl)+1) for _ in range(len(xl)+1)]
    for x,y in na:
        a[xx[x]][yy[y]] += 1
    rui = Ruiwa(a)
    r = []
    for _ in range(m):
        x1,y1,x2,y2 = LI()
        xx1 = bisect.bisect_left(xl, x1)
        yy1 = bisect.bisect_left(yl, y1)
        xx2 = bisect.bisect(xl, x2) - 1
        yy2 = bisect.bisect(yl, y2) - 1
        r.append(rui.search(yy1,xx1,yy2,xx2))

    return '\n'.join(map(str,r))

print(main())