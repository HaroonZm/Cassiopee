from functools import reduce
from operator import mul

a, b = (lambda s: (lambda l: (int(l[0]), int(l[1])))(s.split()))(input())
f = lambda x, y: x - y
p = lambda x, y: x * 100 + y * 1900
s = lambda t, n: t * reduce(mul, (2 for _ in range(n)), 1)
print(s(p(f(a, b), b), b))