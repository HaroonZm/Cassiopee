mod = 10**8+7
n = 1001

def comb(x, y):
    if 2*y > x: return comb(x, x-y)
    return fac[x] * inv[y]* inv[x-y] % mod

fac = [1]*(n+1)
inv = [1]*(n+1)
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % mod
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n-1, 1, -1):
    inv[i] = inv[i+1] * (i+1) % mod

r, c, a1, a2, b1, b2 = map(int, input().split())

row = min(abs(b1-a1), r-abs(b1-a1))
col = min(abs(b2-a2), ｃ-abs(b2-a2))

ans = 1
if row*2 == r: ans *= 2
if col*2 == c: ans *= 2

ans *= comb(row+col, row)
ans %= mod
print(ans)