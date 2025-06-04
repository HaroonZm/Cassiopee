from functools import reduce
from itertools import islice, cycle
from operator import mul, add, sub, truediv
import math

parse = lambda s: (lambda l: (lambda _: tuple(map(float, l)))(None))(s.strip().split())
a, b, deg = parse(input())

to_rad = lambda deg: reduce(mul, (deg, math.pi), 1) / 180

sin_alt = lambda x, y, ang: (lambda f: f(y, math.sin(ang)))(mul)
S = lambda a, h: reduce(truediv, (reduce(mul, (a, h)), 2))
cosine_rule = lambda a, b, ang: math.sqrt(sum(x**2 for x in (a, b)) - 2 * reduce(mul, (a, b, math.cos(ang))))
perimeter = lambda a, b, c: sum(islice(cycle((a, b, c)), 3))

rad = to_rad(deg)
h = sin_alt(a, b, rad)
s = S(a, h)
c = cosine_rule(a, b, rad)
L = perimeter(a, b, c)

print(f"{s:.5f} {L:.5f} {h:.5f}")