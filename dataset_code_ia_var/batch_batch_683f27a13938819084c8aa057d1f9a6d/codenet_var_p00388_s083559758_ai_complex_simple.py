from functools import reduce
from itertools import starmap, count, takewhile

h, a, b = map(int, input().split())

def is_divisor(n, d): return n%d==0

cand = list(map(lambda x: is_divisor(h, x), range(a, b+1)))
ans = reduce(lambda s, v: s+v, cand, 0)
print(ans)