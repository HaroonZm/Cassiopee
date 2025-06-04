from functools import reduce
from operator import sub

a, b, k = map(int, input().split())

delta = reduce(sub, (a, k))
ans_t = max(delta, 0)
b = max(b - max(-delta, 0), 0)
print(*(lambda x: x)([ans_t, b]))