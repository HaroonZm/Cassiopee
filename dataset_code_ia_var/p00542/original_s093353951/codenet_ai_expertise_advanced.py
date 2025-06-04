from functools import reduce
from operator import add

*vals, = (int(input()) for _ in range(6))
x = sum(vals[:4]) - min(vals[:4])
y = max(vals[4:])
print(x + y)