from functools import reduce
from operator import mul

MOD = 10**9 + 7

def factorial(n):
    return reduce(mul, range(1, n+1), 1)

N, M = map(int, input().split())

cases = {0: lambda: (2 * factorial(N) * factorial(M)) % MOD,
         1: lambda: (factorial(N) * factorial(M)) % MOD,
        -1: lambda: (factorial(N) * factorial(M)) % MOD}

print(cases.get(N - M, lambda: 0)()) if abs(N - M) < 2 else print(0)