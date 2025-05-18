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

class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = []
        for i in range(2, int(math.sqrt(m)) + 1):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i*i,m,i):
                a[j] = False

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    def sowa(self, n):
        r = 1
        for k,v in self.division(n):
            t = 1
            for i in range(1,v+1):
                t += math.pow(k, i)
            r *= t
        return r

def main():
    rr = []
    pr = Prime(10**12)
    dc = collections.defaultdict(lambda: inf)
    dc[(0,0)] = 1
    cd = [(inf,inf), (0,0)]
    ti = 2
    for i in range(1, 1000):
        si = i
        sj = i
        i2 = i*2
        for k in range(i2):
            si -= 1
            t = (si, sj)
            dc[t] = ti
            cd.append(t)
            ti += 1
        for k in range(i2):
            sj -= 1
            t = (si, sj)
            dc[t] = ti
            cd.append(t)
            ti += 1
        for k in range(i2):
            si += 1
            t = (si, sj)
            dc[t] = ti
            cd.append(t)
            ti += 1
        for k in range(i2):
            sj += 1
            t = (si, sj)
            dc[t] = ti
            cd.append(t)
            ti += 1
        if ti > 10**6:
            break

    def f(m, n):
        fm = {}
        def ff(k):
            if k in fm:
                return fm[k]
            dk = dc[k]
            if dk > m:
                fm[k] = (0, 0)
                return (0, 0)

            cm = (0, 0)
            for i in range(-1, 2):
                ct = ff((k[0]+1, k[1]+i))
                if cm < ct:
                    cm = ct
            if pr.is_prime(dk):
                if cm[0] == 0:
                    fm[k] = (1, dk)
                else:
                    fm[k] = (cm[0]+1, cm[1])
            else:
                fm[k] = cm
            return fm[k]

        r = ff(cd[n])
        return ' '.join(map(str, r))

    while True:
        m,n = LI()
        if m == 0 and n == 0:
            break
        rr.append(f(m,n))

    return '\n'.join(map(str, rr))

print(main())