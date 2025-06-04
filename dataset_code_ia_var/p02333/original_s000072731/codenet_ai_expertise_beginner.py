import sys

mod = 1000000007

def comb(a, b):
    return fac[a] * inv[b] * inv[a-b] % mod

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

if n < k:
    print(0)
    sys.exit()

fac = [1] * (k+1)
for i in range(1, k+1):
    fac[i] = fac[i-1] * i % mod

inv = [0] * (k+1)
inv[k] = pow(fac[k], mod-2, mod)
for i in range(k, 0, -1):
    inv[i-1] = inv[i] * i % mod

ans = 0
for i in range(k+1):
    v = comb(k, i) * pow(k-i, n, mod) % mod
    if i % 2 == 0:
        ans = (ans + v) % mod
    else:
        ans = (ans - v) % mod
        if ans < 0:
            ans += mod
print(ans)