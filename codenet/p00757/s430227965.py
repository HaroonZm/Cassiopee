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
        x2 -= 1
        y2 -= 1
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
    rr = []

    def f(h,w,s):
        a = [LI() for _ in range(h)]
        rui = Ruiwa(a)
        ss = rui.R[-1][-1] - s

        fm = {}
        def _f(x1,y1,x2,y2):
            key = (x1,y1,x2,y2)
            if key in fm:
                return fm[key]
            t = rui.search(x1,y1,x2,y2)
            if t < ss:
                fm[key] = (-1,-1)
                return (-1,-1)
            r = (1, t)
            for x in range(x1+1,x2):
                r1 = _f(x1,y1,x,y2)
                if r1[0] < 0:
                    continue
                r2 = _f(x,y1,x2,y2)
                if r2[0] < 0:
                    continue
                tr = (r1[0]+r2[0], min(r1[1], r2[1]))
                if r < tr:
                    r = tr
            for y in range(y1+1,y2):
                r1 = _f(x1,y,x2,y2)
                if r1[0] < 0:
                    continue
                r2 = _f(x1,y1,x2,y)
                if r2[0] < 0:
                    continue
                tr = (r1[0]+r2[0], min(r1[1], r2[1]))
                if r < tr:
                    r = tr
            fm[key] = r
            return r

        r,rs = _f(0,0,w,h)

        return '{} {}'.format(r, rs - ss)

    while 1:
        n,m,s = LI()
        if n == 0 and m == 0 and s == 0:
            break
        rr.append(f(n,m,s))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())