from functools import reduce
from operator import mul

M = 998244353

def mat_mult(a, b):
    return [ (a[0]*b[0] + a[1]*b[2]) % M, (a[0]*b[1] + a[1]*b[3]) % M,
             (a[2]*b[0] + a[3]*b[2]) % M, (a[2]*b[1] + a[3]*b[3]) % M ]

def mat_pow(mat, exp):
    res = [1, 0, 0, 1]
    while exp:
        if exp & 1:
            res = mat_mult(res, mat)
        mat = mat_mult(mat, mat)
        exp >>= 1
    return res

def f(n):
    # Optimized using matrix exponentiation
    return mat_pow([1, 1, 1, 0], n)[1]

def precompute_inv(n):
    # Fermat's little theorem for inverse factorial, vectorized
    inv = [1] * (n+1)
    for i in range(2, n+1):
        inv[i] = ((M - M // i) * inv[M % i]) % M
    return inv

n, m = map(int, input().split())
r, c = f(m + 2 * n - 2), 1
I = precompute_inv(n)
for i in range(n-1):
    r = (r + c * (M - f(2 * n - 2 - 2 * i))) % M
    c = c * (m + i) % M * I[i+1] % M
print(r)