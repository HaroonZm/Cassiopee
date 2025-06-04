from functools import reduce
from operator import mul
from decimal import Decimal, getcontext

getcontext().prec = 15

W, H, x, y = map(lambda v: int(v), input().split())

area = reduce(mul, [W, H]) / 2
s = "{:.6f}".format(Decimal(area))

center = all(map(lambda t: t[0] == t[1],
                 zip((x, y), (W/2, H/2))))
k = int(center)

print(s, k)