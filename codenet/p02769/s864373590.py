n, k = map(int, input().split())
mod = 10**9+7
m = min(n-1,k)
ans = 0

f = [1]
fi = [1]
for i in range(n):
    f.append(f[i]*(i+1) % mod)
    fi.append(pow(f[i+1], mod-2, mod))

def comb_mod(n, r, mod):
    return f[n] * fi[r] * fi[n-r] % mod

for m in range(m+1):
    ans += comb_mod(n, m, mod) * comb_mod(n-1, m, mod) % mod

print(ans%mod)