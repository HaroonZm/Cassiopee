from functools import reduce
from operator import sub, floordiv
from itertools import count, islice

a, b = map(int, input().split())
delta = reduce(sub, (b, 1)), reduce(sub, (a, 1))
div = floordiv(*delta)
gen = (div + (1 if (b - 1) % (a - 1) else 0) for _ in count(0))
print(next(islice(gen, 0, 1)))