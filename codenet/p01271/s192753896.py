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

    def f(w, h):
        w2 = w+2
        la = ['#' * w2]
        ra = ['#' * w2]
        ls = rs = None
        for i in range(1,h+1):
            lt, rt = LS()
            if 'L' in lt:
                ls = (i, lt.index('L') + 1)
            if 'R' in rt:
                rs = (i, rt.index('R') + 1)
            la.append('#' + lt + '#')
            ra.append('#' + rt + '#')
        la.append('#' * w2)
        ra.append('#' * w2)

        q = collections.deque([(ls[0], ls[1], rs[0], rs[1])])
        v = collections.defaultdict(bool)
        v[(ls[0], ls[1], rs[0], rs[1])] = 1
        while q:
            ly,lx,ry,rx = q.pop()
            for dy, dx in dd:
                lty = ly + dy
                ltx = lx + dx
                rty = ry + dy
                rtx = rx - dx
                if la[lty][ltx] == '#':
                    lty = ly
                    ltx = lx
                if ra[rty][rtx] == '#':
                    rty = ry
                    rtx = rx
                if v[(lty,ltx,rty,rtx)]:
                    continue
                v[(lty,ltx,rty,rtx)] = 1
                if la[lty][ltx] == '%' and ra[rty][rtx] == '%':
                    return 'Yes'
                if la[lty][ltx] != '%' and ra[rty][rtx] != '%':
                    q.append((lty,ltx,rty,rtx))

        return 'No'

    while True:
        w,h = LI()
        if w == 0 and h == 0:
            break
        rr.append(f(w,h))

    return '\n'.join(rr)

print(main())