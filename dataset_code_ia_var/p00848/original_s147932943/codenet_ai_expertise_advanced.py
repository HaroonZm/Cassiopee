from functools import lru_cache
from math import isqrt

# Générer la liste des nombres premiers jusqu'à 1120 efficacement
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return primes

primes = sieve(1120)
N, K = 1121, 15

# Initialiser le tableau dp avec mémoire partagée (meilleures performances en numpy, mais on reste pur Python ici)
dp = [[0]*N for _ in range(K)]
dp[0][0] = 1

for idx, val in enumerate(primes):
    lim = min(idx+1, K-1)
    for k in range(lim, 0, -1):
        for j in range(val, N):
            dp[k][j] += dp[k-1][j-val]

while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break
    if n == 0:
        break
    print(dp[k][n])