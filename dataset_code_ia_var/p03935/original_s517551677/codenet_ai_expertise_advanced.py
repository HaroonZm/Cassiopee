from functools import lru_cache
from operator import mul

M = 998244353

def mat_mult(a, b):
    return [
        (a[0]*b[0]+a[1]*b[2])%M, (a[0]*b[1]+a[1]*b[3])%M,
        (a[2]*b[0]+a[3]*b[2])%M, (a[2]*b[1]+a[3]*b[3])%M
    ]

@lru_cache(maxsize=None)
def f(n):
    res, mat = (1, 0, 0, 1), (1, 1, 1, 0)
    while n:
        if n & 1:
            res = mat_mult(res, mat)
        mat = mat_mult(mat, mat)
        n >>= 1
    return res[1]

def inv_list(n):
    inv = [1] * (n+1)
    for i in range(2, n+1):
        inv[i] = inv[M % i] * (M - M // i) % M
    return inv

n, m = map(int, raw_input().split())
inv = inv_list(n)
res = f(m + 2*n - 2)
c = 1
for i in range(n-1):
    res = (res + c * (M - f(2*n-2-2*i))) % M
    c = c * (m + i) % M * inv[i+1] % M

print(res)