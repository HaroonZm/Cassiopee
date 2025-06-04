from functools import reduce
from operator import add
import sys
import itertools

pipe = lambda f, xs: reduce(lambda v, fn: fn(v), xs, f)
splat = lambda f: lambda args: f(*args)
seq = lambda start, stop, step: itertools.islice(itertools.count(start, step), 0, ((stop-start)//step)+1)
sq_sum = lambda d, gen: reduce(add, map(lambda x: d*x**2, gen), 0)

list(map(lambda l: pipe(int(l.strip()), [
    lambda d: list(seq(d, 600-d, d)),
    lambda xs: (xs, int(l.strip())),
    splat(lambda xs, d: sq_sum(d, xs)),
    print
]), sys.stdin))