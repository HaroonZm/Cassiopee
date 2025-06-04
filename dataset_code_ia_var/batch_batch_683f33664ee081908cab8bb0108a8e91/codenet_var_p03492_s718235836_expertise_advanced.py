import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_order

sys.setrecursionlimit(1 << 20)
MOD = 10 ** 9 + 7

def input(): return sys.stdin.readline()
def ints(): return map(int, sys.stdin.buffer.read().split())

N, *XY = map(int, sys.stdin.buffer.read().split())
edges = np.array(XY, dtype=np.int64).reshape(-1, 2)
adj = csr_matrix(
    (np.ones(len(edges), dtype=np.int8), (edges[:, 0], edges[:, 1])),
    shape=(N + 1, N + 1))
adj = adj + adj.T

dfs_order, par = depth_first_order(adj, 1, directed=False)
subtree_size = np.ones(N + 1, dtype=np.int32)
is_cent = np.ones(N + 1, dtype=bool)

for v in reversed(dfs_order.tolist()):
    if subtree_size[v] < (N + 1) // 2:
        is_cent[v] = False
    if par[v] < 0:
        continue
    if subtree_size[v] > N // 2:
        is_cent[par[v]] = False
    subtree_size[par[v]] += subtree_size[v]

centroids = np.flatnonzero(is_cent[1:]) + 1
if len(centroids) == 1:
    c = centroids[0]
    sizes = [N - subtree_size[c]] + [subtree_size[v] for v in range(1, N + 1) if par[v] == c]
else:
    sizes = [N // 2, N // 2]

def cumprod_optimized(arr, mod):
    arr = np.array(arr, dtype=np.int64)
    n = len(arr)
    res = np.ones(n, dtype=np.int64)
    acc = 1
    for i in range(n):
        acc = (acc * arr[i]) % mod
        res[i] = acc
    return res

def make_fact(U, mod):
    fact = np.arange(U, dtype=np.int64)
    fact[0] = 1
    fact = cumprod_optimized(fact, mod)
    fact_inv = np.empty(U, dtype=np.int64)
    fact_inv[-1] = pow(int(fact[-1]), mod - 2, mod)
    for i in range(U - 2, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % mod
    return fact, fact_inv

fact, fact_inv = make_fact(N + 100, MOD)

def component_array(n):
    res = (fact[n] * fact_inv[n::-1] % MOD) ** 2 % MOD
    res = (res * fact_inv[:n + 1]) % MOD
    res[1::2] = (-res[1::2]) % MOD
    return res

def convolve_fft(a, b):
    la, lb = len(a), len(b)
    n = 1 << (la + lb - 2).bit_length()
    A = np.fft.fft(a, n)
    B = np.fft.fft(b, n)
    C = A * B
    res = np.fft.ifft(C).real.round().astype(np.int64)[:la + lb - 1] % MOD
    return res

x = np.array([1], dtype=np.int64)
for s in sizes:
    x = convolve_fft(x, component_array(s))

result = (x * fact[N:0:-1] % MOD).sum() if len(centroids) == 1 else (x * fact[N::-1] % MOD).sum()
print(int(result % MOD))