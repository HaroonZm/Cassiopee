from functools import *
import sys
sys.setrecursionlimit(100000)

mod = 10**9+7

n, a, b = list(map(int, input().split(" ")))

r1 = min(a, n - a)
r2 = min(b, n - b)

# combination(n, r, mod)
res1 = 1
for i in range(r1):
    num = n - i
    den = i + 1

    # modinv(den, mod)
    a1 = den
    m1 = mod
    m0, x0, x1 = m1, 0, 1
    g1, a1_ = a1, m1
    while g1:
        q = a1_ // g1
        a1_, g1 = g1, a1_ % g1
        x0, x1 = x1 - q * x0, x0
    inv1 = x1 + m1 if x1 < 0 else x1
    if a1_ != 1:
        raise Exception('modular inverse does not exist')
    res1 = res1 * num * inv1 % mod

res2 = 1
for i in range(r2):
    num = n - i
    den = i + 1
    # modinv(den, mod)
    a2 = den
    m2 = mod
    m0, x0, x1 = m2, 0, 1
    g2, a2_ = a2, m2
    while g2:
        q = a2_ // g2
        a2_, g2 = g2, a2_ % g2
        x0, x1 = x1 - q * x0, x0
    inv2 = x1 + m2 if x1 < 0 else x1
    if a2_ != 1:
        raise Exception('modular inverse does not exist')
    res2 = res2 * num * inv2 % mod

# modpow(2, n, mod)
x = 2
y = n
z = mod
pow_res = 1
while y > 0:
    if y & 1:
        pow_res = pow_res * x % z
    x = x * x % z
    y >>= 1

c = res1 + res2

print((pow_res - c - 1) % mod)