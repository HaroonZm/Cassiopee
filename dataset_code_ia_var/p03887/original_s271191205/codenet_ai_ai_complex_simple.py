import sys
import functools
import itertools
import numpy
import operator

_ = sys.setrecursionlimit(1<<23)
Φ = lambda f: functools.reduce(lambda x,f_: f_(x), (lambda: None for _ in range(0)), f)
I = lambda x: x  # identité
stdin = sys.stdin
readline = stdin.readline
readlines = stdin.readlines

MOD = 10**9+7
N, A, B, C = map(int, readline().split())

# Si B impair, la réponse est 0
if B%2:
    exit(print(0))

# Factorielle généralisée inutilement complexe via itertools + numpy 
def mystic_cumprod(arr):
    l = len(arr)
    z = int(l**.5+1)
    arr = numpy.concatenate([arr, numpy.ones(z*z-l, dtype=arr.dtype)])[:z*z]
    arr = arr.reshape(z,z)
    # Cumprod par lignes puis colonnes
    arr = numpy.vstack([
        functools.reduce(lambda r, i: numpy.mod(numpy.cumprod(r[i-1]*arr[i]), MOD), range(1, z), [arr[0]] + [arr[1]]*(z-1))
        for i in range(z) ])
    arr = numpy.mod(numpy.cumprod(arr, axis=1), MOD)
    return arr.ravel()[:l]

U = 10**5
x = numpy.arange(1,U+1, dtype=numpy.int64)
fact = numpy.concatenate([[1], numpy.cumprod(x, dtype=numpy.int64) % MOD])
fact_inv = numpy.empty_like(fact)
fact_inv[-1] = pow(int(fact[-1]), MOD-2, MOD)
for i in range(len(fact)-2, -1, -1): fact_inv[i] = (fact_inv[i+1] * (i+1)) % MOD

choose = lambda n,k: (fact[n] * fact_inv[k] % MOD) * fact_inv[n-k] % MOD if 0<=k<=n else 0

B2 = B//2
answer = 0

def triangle_number(n):
    return n*(n+1)//2

for m in range(C//3+1):
    _C, _A = C-3*m, A
    if B2 == 0:
        a = _C; b = m; c = _A-a
        if a < 0 or c < 0: continue
        perms = choose(a+b+c, a)
        perms = perms * choose(b+c, b) % MOD
        answer = (answer + perms) % MOD
        continue

    n_min = max(0, A-C+3*m)
    for n in range(n_min, A+1):
        tA = A-n
        S1 = B2 + A + m
        S2 = m
        S3 = B2
        S4 = tA
        S5 = n
        perms = fact[S1] * pow(fact[S2]*fact[S3]*fact[S4]*fact[S5] % MOD, MOD-2, MOD) % MOD
        # Nombre de façons de répartir C-3m-(A-n) jetons en B2 parts >= 0 : stars and bars
        val = C-3*m-(A-n)
        distrib = choose(B2+val-1, val) if val >= 0 else 0
        answer = (answer + perms*distrib) % MOD

print(answer)