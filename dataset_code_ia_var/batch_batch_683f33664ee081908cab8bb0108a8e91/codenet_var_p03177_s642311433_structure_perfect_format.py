import sys

sys.setrecursionlimit(1 << 25)
readline = sys.stdin.buffer.readline
read = sys.stdin.readline  # 文字列読み込む時はこっち

import numpy as np
from functools import partial

array = partial(np.array, dtype=np.int64)
zeros = partial(np.zeros, dtype=np.int64)
full = partial(np.full, dtype=np.int64)

def ints():
    return np.fromstring(readline(), sep=' ', dtype=np.int64)

def read_matrix(H, W) -> np.ndarray:
    '''return np.ndarray shape=(H,W) matrix'''
    lines = []
    for _ in range(H):
        lines.append(read())
    lines = ' '.join(lines)  # byte同士の結合ができないのでreadlineでなくreadで
    return np.fromstring(lines, sep=' ', dtype=np.int64).reshape(H, W)

MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9

N, K = ints()
A = read_matrix(N, N)

def matmul_mod(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    MOD = 10**9 + 7
    ret = np.empty((X.shape[0], Y.shape[1]), dtype=np.int64)
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            tmp = (X[i, :] * Y[:, j]) % MOD
            ret[i, j] = tmp.sum() % MOD
    return ret

def matmul_mod_try(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    MOD = 10**9 + 7
    ret = np.empty((X.shape[0], Y.shape[1]), dtype=np.int64)
    YT = Y.T
    for i in range(X.shape[0]):
        Xi = X[i, :]
        tmp = (YT * Xi) % MOD
        ret[i, :] = tmp.sum(1) % MOD
    return ret

def matmul_mod_fast(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    MOD = 10**9 + 7
    X3d = X[:, :, np.newaxis].transpose(0, 2, 1)
    Y3d = Y[:, :, np.newaxis].transpose(2, 1, 0)
    return ((X3d * Y3d) % MOD).sum(2) % MOD

A_double = np.asanyarray(A, dtype=np.int64)
ans = np.eye(N, dtype=np.int64)
for j in range(int(K).bit_length()):
    if (K >> j) & 1:
        ans = matmul_mod_fast(ans, A_double)
    A_double = matmul_mod_fast(A_double, A_double)

print(ans.sum() % MOD)