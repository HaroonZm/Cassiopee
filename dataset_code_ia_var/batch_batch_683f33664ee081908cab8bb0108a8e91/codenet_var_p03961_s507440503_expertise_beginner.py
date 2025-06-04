mod = 10**9+7

def mod_inv(a, mod):
    return pow(a, mod-2, mod)

def make_fac_inv(n, mod):
    fac = [1] * (n+1)
    inv = [1] * (n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % mod
    inv[n] = pow(fac[n], mod-2, mod)
    for i in range(n, 0, -1):
        inv[i-1] = inv[i] * i % mod
    return fac, inv

def bit_add(idx, val, bit):
    idx += 1
    while idx < len(bit):
        bit[idx] += val
        idx += idx & -idx

def bit_sum(idx, bit):
    idx += 1
    res = 0
    while idx > 0:
        res += bit[idx]
        idx -= idx & -idx
    return res

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

fac, inv = make_fac_inv(n+10, mod)
bit = [0] * (n+2)
used = [False] * (n+2)
zero_count = 0
rz = [0] * n

for i in range(n-1, -1, -1):
    if a[i]:
        used[a[i]] = True
    else:
        zero_count += 1
    rz[i] = zero_count

ans1 = 0
for i in range(n-1, -1, -1):
    if a[i]:
        cnt = bit_sum(a[i]-1, bit)
        ans1 = (ans1 + fac[n-1-i] * cnt) % mod
        bit_add(a[i], 1, bit)

mEX = [0] * (n+2) # mEX[x]=未登場(空き)数値でx以下何個ある
for x in range(1, n+1):
    mEX[x] = mEX[x-1] + (not used[x])

ans1 = ans1 * fac[zero_count] % mod

ans2 = 0
ans3 = 0
if zero_count:
    inv_zero = mod_inv(zero_count, mod)
else:
    inv_zero = 0

left_fac_sum = 0
for i in range(n):
    if a[i]:
        smaller_empty = mEX[a[i]-1]
        bigger_empty = mEX[n] - mEX[a[i]]
        ans2 += fac[zero_count] * smaller_empty % mod * rz[i] % mod * inv_zero % mod * fac[n-1-i] % mod
        ans2 += fac[zero_count] * bigger_empty % mod * inv_zero % mod * left_fac_sum % mod
        ans2 %= mod
    else:
        # (fac[n-1-i] * fac[zero_count] * (rz[i]-1) // 2) % mod
        ans3 += fac[n-1-i] * fac[zero_count] % mod * ((rz[i]-1) * mod_inv(2, mod) % mod) % mod
        left_fac_sum += fac[n-1-i]
        left_fac_sum %= mod

print(ans1, ans2, ans3, fac[zero_count], file=sys.stderr)
print((ans1+ans2+ans3+fac[zero_count])%mod)