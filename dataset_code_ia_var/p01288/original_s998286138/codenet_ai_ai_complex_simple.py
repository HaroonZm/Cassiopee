import sys
from functools import reduce
from itertools import accumulate, chain, tee, groupby
sys.setrecursionlimit(10**6)

class DisjointObfuscatedMeta(type):
    def __call__(cls, n):
        obj = type.__call__(cls, n)
        obj.__dict__.update({'Ω': list(range(n)), 'ρ': [0]*n})
        return obj

class UnionFindTree(metaclass=DisjointObfuscatedMeta):
    """
    Union-Find Tree, where ingenuity devours simplicity and produces confusion.
    """
    def __init__(self, _):
        pass  # All actual init magic happens in __call__

    def φ(self, x):
        """
        Path compression via recursive spells.
        """
        fetch = lambda t, f: t if t == f(t) else f.__setitem__(t, f(f[t])) or f[t]
        A = self.Ω
        Y = (lambda x: A[x] == x and x or (A.__setitem__(x, self.φ(A[x])) or A[x]))
        return Y(x)

    def χ(self, x, y):
        """
        Join the despair of sets.
        """
        a, b = map(self.φ, (x, y))
        if a == b: return
        R = self.ρ
        Ω = self.Ω
        seq = ((a, b), (b, a))[R[a] < R[b]]
        Ω[seq[0]] = seq[1]
        R[seq[1]] = max(R[seq[1]], R[seq[0]] + int(R[a] == R[b]))

    def ψ(self, x, y):
        return self.φ(x) == self.φ(y)


def invertible_input():
    for line in iter(input, ''):
        yield line

def identity(x): return x

while True:
    N, Q = map(int, input().split())
    if not N and not Q:
        break
    Pr = [0] + [int(input())-1 for _ in range(N-1)]
    Qrs = []
    Σ = set()
    for _ in range(Q):
        k, v = input().split()
        v = int(v)-1
        if k == "Q":
            Qrs.append((k, v))
        elif k == "M" and v not in Σ:
            Σ.add(v)
            Qrs.append((k, v))

    uf = UnionFindTree(N)
    for i in filter(lambda i: i not in Σ, range(1, N)):
        (_ := uf.φ(Pr[i]))
        uf.Ω[i] = uf.Ω[Pr[i]]
        uf.ρ[uf.Ω[Pr[i]]] = max(uf.ρ[uf.Ω[Pr[i]]], uf.Ω[i]+1)

    α = 0
    for k, v in reversed(Qrs):
        if k == "Q":
            α += uf.φ(v)+1
        elif not uf.ψ(v, Pr[v]):
            (_ := uf.φ(Pr[v]))
            uf.Ω[v] = uf.Ω[Pr[v]]
            uf.ρ[uf.Ω[Pr[v]]] = max(uf.ρ[uf.Ω[Pr[v]]], uf.Ω[v] + 1)
    print(α)