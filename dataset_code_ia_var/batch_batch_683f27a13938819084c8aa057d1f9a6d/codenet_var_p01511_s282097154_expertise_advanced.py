import sys
import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import random
import time
import copy
from functools import lru_cache, reduce, partial

sys.setrecursionlimit(1 << 25)
inf = float('inf')
eps = 1e-13
mod = 10 ** 9 + 9
dd = [(-1,0), (0,1), (1,0), (0,-1)]
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x - 1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip('\n')
def pf(s): print(s, flush=True)

from operator import add, sub

class Matrix:
    __slots__ = ('A', 'row', 'col', 'PA')

    def __init__(self, A):
        self.A = tuple(tuple(x) for x in A)
        self.row = len(A)
        self.col = len(A[0])
        self.PA = {}

    def __iter__(self):
        yield from self.A

    def __getitem__(self, i):
        return self.A[i]

    def __add__(self, B):
        return Matrix([[a + b for a, b in zip(ra, rb)] for ra, rb in zip(self.A, B.A)])

    def __sub__(self, B):
        return Matrix([[a - b for a, b in zip(ra, rb)] for ra, rb in zip(self.A, B.A)])

    def __mul__(self, B):
        # Strassen optimization not needed for small w, but listcomp at C-speed + zip
        # Also support vector * matrix (for initial T * A)
        if isinstance(B, Matrix):
            # Pretranspose B for cache locality
            B2 = tuple(zip(*B.A))
            res = []
            for row in self.A:
                res.append([sum((x * y for x, y in zip(row, col))) % mod for col in B2])
            return Matrix(res)
        else:
            raise TypeError("Unsupported multiplication")

    def __truediv__(self, x):
        raise NotImplementedError("Division not supported for Matrix")

    def pow_init(self, a_seq):
        # Precompute required powers
        pa = self.PA
        base = a_seq[0]
        pa[base] = self.pow(base)
        curr = base
        for nxt in a_seq[1:]:
            diff = nxt - curr
            pa[nxt] = pa[curr] * self.pow(diff)
            curr = nxt

    def pow(self, n):
        # Matrix fast exponentiation with PA cache usage
        try:
            return self.PA[n]
        except (AttributeError, KeyError):
            pass
        m, rows = self, self.row
        r = Matrix([[int(i==j) for j in range(rows)] for i in range(rows)])
        e = n
        while e > 0:
            if e & 1:
                r = r * m
            m = m * m
            e >>= 1
        return r

    def __str__(self):
        return '\n'.join(map(str, self.A))

def main():
    results = []
    ci = 1

    def f(w, h, n):
        blocked = sorted([LI()[::-1] for _ in range(n)])
        mat_base = [[0]*w for _ in range(w)]
        for i in range(w):
            for j in (i-1, i, i+1):
                if 0 <= j < w:
                    mat_base[i][j] = 1
        A = Matrix(mat_base)
        A.pow_init([b[0] for b in blocked] + [h])
        T = Matrix([[1 if i == 0 else 0] for i in range(w)])
        curr_h = 1
        for hi, wi in blocked:
            T = A.pow(hi-curr_h) * T
            # Block cell wi-1 (input is 1-based)
            T.A = tuple(tuple(0 if idx == wi-1 else val for idx, val in enumerate(row)) if c == 0 else row for c, row in enumerate(T.A))
            curr_h = hi
        T = A.pow(h-curr_h) * T
        return T.A[-1][0]

    while True:
        n, m, l = LI()
        if n == 0:
            break
        results.append(f'Case {ci}: {f(n, m, l)}')
        ci += 1

    return '\n'.join(results)

if __name__ == '__main__':
    print(main())