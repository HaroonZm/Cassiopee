mod = 10**9 + 7
fac = []
pw = []
fac.append(1 % mod)
pw.append(1 % mod)
for i in range(1, 1001):
    fac.append(fac[i-1]*i % mod)
for i in range(1, 1001):
    pw.append(pow(fac[i], mod-2, mod))
n, k = [int(s) for s in input().split()]
if n > k:
    print(0)
else:
    print(fac[k] * pw[k-n] % mod)