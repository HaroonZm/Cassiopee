import sys
from functools import cache
from itertools import product

sys.setrecursionlimit(1 << 25)
INF = float('inf')

input = lambda: sys.stdin.buffer.readline().rstrip()

class ModInt(int):
    __slots__ = ()
    MOD = 10 ** 9 + 7

    def __new__(cls, x):
        return int.__new__(cls, x % cls.MOD)

    def __add__(self, other):
        return ModInt(int(self) + int(other))

    def __sub__(self, other):
        return ModInt(int(self) - int(other))

    def __mul__(self, other):
        return ModInt(int(self) * int(other))

    def __truediv__(self, other):
        return ModInt(int(self) * pow(int(other), self.MOD - 2, self.MOD))

    def __pow__(self, other, modulo=None):
        return ModInt(pow(int(self), int(other), self.MOD))

    __radd__ = __add__
    __rsub__ = lambda self, other: ModInt(int(other) - int(self))
    __rmul__ = __mul__
    __rtruediv__ = lambda self, other: ModInt(int(other) * pow(int(self), self.MOD - 2, self.MOD))
    __rpow__ = lambda self, other: ModInt(pow(int(other), int(self), self.MOD))
    def __repr__(self):
        return str(int(self))

def resolve():
    L, R = map(int, input().split())
    D = 61
    dp = [[[[ModInt(0) for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(D + 1)]
    dp[D][0][0][0] = ModInt(1)
    rng = (0, 1)
    for d in range(D-1, -1, -1):
        lb = (L >> d) & 1
        rb = (R >> d) & 1
        for i, j, m, x, y in product(rng, repeat=5):
            if x > y: continue
            if not (i or lb <= x): continue
            if not (j or y <= rb): continue
            ni = i | (lb < x)
            nj = j | (y < rb)
            nm = m | (x & y)
            if not (m or x == y): continue
            dp[d][ni][nj][nm] += dp[d+1][i][j][m]
    print(sum(dp[0][i][j][m] for i, j, m in product(rng, repeat=3)))
resolve()