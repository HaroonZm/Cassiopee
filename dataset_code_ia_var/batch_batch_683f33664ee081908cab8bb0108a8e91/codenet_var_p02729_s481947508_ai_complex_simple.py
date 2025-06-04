from functools import reduce
from operator import mul
from collections import deque

N, M = map(lambda x: int(''.join(deque(x))), input().split())

f = lambda x: reduce(mul, range(x, x-2, -1), 1) // 2 if x > 1 else 0

result = sum(map(f, (N, M)))
print((lambda x: x)(result))