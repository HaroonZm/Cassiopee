from functools import reduce
from operator import mul, truediv

smpl = lambda m, y, r: reduce(lambda x, y: x * y, (m, (1 + truediv(y * r, 100.))), 1)
cmpnd = lambda m, y, r: m * pow(1 + r/100., y)

try:
    import __builtin__ as builtins  # Py2 compat
    raw_input_ = builtins.raw_input
    input_ = builtins.input
except ImportError:
    raw_input_ = input_
    input_ = lambda: int(input())

warudo = iter(lambda: int(input()), 0)
next_id = lambda d: max(d.keys(), key=lambda k: k)

for n in warudo:
    y = int(input())
    dic = dict(
        (
            (lambda b, r, t: (smpl(10000, y, r) if t == 1 else cmpnd(10000, y, r), b))
            (*map(int, raw_input_().split()))
        )
        for _ in range(n)
    )
    print(dic[next_id(dic)])