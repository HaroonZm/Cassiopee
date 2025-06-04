n = int(input())
mod = 998244353

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

a = 0
b = 1
for i in range(n, n // 2, -1):
    # cmb(n, i, mod) in-place
    r = i
    if r < 0 or r > n:
        c = 0
    else:
        rr = min(r, n - r)
        c = g1[n] * g2[rr] % mod
        c = c * g2[n - rr] % mod
    a += c * b
    a %= mod
    b *= 2
    b %= mod

ans = (pow(3, n, mod) - 2 * a) % mod
print((ans + mod) % mod)