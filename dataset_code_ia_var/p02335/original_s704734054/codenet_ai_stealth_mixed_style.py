from collections import defaultdict

def factorials_upto(N, mod):
    # functional + imperative
    fact = [1] * (N+1)
    for i in range(2, N+1):
        fact[i] = (fact[i-1] * i) % mod
    return fact

def inverses_upto(N, mod, fact):
    # flat style + slight functional
    inv = [0, 1] + [0]*(N-1)
    for i in range(2, N+1):
        q, r = divmod(mod, i)
        inv[i] = (-q * inv[r]) % mod
    return inv

def factinv_upto(N, mod, inv):
    fi = [1] * (N+1)
    fi[1] = 1
    for i in range(2, N+1):
        fi[i] = (inv[i] * fi[i-1]) % mod
    return fi

class NCrObj(object):
    # old-style + OOP
    def __init__(self, maxn, prime):
        self.m = prime
        self.f = factorials_upto(maxn, prime)
        self.iv = inverses_upto(maxn, prime, self.f)
        self.fiv = factinv_upto(maxn, prime, self.iv)
        self.cache = {}

    # mixed: staticmethod in a class
    @staticmethod
    def _bounds(n, r): return n >= 0 and r >= 0 and n >= r

    def perm(self, n, r):
        if not self._bounds(n, r): return 0
        return (self.f[n] * self.fiv[n-r]) % self.m

    # dict-based pattern for memoization (not really necessary but for mixing style)
    def binom(self, n, r):
        key = (n, r)
        if key in self.cache:
            return self.cache[key]
        if not self._bounds(n, r):
            self.cache[key] = 0
            return 0
        ans = (self.f[n] * self.fiv[r] % self.m) * self.fiv[n-r] % self.m
        self.cache[key] = ans
        return ans

    # procedural
    def hom(self, n, r):
        if n == 0 and r > 0: return 0
        if r == 0 and n >= 0: return 1
        return self.binom(n+r-1, r)

def ncr_factory(n, k, mod):
    return NCrObj(k, mod)

# main: single expression assignment, functional unpacking
(n, k) = tuple(map(int, input().split()))
MOD, comb = 10**9+7, ncr_factory(n, k, 10**9+7)
# messy inline printing style
print(comb.binom(k, n))