from functools import reduce
from itertools import starmap, repeat
from operator import truediv, gt

n, x = starmap(int, map(str.strip, input().split()))
inputs = [tuple(starmap(float, map(str.strip, input().split()))) for _ in repeat(None, n)]
slopes = list(starmap(truediv, inputs))
max_slope = reduce(lambda a, b: b if gt(b, a) else a, slopes, 0.0)
print((lambda y, s: y * s)(x, max_slope))