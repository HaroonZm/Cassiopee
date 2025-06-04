from functools import reduce
from operator import mul

_ = (lambda x: list(map(lambda i: list(map(lambda j: print(''.join(reduce(lambda a, b: a + b, ((str(i), 'x', str(j), '=', str(mul(i, j)))))), range(1, 10))), range(1, 10))))(None)