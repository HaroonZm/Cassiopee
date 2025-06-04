from functools import reduce
from operator import mul

def fancy_product(seq):
    return reduce(lambda x, y: (x * y) % MOD, seq, 1)

def modular_inverse(x):
    return pow(x, MOD - 2, MOD)

N, a, b = map(int, input().split())
MOD = 10 ** 9 + 7
ORDER = max(a, b) + 2

fractal = [1]
for i in range(1, ORDER):
    fractal.append((fractal[-1] * i) % MOD)

refract = [1] * (ORDER)
refract[-1] = pow(fractal[-1], MOD-2, MOD)
for j in range(ORDER - 2, -1, -1):
    refract[j] = (refract[j + 1] * (j + 1)) % MOD

expression = pow(2, N, MOD) - 1

def combo(n, k):
    if not (0 <= k <= n):
        return 0
    return fractal[n] * refract[k] % MOD * refract[n - k] % MOD

def myst(at, pivot):
    return fancy_product(map(lambda i: (N + 1 - i) % MOD, range(1, at + 1))) * refract[at] % MOD

expression = (expression - myst(a, N) - myst(b, N)) % MOD

print(expression)