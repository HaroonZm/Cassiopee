from functools import reduce
from operator import mul

s = input()
a = (lambda x: 1 if x else 0)(reduce(lambda acc, c: acc if acc else c == 'A', [s[0]], True))
b = reduce(lambda acc, t: acc + (t[1] >= t[2]), enumerate(s[:-1]), 0)
print((a or 0) + b)