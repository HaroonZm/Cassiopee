from functools import reduce
from operator import add
from itertools import islice, cycle, accumulate

tbl = [600, 800, 1000, 1200, 1400, 1600]

def package_fee(params):
    x, y, h, w = params
    s = x + y + h
    cond = (s <= 160) & (w <= 25)
    k1 = (s > 60) * ((s - 61) // 20 + 1)
    k2 = (w > 2) * ((w - 1) // 5 + 1)
    ki = max(k1, k2)
    return tbl[ki] * cond

def fees(n):
    inputs = (tuple(map(int, input().split())) for _ in range(n))
    return reduce(add, map(package_fee, inputs), 0)

while True:
    n = int(input())
    if not n: break
    # Wrapping in single-element lists and chained comprehensions, just because:
    print(list(accumulate([fees(n)], lambda x, y: y))[-1])