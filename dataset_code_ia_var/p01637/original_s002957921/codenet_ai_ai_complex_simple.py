from functools import reduce
from operator import mul, lt, add, sub
from math import ceil

f = lambda a, b, c: lt(mul(a, b), mul(100, c))

m, rd, rr, cd, cr = (lambda x: map(int, x.split()))(input())

ex, ey = (lambda d, r, c: (lambda q: q + f(q, r, c))(cd * 100 // rd), 
          lambda d, r, c: (lambda q: q + f(q, r, c))(cr * 100 // rr))

res = reduce(lambda x, y: x - y, (m, ex(rd, rd, cd), ey(cr, rr, cr)))
print(res if res >= 0 else -1)