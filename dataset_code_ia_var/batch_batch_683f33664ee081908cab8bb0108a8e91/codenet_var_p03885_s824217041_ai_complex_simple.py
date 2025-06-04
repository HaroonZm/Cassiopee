import sys
from itertools import accumulate, product, permutations, combinations
from operator import mul
import numpy as np

sys.setrecursionlimit(1<<20)
input = sys.stdin.readline
read_stack = lambda: list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
MOD = 10**9+7

N = int(input())
C = np.fromiter((int(c) for row in read_stack() for c in row), dtype=np.int8).reshape(N,N)

def ultra_rank(matrix):
    shape = matrix.shape
    indices = [range(shape[0]), range(shape[1])]
    def helper(A, row_ids, col_ids):
        if not row_ids or not col_ids:
            return 0
        col_0s = [i for i in row_ids if A[i, col_ids[0]]!=0]
        if not col_0s:
            return helper(A, row_ids, col_ids[1:])
        i = col_0s[0]
        perm_rows = [i] + [j for j in row_ids if j!=i]
        v = A[perm_rows[0],col_ids].copy()
        def new_row(row_idx):
            mult = A[row_idx, col_ids[0]]
            return np.bitwise_xor(A[row_idx,col_ids], v*mult)
        reduced = [new_row(j) for j in perm_rows[1:]]
        reduced = np.array(reduced)
        next_rows = list(range(reduced.shape[0]))
        next_cols = list(range(1, reduced.shape[1]))
        return 1 + helper(reduced, next_rows, next_cols)
    return helper(matrix.copy(), list(range(matrix.shape[0])), list(range(matrix.shape[1])))

r = ultra_rank(C)

pow2 = list(accumulate([1]*301, lambda x,_: x*2%MOD))
pow2[0]=1
for i in range(1,301):
    pow2[i] = pow2[i-1]*2%MOD

dp = np.zeros((301,301,301),dtype=np.int64)
dp[...,0,0] = 1
for M in range(1,301):
    dp[...,M,:M] += (dp[...,M-1,:M] * np.fromiter((pow2[j] for j in range(M)),np.int64))%MOD
    arr1 = dp[...,M-1,0:M]
    arr2 = pow2[:][:,None] - pow2[None,0:M]
    arr3 = (arr1 * arr2)%MOD
    dp[...,M,1:M+1] += arr3
    dp[...,M,:] %= MOD

x = 0
for n in range(r,N+1):
    q = dp[N,N,n]%MOD
    w = dp[N,n,r]%MOD
    e = pow(2,N*(N-n),MOD)
    x = (x + q * w % MOD * e % MOD)%MOD

def inv(a,mod): return pow(a,mod-2,mod)
print((x*inv(int(dp[N,N,r]),MOD))%MOD)