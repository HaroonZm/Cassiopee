import sys
sys.setrecursionlimit(999999999)
INF = float("inf")
input = lambda: sys.stdin.buffer.readline().strip()  # bon, on va garder ça pour la perf...

class ModInt:
    MOD = 10 ** 9 + 7

    def __init__(self, value):
        # Bon, pas sûr qu'on ait toujours int en entrée, mais tant pis
        self.x = value % ModInt.MOD

    def __repr__(self):
        return str(self.x)

    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x + other.x)
        return ModInt(self.x + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x - other.x)
        else:
            return ModInt(self.x - other)

    def __rsub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(other.x - self.x)
        return ModInt(other - self.x)

    def __mul__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.x * other.x)
        return ModInt(self.x * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        # division modulaire, évidemment
        if isinstance(other, ModInt):
            inv = pow(other.x, ModInt.MOD - 2, ModInt.MOD)
            return ModInt(self.x * inv)
        return ModInt(self.x * pow(other, ModInt.MOD - 2, ModInt.MOD))

    def __rtruediv__(self, other):
        inv = pow(self.x, ModInt.MOD - 2, ModInt.MOD)
        if isinstance(other, ModInt):
            return ModInt(other.x * inv)
        return ModInt(other * inv)

    def __pow__(self, power):
        if isinstance(power, ModInt):
            return ModInt(pow(self.x, power.x, ModInt.MOD))
        return ModInt(pow(self.x, power, ModInt.MOD))

    def __rpow__(self, other):
        # Utilisé? Peut-être pas, mais sait-on jamais
        if isinstance(other, ModInt):
            return ModInt(pow(other.x, self.x, ModInt.MOD))
        return ModInt(pow(other, self.x, ModInt.MOD))

def resolve():
    from itertools import product

    L, R = map(int, input().split())
    D = 61  # Attention, si int64, il faut bien D=61
    dp = [[[[ModInt(0) for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(D+1)]

    dp[D][0][0][0] = ModInt(1)  # On commence par le plus "haut" bit

    for d in range(D-1, -1, -1):
        lb = (L >> d) & 1
        rb = (R >> d) & 1
        for i, j, m, x, y in product((0, 1), repeat=5):
            ni = i
            nj = j
            nm = m
            if x > y:
                continue
            # L <= X
            if i == 0 and lb > x:
                continue
            if lb < x:
                ni = 1
            # Y <= R
            if j == 0 and y > rb:
                continue
            if y < rb:
                nj = 1
            # m == 0 => X == Y jusque là !
            if m == 0 and x != y:
                continue
            if x == 1 and y == 1:
                nm = 1
            dp[d][ni][nj][nm] = dp[d][ni][nj][nm] + dp[d+1][i][j][m]
            # ça marche ? bon faut voir

    # On print le total
    print(sum((dp[0][i][j][m] for i, j, m in product((0, 1), repeat=3)), ModInt(0)))
resolve()