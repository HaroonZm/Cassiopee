MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def comb(n, k):
    if k > n or k < 0:
        return 0
    return fact[n]*inv_fact[k]%MOD*inv_fact[n-k]%MOD

n, k = map(int, input().split())

if k > n:
    print(0)
    exit()

fact = [1]*(n+1)
inv_fact = [1]*(n+1)
for i in range(2, n+1):
    fact[i] = fact[i-1]*i % MOD
inv_fact[n] = modinv(fact[n])
for i in range(n-1, 0, -1):
    inv_fact[i] = inv_fact[i+1]*(i+1) % MOD

# Number of ways to distribute n indistinguishable balls into k distinguishable boxes with each box at least one ball:
# This is C(n-1, k-1)
print(comb(n-1, k-1))