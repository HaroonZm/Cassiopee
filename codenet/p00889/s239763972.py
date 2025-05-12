import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+9
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

    def f(n,s,w,q):
        g = s
        a = []
        for i in range(n):
            a.append(g // 7 % 10)
            if g % 2 == 1:
                g = (g // 2) ^ w
            else:
                g //= 2
        if q % 2 == 0 or q % 5 == 0:
            r = 0
            t = 0
            for c in a:
                if c > 0:
                    t += 1
                if c % q == 0:
                    r += t
            return r
        b = [0] * (n+1)
        k = 1
        for i in range(n-1,-1,-1):
            b[i] = (b[i+1] + a[i] * k) % q
            k = k * 10 % q
        d = collections.defaultdict(int)
        r = 0
        for i in range(n):
            if a[i] > 0:
                d[b[i]] += 1
            r += d[b[i+1]]

        return r

    while 1:
        n,m,l,o = LI()
        if n == 0:
            break
        rr.append(f(n,m,l,o))

    return '\n'.join(map(str, rr))

print(main())