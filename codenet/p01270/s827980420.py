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

def main():
    rr = []

    def f(n):
        ss = [[int(c) if i > 0 else c for c,i in zip(LS(),range(3))] for _ in range(n)]
        r = []
        a = [(0, -1)]
        ds = set()
        for s in ss:
            if s[0] == 'R':
                bi = bisect.bisect_left(a, (s[1], inf))
                t = a[bi-1][1]
                if t in ds:
                    t = -1
                r.append(t)
            elif s[0] == 'W':
                i = s[1]
                c = s[2]
                ai = 0
                al = len(a)
                while c > 0:
                    if a[ai][1] >= 0 and a[ai][1] not in ds:
                        ai += 1
                        continue
                    if ai == al - 1:
                        a[-1:] = [(a[ai][0], i), (a[ai][0]+c, -1)]
                        break
                    aic = a[ai+1][0] - a[ai][0]
                    if aic <= c:
                        a[ai] = (a[ai][0], i)
                        c -= aic
                    else:
                        a[ai:ai+1] = [(a[ai][0], i), (a[ai][0]+c, -1)]
                        break
            else: # 'D'
                ds.add(s[1])
        return r

    while True:
        n = I()
        if n == 0:
            break
        rr.extend(f(n))
        # print(rr[-1])
        rr.append('')

    return '\n'.join(map(str, rr))

print(main())