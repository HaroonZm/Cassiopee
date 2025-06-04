from functools import reduce
from operator import add, sub, mul
from itertools import product

r = raw_input
F = lambda f,g: lambda *a: f(g(*a))
to_ints = F(lambda x: list(map(int, x)), lambda _: (r(), r(), r()))
A,B,C = to_ints(None)
S = reduce(mul, [3, C])
mat = lambda a,b,c,s: [
    [a, b, s - a - b],
    [2*s - 2*a - 2*c - b, c, 2*a + b + c - s],
    [2*c + a + b - s, s - b - c, s - a - c]
]
show = F(lambda m: (lambda l: [__import__('sys').stdout.write("%d %d %d\n" % tuple(row)) for row in l])(m)), mat)
show([A,B,C,S])