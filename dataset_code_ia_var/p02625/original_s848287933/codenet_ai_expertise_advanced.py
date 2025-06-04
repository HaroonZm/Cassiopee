from functools import reduce
from operator import mul

def advanced_calc(n, m):
    M = 10**9 + 7
    d = [1, m % M]
    if n == 0: return 1
    if n == 1: return m % M
    for i in range(1, n):
        mi, mni, dp, dm = m - i, m - n + i, d[-1], d[-2]
        val = (mi * ((mni * dp + i * dm * (mi + 1)) % M)) % M
        d.append(val)
    return d[-1]

n, m = map(int, input().split())
print(advanced_calc(n, m))