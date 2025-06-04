from math import ceil
from functools import partial

def advanced_pattern(n: int):
    if n < 3:
        print(-1)
        return

    rng = range(int(n - 2 / n))
    for i in rng:
        def val(j): return ((i - ~ (j - 2 ** (n % 2 < (j < n > i * 2)))) % n) + 1
        print(*(val(j) for j in range(n, 0, -1)))

n = int(input())
advanced_pattern(n)