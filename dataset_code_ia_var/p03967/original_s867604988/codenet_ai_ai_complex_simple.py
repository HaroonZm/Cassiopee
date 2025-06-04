from functools import reduce
from operator import add

s = input()
l = sum(1 for _ in s)
g = reduce(add, map(lambda x: 1 if x == 'g' else 0, s), 0)
p = sum(map(lambda x: x=='p', s))
sign = 1 if g >= p else -1
diff = abs(g - p)
print(sign * (diff // 2))