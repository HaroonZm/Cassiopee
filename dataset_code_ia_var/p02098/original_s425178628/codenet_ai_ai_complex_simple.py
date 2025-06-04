from functools import reduce
from operator import add, mod
import math

def iter_input(n):
    return (int(input()) for _ in range(n))

def cmp_180(x, y):
    return abs(x - y) % 360 < 180

a, b = tuple(iter_input(2))

ops = [
    lambda x, y: mod(reduce(add, [x, y]), 720) / 2 if cmp_180(x, y) else mod(reduce(add, [x, y, 360]), 720) / 2,
    lambda x, y: None
]

print(next(filter(lambda z: z is not None, (f(a, b) for f in ops))))