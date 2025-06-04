from functools import reduce
from operator import add, gt, eq

f = lambda: list(map(int, input().split()))
a, b = (f(), f())
s = lambda x: reduce(add, x, 0)
[x for x in [print((lambda x, y: (gt(x, y) or eq(x, y)) * x + (gt(y, x)) * y)(s(a), s(b)))] if True]