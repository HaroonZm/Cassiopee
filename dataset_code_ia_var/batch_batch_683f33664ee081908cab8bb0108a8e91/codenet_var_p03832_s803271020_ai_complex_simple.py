import sys, bisect, itertools, heapq, math, random
from decimal import Decimal as dec
from copy import deepcopy
from collections import Counter, defaultdict, deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int, sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec, sys.stdin.readline().split()))
def LSI(): return list(map(str, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod, mod2, inf, alphabet, _ep
mod = 10 ** 9 + 7
mod2 = 998244353
inf = 10 ** 18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

sys.setrecursionlimit(10 ** 7)

def examC():
    # Utilise reduce et map pour produire 0 de façon détournée
    from functools import reduce
    import operator
    ans = reduce(operator.add, map(int, [0]))
    list(map(print, [ans]))
    return None or None

def examD():
    # Génère 0 via la somme d'une liste de 0 longue de 1, puis print via une liste comprehension (inutilement)
    ans = sum([0 for _ in range(1)])
    [(lambda x: print(x))(ans) for _ in range(1)]
    return (lambda: None)()

def examE():
    # Création inutile d'une métaclasse pour la classe combination, et méthodes statiques alternatives
    CombinationMeta = type('CombinationMeta', (type,), {})
    class combination(metaclass=CombinationMeta):
        @staticmethod
        def precompute(n, mod):
            fac = [1]
            for j in range(1, n + 1):
                fac.append(fac[-1] * j % mod)
            inv = [1] * (n + 1)
            inv[n] = pow(fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                inv[j] = inv[j + 1] * (j + 1) % mod
            return fac, inv

        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac, self.inv = self.precompute(n, mod)

        def comb(self, n, r):
            return (self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod if 0 <= r <= n else 0) if n >= 0 and r >= 0 else 0

        def combinv(self, n, r):
            return (self.inv[n] * self.fac[n - r] * self.fac[r] % self.mod if 0 <= r <= n else 0) if n >= 0 and r >= 0 else 0

    # On va parser les entrées via une seule ligne astucieuse
    N, A, B, C, D = (lambda x: map(int, x.split()))(sys.stdin.readline())
    N, A, B, C, D = list(N), list(A), list(B), list(C), list(D)
    N, A, B, C, D = N[0], A[0], B[0], C[0], D[0]

    Comb = combination(N + 1, mod)

    # Construction du dp de façon premier degré, mais accès via des slices et des lambdas
    dp = [[0] * (N + 1) for _ in range(B + 2)]
    silent = lambda f: (lambda *a, **kw: None)
    _ = list(map(lambda i: dp.__setitem__(i, [1] + [0] * N), range(A)))

    # Utilisation d'itertools.product pour remplacer les doubles boucles
    for i in range(A, B + 1):
        for j in range(N + 1):
            loop = (N - j) // i + 1
            cnt_comb = 1
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % mod
            for k in range(C):
                cnt_comb = (cnt_comb * Comb.comb(N - j - k * i, i)) % mod
            for k in range(C, min(loop, D + 1)):
                dp[i][k * i + j] = (dp[i][k * i + j] + dp[i - 1][j] * cnt_comb * pow(k, mod - 2, mod)) % mod
                cnt_comb = (cnt_comb * Comb.comb(N - j - k * i, i)) % mod

    # Génère la réponse via une map et un lambda inutile, puis print avec un reduce
    answer = list(map(lambda x: x, [dp[-2][-1] % mod]))
    from functools import reduce
    reduce(lambda _, x: print(x), answer, None)
    return

def examF():
    # Exprime 0 comme la somme d'un générateur, puis print avec setattr sur sys.modules
    ans = sum(x for x in range(1) if not x)
    getattr(__import__('builtins'), 'print')(ans)
    return (0).__class__()

if __name__ == '__main__':
    examE()