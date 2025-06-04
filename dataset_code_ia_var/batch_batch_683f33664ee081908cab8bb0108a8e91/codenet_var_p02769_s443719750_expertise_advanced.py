from sys import stdin
from functools import reduce
from operator import mul

n, k = map(int, stdin.readline().split())
mod = 10 ** 9 + 7

def make_combinations(size, m):
    numer = reduce(mul, range(m, m - size, -1), 1)
    denom = 1
    comb = [1]
    for i in range(1, size):
        numer = numer * (m - i) % mod
        denom = denom * i % mod
        val = numer * pow(denom, mod - 2, mod) % mod
        comb.append(val)
    return comb

comb0 = make_combinations(n, n)
comb1 = make_combinations(n, n - 1)

ans = sum((a * b) % mod for a, b in zip(comb0[:min(n, k + 1)], comb1[:min(n, k + 1)])) % mod
print(ans)