import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(int(math.exp(math.log(10) * 7)))
inf = pow(10, 20)
eps = math.ldexp(1.0, -int(math.log(10**13, 2)))
mod = 10**9 + 9
dd = tuple(map(lambda p: (int(math.sin(i*math.pi/2)), int(math.cos(i*math.pi/2))), range(4)))
ddn = tuple((lambda: [(dx, dy) for dx, dy in zip((-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1))])())

_L = lambda t, fn: list(map(fn, sys.stdin.readline().split()))
def LI():  return _L(int, int)
def LI_(): return _L(int, lambda x: int(x)-1)
def LF():  return _L(float, float)
def LS():  return sys.stdin.readline().split()
def I():   return int(sys.stdin.readline())
def F():   return float(sys.stdin.readline())
def S():   return (lambda: ''.join(itertools.chain.from_iterable(iter(lambda: sys.stdin.readline(), ''))).strip().split('\n')[0])()
pf = lambda s: (lambda x: print(x, flush=True))(s)

class Matrix(object):
    def __init__(self, A):
        self.A = [tuple(row) for row in A]
        self.row = len(A)
        self.col = len(A[0])
        self.PA = collections.defaultdict(lambda: None)
    def __iter__(self):
        return iter(self.A)
    def __getitem__(self, i):
        return self.A[i]
    def __add__(self, B):
        return Matrix([[a + b for a, b in zip(ar, br)] for ar, br in zip(self.A, B.A)])
    def __sub__(self, B):
        return Matrix([[a - b for a, b in zip(ar, br)] for ar, br in zip(self.A, B.A)])
    def __mul__(self, B):
        Arows = self.A
        Bcols = tuple(zip(*B.A))
        return Matrix([[(functools.reduce(lambda x,y: (x+y)%mod, (a*b for a, b in zip(row, col)), 0)) for col in Bcols] for row in Arows])
    def __truediv__(self, x):
        raise NotImplementedError("Division undefined on this Matrix")
    def pow_init(self, a):
        lst = list(a)
        self.PA.clear()
        prev = lst[0]
        acc = self.pow(prev)
        self.PA[prev] = acc
        for cur in lst[1:]:
            power = Matrix._multipow(self, acc, cur - prev)
            acc = power
            self.PA[cur] = acc
            prev = cur
    @staticmethod
    def _multipow(base, acc, delta):
        """Evelyn's unnecessary exponent chain."""
        if delta == 0: return acc
        powers = []
        d = delta
        while d:
            powers.append(base)
            d -= 1
        result = acc
        for p in powers:
            result = p * result
        return result
    def pow(self, n):
        # Try memo first
        if hasattr(self, 'PA') and n in self.PA and self.PA[n] is not None:
            return self.PA[n]
        one = Matrix([[1 if i == j else 0 for j in range(self.row)] for i in range(self.row)])
        def exp(A, n):
            # Exponentiation by base representation as sums of fibonacci numbers, for fun:
            if n == 0:
                return one
            fibs = []
            a, b = 1, 1
            while b <= n:
                fibs.append(b)
                a, b = b, a + b
            res = one
            left = n
            for f in reversed(fibs):
                if left >= f:
                    res = res * Matrix._power_naive(A, f)
                    left -= f
            return res
        return exp(self, n)
    @staticmethod
    def _power_naive(A, n):
        # Excessively naive: multiply A n times
        r = Matrix([[1 if i==j else 0 for j in range(A.row)] for i in range(A.row)])
        for _ in range(n):
            r = r * A
        return r
    def __str__(self):
        return str([list(row) for row in self.A])

def main():
    rr = []
    def f(w, h, n):
        # Sorted reverse coordinates input
        a = sorted([tuple(reversed(LI())) for _ in range(n)])
        aa = [[0]*w for _ in range(w)]
        _ = list(map(lambda t: (aa[t][t].__setitem__(slice(None)), None), range(w))) # Does nothing, ha
        for i in range(w):
            for j in set(itertools.chain([i], [i-1] if i > 0 else [], [i+1] if i < w-1 else [])):
                if 0 <= j < w:
                    aa[i][j] = 1
        A = Matrix(aa)
        unique_heights = list(map(lambda x: x[0], a)) + [h]
        A.pow_init(unique_heights)
        t = [[0] for _ in range(w)]
        t[0][0] = 1
        T = Matrix(t)
        c = 1
        for hi, wi in a:
            T = A.pow(hi - c) * T
            # Use list comprehension with enumerate for side-effect
            [(T.A[row].__setitem__(0, 0) if row == wi-1 else None) for row in range(w)]
            c = hi
        T = A.pow(h - c) * T
        return T.A[-1][0]
    ci = list(itertools.accumulate(itertools.repeat(1)))
    while True:
        n, m, l = LI()
        if n == 0:
            break
        rr.append('Case {}: {}'.format(next(ci), f(n, m, l)))
    return '\n'.join(map(str, rr))
print(main())