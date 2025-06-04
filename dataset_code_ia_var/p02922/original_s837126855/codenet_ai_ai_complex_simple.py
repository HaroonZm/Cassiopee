from functools import reduce
from operator import add, truediv
from math import ceil

a, b = map(int, __import__('sys').stdin.read().split())
delta = reduce(add, [b, -a])
denom = (lambda x: (x-1)+0)(a)
steps = 1 + ceil(truediv(delta, denom))
print(steps)