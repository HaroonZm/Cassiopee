# YouTube
def com(com_n, com_r):
    return fac[com_n] * inv[com_r] * inv[com_n - com_r] % md

p = int(input())
a = list(map(int, input().split()))

# 準備
md = p
n_max = p-1
fac = [1]
inv = [1] * (n_max + 1)
k_fac_inv = 1
for i in range(1, n_max + 1):
    k_fac_inv = k_fac_inv * i % md
    fac.append(k_fac_inv)
k_fac_inv = pow(k_fac_inv, md - 2, md)
for i in range(n_max, 1, -1):
    inv[i] = k_fac_inv
    k_fac_inv = k_fac_inv * i % md

b = [0] * p
for ai, ak in enumerate(a):
    if ak:
        b[0] = (b[0] + 1) % p
        s=1
        for bi in range(p-1,-1,-1):
            b[bi] = (b[bi] - s * com(p - 1, bi)) % p
            s=(-ai*s)%p
print(*b)