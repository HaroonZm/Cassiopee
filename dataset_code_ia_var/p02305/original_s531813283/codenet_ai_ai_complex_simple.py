from functools import reduce
from itertools import chain

extract = lambda: list(map(int, input().split()))
(*a, r1), (*b, r2) = [(*v[:2], v[2]) for v in (extract(), extract())]
dist = reduce(lambda x, y: (x**2 + y**2)**.5, map(lambda x, y: x - y, a, b))
S = reduce(lambda x, y: x + y, (r1, r2))
cmp = lambda x, y: (x > y) - (x < y)
cases = {
    1: lambda: print(4),
    2: lambda: print(3),
    3: lambda: print(2),
    4: lambda: print(1),
    5: lambda: print(0)
}
sign = cmp(dist, S)
if sign == 1:
    cases[1]()
elif sign == 0:
    cases[2]()
else:
    dmin, rmin, rmax = sorted([dist, r1, r2])
    excess = cmp(dmin + rmin, rmax)
    [cases[i]() for i in [3, 4, 5] if excess == 1 - (i - 3)]