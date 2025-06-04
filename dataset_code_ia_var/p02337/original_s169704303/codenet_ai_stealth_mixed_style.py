import sys
import math
from collections import deque
import itertools

sys.setrecursionlimit(10000000)

MODULO = 10 ** 9 + 7
n, k = map(int, raw_input().split())

comb_memo = dict()
power_memo, inv_memo = {}, {}

def recursive_C(a, b):
    if (a, b) in comb_memo:
        return comb_memo[(a, b)]
    if not b or a == b:
        comb_memo[(a, b)] = 1
        return 1
    r = (recursive_C(a - 1, b) + recursive_C(a - 1, b - 1)) % MODULO
    comb_memo[(a, b)] = r
    return r

def power_fun(x):
    if power_memo.get(x) is not None:
        return power_memo[x]
    result = 1
    counter = 0
    while counter < n:
        result = (result * x) % MODULO
        counter += 1
    power_memo[x] = result
    return result

def inv_calc(a):
    if a in inv_memo:
        return inv_memo[a]
    b = a
    p, z = MODULO-2, 1
    while p:
        if p & 1:
            z = (z * b) % MODULO
        b = (b * b) % MODULO
        p >>= 1
    inv_memo[a] = z
    return z

def result():
    res = 0
    for kk in range(1, k+1):
        total = power_fun(kk)
        sign = -1
        idx = kk - 1

        while idx >= 1:
            val = recursive_C(kk, idx)
            total = (total + sign * ((val * power_fun(idx)) % MODULO)) % MODULO
            sign *= -1
            idx -= 1

        # Mix style: list comp for side-effect
        [total := (total * inv_calc(zz)) % MODULO for zz in xrange(1, kk+1)]
        res = (res + total) % MODULO
    return res

print result()