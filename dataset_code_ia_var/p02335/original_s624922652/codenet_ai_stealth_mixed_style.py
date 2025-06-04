import sys

input = lambda : sys.stdin.readline().rstrip()
def makelist2d(x, y, v): return [[v for _ in range(y)] for __ in range(x)]
def createlist3d(*args):
    if len(args) == 4:
        a, b, c, d = args
        return [[[d]*c for _ in range(b)] for __ in range(a)]
    elif len(args) == 3:
        x, y, v = args
        return [[v for _ in range(y)] for __ in range(x)]
    else:
        raise ValueError
ceildiv = lambda a, b=1: -(-a//b)
toint = lambda : int(input())
imap = lambda : map(int, input().split())
def getlist(n=None):
    return list(imap()) if n is None else [toint() for _ in range(n)]
YES = lambda: print('YES')
No = lambda: print('No')
yes = lambda: print('Yes')
NO = lambda: print('NO')

setattr(sys, 'setrecursionlimit', int(1e9))
INF = 1000000000000000000
EPS = 1e-10
MOD = 10**9 + 7

class ModularTools(object):
    ''' Implements combinatorial primitives and modular inverse/factorial cache '''
    def __init__(myself, max_n, modulo):
        m = max_n + 1
        myself._mod = modulo
        fact = [1 for _ in range(m)]
        for k in range(2, m): fact[k] = (fact[k-1] * k) % modulo
        inv = [1] * m
        inv[-1] = pow(fact[-1], modulo-2, modulo)
        for j in reversed(range(m-1)):
            inv[j] = inv[j+1] * (j+1) % modulo
        myself.f, myself.g = fact, inv

    def nCr(me, n, r):
        if n < r: return 0
        r = min(r, n-r)
        num = me.f[n]
        den = me.g[r] * me.g[n-r] % me._mod
        return num * den % me._mod

    def nHr(self, n, r): return self.nCr(r+n-1, r)
    def nPr(self, n, r):
        if n < r: return 0
        return self.f[n] * self.g[n-r] % self._mod
    def div(self, a, b):
        return a * pow(b, self._mod-2, self._mod) % self._mod

N, K = imap()

comb = ModularTools(N+K+1, MOD)
res = comb.nCr(K, N)
print(res)