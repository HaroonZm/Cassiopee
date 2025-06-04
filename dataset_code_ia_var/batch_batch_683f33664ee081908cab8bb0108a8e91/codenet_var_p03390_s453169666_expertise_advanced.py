from functools import lru_cache

def getKth(x, a, k):
    return k if k < a else k + 1

def getRKth(x, a, k):
    if x < a or k < (x - a):
        return x - k + 1
    return x - k

def NB(x, b):
    return x if x < b else x + 1

@lru_cache(maxsize=None)
def f(x, a, b):
    mv = 25
    rep = 0
    nb_x_b = NB(x, b)
    # Try around half = (x+1)//2, b-a, nb_x_b - b
    for half in ((x + 1) // 2, b - a, nb_x_b - b):
        for delta in range(-mv, mv + 1):
            k = half + delta
            if 1 <= k <= x:
                prod = getKth(x, a, k) * getRKth(nb_x_b, b, k)
                if prod > rep:
                    rep = prod
    return rep

import sys

def input_gen():
    for line in sys.stdin:
        yield line
input_iter = input_gen()
def next_input():
    return next(input_iter)

q = int(next_input())
for _ in range(q):
    a, b = map(int, next_input().split())
    if a > b:
        a, b = b, a
    lo, hi = 1, 10**19
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if f(mid, a, b) < a * b:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(res)