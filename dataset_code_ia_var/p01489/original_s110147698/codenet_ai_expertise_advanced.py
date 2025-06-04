import sys
from functools import lru_cache

readline = sys.stdin.readline
write = sys.stdout.write

def fibonacci(n, m):
    def mat_mult(a, b):
        return (
            (a[0]*b[0] + a[1]*b[2]) % m, (a[0]*b[1] + a[1]*b[3]) % m,
            (a[2]*b[0] + a[3]*b[2]) % m, (a[2]*b[1] + a[3]*b[3]) % m
        )

    def mat_pow(mat, exp):
        res = (1, 0, 0, 1)
        while exp:
            if exp & 1:
                res = mat_mult(res, mat)
            mat = mat_mult(mat, mat)
            exp >>= 1
        return res

    if n == 0:
        return 0
    mat = mat_pow((1, 1, 1, 0), n - 1)
    return mat[0]

def solve():
    MOD = 10**9 + 7
    K = int(readline())
    k0 = int(((1 + 4 * K) ** 0.5 - 1) // 2)
    if k0 * (k0 + 1) == K:
        k0 -= 1
    kk = k0 * (k0 + 1)
    delta = K - kk
    if delta > k0 + 1:
        m0 = 2 * k0 + 1
        b = delta - k0 - 2
    else:
        m0 = 2 * k0
        b = delta - 1
    if b < (k0 // 2 + 1):
        v = (fibonacci(2 + 2 * b, MOD) * fibonacci(m0 + 2 - 2 * b, MOD)) % MOD
    else:
        b1 = k0 + 1 - b - 1
        v = (fibonacci(3 + 2 * b1, MOD) * fibonacci(m0 + 1 - 2 * b1, MOD)) % MOD
    write(f"{v}\n")

solve()