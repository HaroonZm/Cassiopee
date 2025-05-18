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

def main():
    rr = []

    d = collections.defaultdict(list)
    def kf(e):
        na = []
        for i in range(3):
            na.append(sorted([(e[j]-e[i])%60 for j in range(3)]))
        return tuple(min(na))

    for h in range(24):
        for m in range(60):
            for s in range(60):
                a = h * 5 + m // 12
                k = kf([a,m,s])
                d[k].append((h*3600+m*60+s))

    def to_time(i):
        h = i // 3600
        m = i // 60 % 60
        s = i % 60
        return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

    def f(n):
        a = [LI() for _ in range(n)]
        cs = [d[kf(a[i])] + [inf] for i in range(n)]
        mr = inf
        mi = -1
        for i in range(60*60*24):
            t = i
            for j in range(n):
                c = cs[j][bisect.bisect_left(cs[j], i)]
                if t < c:
                    t = c
            tr = t - i
            if mr > tr:
                mr = tr
                mi = i
        return '{} {}'.format(to_time(mi), to_time(mi+mr))

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))

print(main())