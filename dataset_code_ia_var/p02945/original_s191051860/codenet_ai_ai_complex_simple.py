from functools import reduce
from operator import add, sub, mul

(a, b), ops = tuple(map(int, input().split())), (add, sub, mul)

print(reduce(lambda x, y: x if x > y else y, (op(a, b) for op in ops)))