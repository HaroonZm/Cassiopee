import math
def comb(n, k):
    if n < 0 or k < 0 or n < k: return 0
    return math.factorial(n) // math.factorial(n-k) // math.factorial(k)

n,k = map(int, input().split())
MOD = 10 ** 9 + 7

all = 0

for i in range(k):
    add = comb(k, i) * ((k-i) ** n)
    if i & 1: all = (all - add)
    else: all = (all + add)

print(all // (math.factorial(k)) % MOD)