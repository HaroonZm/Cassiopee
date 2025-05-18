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

class Matrix():
    def __init__(self, A):
        self.A = A
        self.row = len(A)
        self.col = len(A[0])

    def __iter__(self):
        return self.A.__iter__()

    def __getitem__(self, i):
        return self.A.__getitem__(i)

    def __add__(self, B):
        aa = self.A
        bb = B.A
        return Matrix([[aa[i][j] + bb[i][j] for j in range(self.col)] for i in range(self.row)])

    def __sub__(self, B):
        aa = self.A
        bb = B.A
        return Matrix([[aa[i][j] - bb[i][j] for j in range(self.col)] for i in range(self.row)])

    def __mul__(self, B):
        bb = [[B.A[j][i] for j in range(B.row)] for i in range(B.col)]
        return Matrix([[sum([ak * bk for ak,bk in zip(ai,bj)]) % mod for bj in bb] for ai in self.A])

    def __truediv__(self, x):
        pass

    def pow_init(self, a):
        self.PA = pa = {}
        t = self.pow(a[0])
        c = a[0]
        pa[c] = t
        for d in a[1:]:
            t = t * self.pow(d-c)
            pa[d] = t
            c = d

    def pow(self, n):
        if n in self.PA:
            return self.PA[n]
        A = self
        r = Matrix([[0 if j != i else 1 for j in range(self.row)] for i in range(self.row)])
        while n > 0:
            if n % 2 == 1:
                r = r * A
            A = A * A
            n //= 2
        return r

    def __str__(self):
        return self.A.__str__()

def main():
    rr = []

    def f(w,h,n):
        a = sorted([LI()[::-1] for _ in range(n)])
        aa = [[0]*w for _ in range(w)]
        for i in range(w):
            ai = aa[i]
            ai[i] = 1
            if i > 0:
                ai[i-1] = 1
            if i < w-1:
                ai[i+1] = 1
        A = Matrix(aa)
        A.pow_init(list(map(lambda x: x[0], a)) + [h])
        t = [[0] for _ in range(w)]
        t[0][0] = 1
        T = Matrix(t)
        c = 1
        for hi,wi in a:
            T = A.pow(hi-c) * T
            T.A[wi-1][0] = 0
            c = hi
        T = A.pow(h-c) * T
        return T.A[-1][0]

    ci = 0
    while 1:
        ci += 1
        n,m,l = LI()
        if n == 0:
            break
        rr.append('Case {}: {}'.format(ci, f(n,m,l)))

    return '\n'.join(map(str, rr))

print(main())