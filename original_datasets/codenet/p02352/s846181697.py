import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

class RangeAddMin():
    def __init__(self, n):
        i = 1
        while 2**i <= n:
            i += 1
        self.N = 2**i
        self.A = [0] * (self.N*2)
        self.B = [0] * (self.N*2)

    def add(self, a, b, x, k, l, r):
        def ina(k, l, r):
            if b <= l or r <= a:
                pass
            elif a <= l and r <= b:
                self.A[k] += x
            else:
                m = (l+r) // 2
                ina(k*2+1, l, m)
                ina(k*2+2, m, r)
                self.B[k] = min(self.B[k*2+1] + self.A[k*2+1], self.B[k*2+2] + self.A[k*2+2])

        ina(k, l, r)

    def query(self, a, b, k, l, r):
        def inq(k, l, r):
            if b <= l or r <= a:
                return inf

            if a <= l and r <= b:
                return self.A[k] + self.B[k]

            m = (l+r) // 2
            rl = inq(k*2+1, l, m)
            rr = inq(k*2+2, m, r)
            return min(rl, rr) + self.A[k]

        return inq(k, l, r)

def main():
    n,q = LI()
    qa = [LI() for _ in range(q)]

    ram = RangeAddMin(n)
    rr = []
    for qi in qa:
        s = qi[1]
        t = qi[2] + 1
        if qi[0] == 0:
            x = qi[3]
            ram.add(s, t, x, 0, 0, n)
        else:
            rr.append(ram.query(s, t, 0, 0, n))

        # print(qi,ras.A,ras.B)

    return JA(rr, "\n")

# start = time.time()
print(main())
# pe(time.time() - start)