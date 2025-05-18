def C(n, r):
    global MOD
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD
    

K = int(input())
S = input()
N = len(S)

MOD = 10 ** 9 + 7
ans = 0

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, K + N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

for i in range(0, K + 1):
    ans += C(i + N - 1, N - 1) * pow(25, i, MOD) * pow(26, K - i, MOD)
    ans %= MOD
print(ans)