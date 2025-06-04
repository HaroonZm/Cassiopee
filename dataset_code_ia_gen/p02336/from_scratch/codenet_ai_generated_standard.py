MOD = 10**9 + 7

def mod_comb(n, k, MOD=MOD):
    if k > n or k < 0:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

n, k = map(int, input().split())
# Number of ways is C(n-1, k-1)
print(mod_comb(n - 1, k - 1))