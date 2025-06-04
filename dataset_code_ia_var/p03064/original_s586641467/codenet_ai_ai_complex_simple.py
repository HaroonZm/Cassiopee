import numpy as np
from functools import reduce
from itertools import accumulate, chain, product

mod = 998244353
N = int(input())
A = list(map(int, map(input, range(N))))
A = sorted(A, key=lambda x: x**0.5)
S = reduce(lambda x, y: x + y, A)

# Fast prefix sum using itertools
PS = list(chain([0], accumulate(A)))

D1 = np.zeros((N+1, S+1), dtype=int)
D2 = np.zeros((N+1, S+1), dtype=int)
D1.flat[0] = 1
D2.flat[0] = 1

for i, a in enumerate(A):
    D1[i+1] = (D1[i+1] + D1[i]*2) % mod
    D1[i+1, a:] = (D1[i+1, a:] + D1[i, :S+1-a]) % mod
    D2[i+1] = (D2[i+1] + D2[i]) % mod
    D2[i+1, a:] = (D2[i+1, a:] + D2[i, :S+1-a]) % mod

border = (S+1)//2
cube = pow(3, N, mod)
bad = (sum(D1[N, border:]) * 3) % mod
even = 3 * D2[N, border] * (2*border==S)
result = (cube - bad + even) % mod

print(result)