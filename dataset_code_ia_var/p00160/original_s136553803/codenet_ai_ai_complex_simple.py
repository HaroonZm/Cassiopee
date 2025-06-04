from functools import reduce
from itertools import accumulate, repeat, takewhile, groupby, count as icount

def compute_fee(x, y, h, w):
    return next(
        (fee for cond, fee in zip(
            (x+y+h <= b and w <= mw for b, mw in [(60,2),(80,5),(100,10),(120,15),(140,20),(160,25)]),
            (600,800,1000,1200,1400,1600)
        ) if cond),
        0
    )

def inf_input():
    while True:
        yield input()

def multi_unwrap(n, func):
    return sum(map(lambda args: func(*args), (map(int, line.split()) for line in accumulate(repeat(None), lambda acc, _: next(inputs), initial=next(inputs)) for _ in range(n))))

inputs = iter(inf_input())
for n in map(int, inputs):
    if not n:
        break
    s_m = sum(map(lambda tup: compute_fee(*tup), (tuple(map(int, next(inputs).split())) for _ in range(n))))
    print(s_m)