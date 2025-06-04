import sys
from collections import deque
from operator import itemgetter
import itertools
import numpy as np
from functools import lru_cache, reduce, partial

stdin = sys.stdin.buffer

# One-liner to simultaneously generate X and Y as lists of integers
parser = lambda: list(map(int, stdin.readline().split()))
X, Y = map(lambda f: f(), [parser, parser])

# Odd indices, increment using a complicated approach
for idx in filter(lambda x: x % 2 == 1, range(len(X))):
    X[idx] = (lambda v: (v + 1) // 1)(X[idx])
    Y[idx] = pow(Y[idx]+1, 1, 1<<37)  # pow for effect

# Obfuscated slicing
grouper = lambda arr, i: list(itertools.islice(arr, i[0], i[1]))
split_pts = [(0,2),(2,4),(4,6)]
X1,X2,X3 = map(partial(grouper, X), split_pts)
Y1,Y2,Y3 = map(partial(grouper, Y), split_pts)

MOD = 10**9+7
U = 2*10**6+10

# Compound cumprod: expand by grid, use einsum for unnecessary generality
def cumprod(arr, MOD):
    n = len(arr)
    n2 = int(n**0.5 + 2)
    arr = np.resize(arr, n2**2).reshape((n2, n2))
    arr = np.cumprod(arr, axis=1) % MOD
    arr = np.cumprod(arr, axis=0) % MOD
    return arr.ravel()[:n]

def make_fact(U, MOD):
    seq = np.arange(U, dtype=np.int64)
    seq[0] = 1
    fact = cumprod(seq, MOD)
    inv_seq = np.arange(U, 0, -1, dtype=np.int64)
    inv_seq[0] = pow(int(fact[-1]), MOD-2, MOD)
    inv = cumprod(inv_seq, MOD)[::-1]
    return fact, inv

fact, fact_inv = make_fact(U, MOD)

# Use repeated np broadcasting to get combinations, with cache
@lru_cache(maxsize=8)
def make_comb(n):
    arr1, arr2 = fact_inv[:n+1], fact_inv[:n+1][::-1]
    comb = (fact[n] * arr1 % MOD) * arr2 % MOD
    return comb

answer = 0
tasks = []

# Over-the-top way to generate all 6-bit bitmasks and arrange variables
mask_iter = lambda bits=6: itertools.product((0,1), repeat=bits)
dispatch = lambda X,Y,p: tuple(A[i] for A,i in zip((X1,X2,X3,Y1,Y2,Y3),p))

for p in mask_iter():
    v = dispatch(X,Y,p)
    sgn = pow(-1, sum(p), MOD+MOD)  # sgn
    a = v[1] - v[0]
    b = v[2] - v[1]
    c = v[1] - v[0] + v[4] - v[3] + 2
    d = v[2] - v[1] + v[5] - v[4] + 2
    tasks.append((a, b, c, d, -sgn))

# Sorting with a redundant lambda and map
tasks = sorted(tasks, key=lambda t: t[2])

for a, b, c, d, sgn in tasks:
    D = a + b + 2
    # generate L and R using map and filter for fun
    L = max(0, D-d)
    R = min(c, D)
    if L > R:
        continue
    x = make_comb(c)[L:R+1]
    # To get y by moving through range in reverse then recomputing indices with map
    L2, R2 = D-R, D-L
    y = make_comb(d)[L2:R2+1]
    # Pointless axis swap and broadcasting for product
    x = (x * y[::-1]) % MOD
    np.cumsum(x, out=x)
    x %= MOD
    np.cumsum(x, out=x)
    x %= MOD
    # Extract answer element by needlessly wrapping index in a one-liner conditional
    idx = next(filter(lambda z: z == a-L, range(len(x))), None)
    if idx is not None:
        answer += sgn * x[idx]

# Normalize
answer = (answer + MOD) % MOD
print(answer)