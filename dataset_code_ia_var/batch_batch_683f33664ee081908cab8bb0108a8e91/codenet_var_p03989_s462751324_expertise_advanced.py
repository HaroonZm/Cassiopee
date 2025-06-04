import sys
import numpy as np
from functools import cache

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(1 << 24)

MOD = 924844033

def cumprod(arr, mod):
    l = arr.size
    sq = int(np.sqrt(l)) + 1
    arr2 = np.resize(arr, sq * sq).reshape(sq, sq)
    np.multiply.accumulate(arr2, axis=1, out=arr2)
    arr2 %= mod
    np.multiply.accumulate(arr2, axis=0, out=arr2)
    arr2 %= mod
    return arr2.ravel()[:l]

def make_fact(U, mod):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, mod)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), mod - 2, mod)
    fact_inv = cumprod(x, mod)[::-1]
    return fact, fact_inv

N, K = map(int, readline().split())

dp = np.zeros((3, N + 1, N + 1), dtype=np.int64)
dp[:, 0, 0] = 1

for n in range(1, N + 1):
    # Take from right
    dp[1, n, 1:] = (dp[1, n, 1:] + dp[1, n - 1, :-1]) % MOD
    dp[2, n, 1:] = (dp[2, n, 1:] + dp[2, n - 1, :-1]) % MOD
    # Take from left
    if n >= 2:
        dp[0, n, 1:] = (dp[0, n, 1:] + dp[0, n - 1, :-1]) % MOD
        dp[1, n, 1:] = (dp[1, n, 1:] + dp[0, n - 1, :-1]) % MOD
    dp[2, n, 1:] = (dp[2, n, 1:] + dp[1, n - 1, :-1]) % MOD
    # Skipping last
    dp[0, n] = (dp[0, n] + dp[1, n - 1]) % MOD
    dp[1, n] = (dp[1, n] + dp[1, n - 1]) % MOD
    dp[2, n] = (dp[2, n] + dp[2, n - 1]) % MOD

def F(N, K, n):
    items = (N - n) // (2 * K) + 1
    last = n + (items - 1) * 2 * K
    x = int(n - K > 0) + int(last + K <= N)
    arr = dp[x]
    return arr[items, :items + 1]

def convolve(x, y):
    if x.size < y.size:
        x, y = y, x
    Lx, Ly = x.size, y.size
    res = np.zeros(Lx + Ly - 1, dtype=np.int64)
    for i in range(Ly):
        res[i:i + Lx] = (res[i:i + Lx] + y[i] * x) % MOD
    return res

x = np.array([1], dtype=np.int64)
for n in range(1, 2 * K + 1):
    if n > N: break
    x = convolve(x, F(N, K, n))

fact, _ = make_fact(N + x.size + 10, MOD)
if x.size > 1:
    x[1::2] = -x[1::2] % MOD
else:
    x = x % MOD
idx = np.arange(N - x.size + 1, N + 1)
np.mod(idx, fact.size, out=idx)
tmp = (x[::-1] * fact[idx]) % MOD
print(int(np.sum(tmp) % MOD))