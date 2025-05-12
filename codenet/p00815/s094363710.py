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

    def f():
        a = LI()
        while a[-1] != 0:
            a += LI()
        r = [[]]
        c = 0
        nk = [a[0]]
        d = {}
        d[0] = 0
        for n in a[1:]:
            if n == 0:
                break
            while nk[d[c]] < 1:
                c -= 1

            if n < 0:
                dc = d[c]
                dn = d[c+n]
                r[dn].append(dc)
                r[dc].append(dn)
                nk[dn] -= 1
                nk[dc] -= 1
            else:
                nk.append(n-1)
                dc = d[c]
                ni = len(nk) - 1
                r[dc].append(ni)
                r.append([dc])
                nk[dc] -= 1
                c += 1
                d[c] = ni
        rr = []
        for i in range(len(nk)):
            rr.append('{} {}'.format(i+1, ' '.join(map(lambda x: str(x+1), sorted(r[i])))))
        return '\n'.join(rr)

    while 1:
        n = I()
        if n == 0:
            break
        rr = [f() for _ in range(n)]
        break

    return '\n'.join(map(str, rr))

print(main())