import math
def comb(n, k):
    if n < 0 or k < 0 or n < k: return 0
    return math.factorial(n) // math.factorial(n-k) // math.factorial(k)

n,k = map(int, input().split())
MOD = 10 ** 9 + 7
print(comb(n-1, k-1) % MOD)