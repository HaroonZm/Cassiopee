from functools import reduce
from operator import mul, add, sub
from math import pi, sin, cos, sqrt

to_radian = lambda deg: reduce(mul, [deg, pi], 1.0 / 180.0)
parse_floats = lambda s: list(map(float, s.split()))
unroll = lambda f, x: f(*x)

compose = lambda *fs: lambda x: reduce(lambda v, f: f(v), reversed(fs), x)

f_area = lambda a, b, c: reduce(lambda acc, op: op(acc), [lambda _: a, lambda v: v * b, lambda v: v * sin(c), lambda v: v / 2.0], 0)
f_perimeter = lambda a, b, c: reduce(add, [a, b, sqrt(reduce(add, [a ** 2, b ** 2, -2 * a * b * cos(c)]))])
f_height = lambda a, b, c: reduce(add, [0, b * sin(c)])

exec("""
a, b, c = parse_floats(raw_input())
c = to_radian(c)
print("%f" % f_area(a, b, c))
print("%f" % f_perimeter(a, b, c))
print("%f" % f_height(a, b, c))
""")