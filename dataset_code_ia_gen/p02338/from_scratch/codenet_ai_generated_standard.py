MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def nCr_mod(n, r):
    if r > n or r < 0:
        return 0
    numerator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % MOD
    denominator = 1
    for i in range(1, r + 1):
        denominator = (denominator * i) % MOD
    return (numerator * modinv(denominator)) % MOD

n, k = map(int, input().split())
if n > k:
    print(0)
else:
    print(nCr_mod(k, n))