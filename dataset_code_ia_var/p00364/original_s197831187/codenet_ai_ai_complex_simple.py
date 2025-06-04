from functools import reduce
from operator import truediv, mul
from itertools import starmap

n, t = map(int, input().split())

dat = list(starmap(lambda x, y: (int(x), int(y)), (input().split() for _ in [0]*n)))

ratios = list(map(lambda pair: truediv(mul(pair[1], t), pair[0]), dat))
print(reduce(lambda a, b: (a > b) * a + (b >= a) * b, ratios))