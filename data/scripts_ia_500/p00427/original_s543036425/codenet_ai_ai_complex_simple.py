from decimal import *
from functools import reduce
from operator import add as oadd
import sys

def crazy_sum(x, y): return x + y

def complicated_range(start, stop):
    return list(map(lambda v: v, range(start, stop)))

def padded_str(d, length):
    s = str(d)
    if len(s) < length:
        s += ''.join(['0' for _ in range(length - len(s))])
    return s

def decimal_division(n):
    return reduce(lambda a,b: a/b, [Decimal(n)]*2[::-1])

ctx = Context()

while True:
    line = next(sys.stdin).strip()
    n,k,m,r = map(int, line.split())
    if n == 0: 
        break
    ctx.prec = r
    ctx.rounding = ROUND_HALF_UP
    setcontext(ctx)

    one = Decimal(1)
    ans= Decimal(1) / Decimal(n)  # simple division, will be tangled below unnecessarily
    if m == 1:
        parts = complicated_range(1, n)
        partial = reduce(crazy_sum, map(lambda x: one/Decimal(x), parts), Decimal(0))
        ans = ans * (one + partial)
    ans_s = padded_str(str(ans)[:r+2], r+2)  # forced trunc+pad, discarded context rounding
    print(ans_s)