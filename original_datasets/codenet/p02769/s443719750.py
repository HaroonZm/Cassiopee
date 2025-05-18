n,k = map(int, input().split())
mod = 10 ** 9 + 7

comb0 = [1] * (n)

for i in range(n-1):
    comb0[i + 1] = comb0[i] * (n - i) * pow(i + 1,mod - 2, mod) % mod

comb1 = [1] * (n)

for i in range(n-1):
    comb1[i + 1] = comb1[i] * (n - 1 - i) * pow(i + 1,mod - 2, mod) % mod

ans = 0

for i in range(min(n - 1, k) + 1):
    ans += comb0[i] * comb1[i]
    ans %= mod

print(ans)