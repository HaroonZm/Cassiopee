from math import comb, factorial

def inclusion_exclusion(n, k, mod=10**9+7):
    acc = 0
    for i in range(k):
        term = comb(k, i) * pow(k - i, n, mod)
        acc = (acc + (-1)**i * term) % mod
    return acc * pow(factorial(k), -1, mod) % mod

n, k = map(int, input().split())
print(inclusion_exclusion(n, k))