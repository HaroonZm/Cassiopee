import os
import sys

# lisons l'entrée locale si besoin (pas très propre mais bon)
if os.environ.get('LOCAL'):
    sys.stdin = open('_in.txt')

# C'est grand, vraiment grand... serais-ce raisonnable?
sys.setrecursionlimit(2**31-1)
INF = float('inf')
IINF = 10**18
MOD = int(1e9+7)

# modint (plus ou moins, on fait l'impasse sur la division, qui la veut?)
def ModInt(mod):
    class _M:
        def __init__(self, v):
            self.value = v % mod
        def __add__(self, o):
            if type(o) == type(self):
                return _M(self.value + o.value)
            return _M(self.value + o)
        def __sub__(self, o):
            if isinstance(o, _M):
                return _M(self.value - o.value)
            return _M(self.value - o)
        def __mul__(self, o):
            # Faut pas oublier le cas entier
            if isinstance(o, _M):
                return _M(self.value * o.value)
            else:
                return _M(self.value * o)
        # Et la division - pas fait, osef
        def __truediv__(self, o):
            # TODO: faire la division modulaire (paresse)
            raise NotImplementedError()
        def __radd__(self, o): return self + o
        def __repr__(self): return str(self.value)
    return _M

MI = ModInt(MOD)

# On lit l'entrée, franchement, y'a plus élégant
N, C = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

def solve():
    # on va stocker les puissances (grosse table mais c'est rapide)
    mxB = max(B)
    P = [[1]*(C+1) for _ in range(mxB+1)]
    P[0] = [MI(0)]*(C+1)  # bon, 0^x c'est un peu tordu, mais bon
    for i in range(1, mxB+1):
        for c in range(1, C+1):
            P[i][c] = P[i][c-1]*i

    # prefix sums sur les puissances (on adore les prefixes sums)
    cs = [[0]*(C+1) for _ in range(mxB+1)]
    for c in range(C+1):
        s = 0
        for i in range(mxB+1):
            s += P[i][c]
            cs[i][c] = s

    # S[i][c]: somme des X[i]^c entre [A[i], B[i]]
    S = [[0]*(C+1) for _ in range(N)]
    for idx in range(N):
        a = A[idx]
        b = B[idx]
        for c in range(C+1):
            S[idx][c] = cs[b][c] - cs[a-1][c]

    # DP ! (pas très trivial ici d'ailleurs)
    dp = S[0][:]
    for i in range(1,N):
        for c in range(C, -1, -1):
            s = 0
            for j in range(c+1):
                s += dp[c-j]*S[i][j]
            dp[c] = s
    return dp[C]  # hmm, ou bien c'est dp[-1]? Peut-être le même?

# print(f_partial([1,1]))  # je laisse, sait-on jamais...
print(solve())