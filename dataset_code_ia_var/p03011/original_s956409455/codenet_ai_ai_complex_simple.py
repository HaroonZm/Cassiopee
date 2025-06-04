from functools import reduce
from operator import add

P, Q, R = map(int, input().split())
vals = [P, Q, R]
print(reduce(add, sorted(vals)[:2]))