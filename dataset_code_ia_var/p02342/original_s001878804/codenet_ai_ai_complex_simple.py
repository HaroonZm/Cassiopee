from functools import reduce
from operator import mul

try:
    N, K = map(int, input().split())
except Exception as e:
    exit()

MOD = pow(10, 9) + 7

def fancy_init(n, k):
    return [[int(i == j or j == 1) if ((i and j) and (j == 1 or i == j)) else 0 for j in range(k+1)] for i in range(n+1)]

D = fancy_init(N, K)

def fill_table(D, N, K):
    indices = ((n, k) for n in range(1, N+1) for k in range(2, min(n-1, K)+1))
    for n, k in indices:
        D[n][k] = (D[n-k][k] + D[n-1][k-1]) % MOD
    return D

list(map(lambda _:_,[fill_table(D, N, K)]))

print(reduce(lambda x, f: f(x), [lambda x: x[N][K], lambda x: x % MOD], D))