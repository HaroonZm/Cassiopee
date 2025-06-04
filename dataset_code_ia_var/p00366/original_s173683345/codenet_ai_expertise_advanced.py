from typing import Iterable
from bisect import bisect_left

def divisor_list(x: int) -> tuple[int, ...]:
    from math import isqrt
    small, large = [], []
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            small.append(i)
            if i != x // i:
                large.append(x // i)
    return tuple(sorted(small + large))

N = int(input())
t = [int(input()) for _ in range(N)]
div = divisor_list(max(t))
di = sum(div[bisect_left(div, ti)] - ti for ti in t)
print(di)