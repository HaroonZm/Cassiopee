from operator import __truediv__ as _div
from functools import reduce

get = lambda: int(input())
pool = [get() for _ in range(6)]
N = pool.pop(0)
strange_pick = sorted(pool)[0]
lucky = lambda x, y: int(x // y) + bool(x % y)
steps = lucky(N, strange_pick) + (2 << 1)
print(steps)