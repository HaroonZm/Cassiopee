from functools import reduce
from operator import add, sub, eq, gt, lt

x = list(map(int, input().split()))
sides = list(map(lambda t: reduce(add, t), ((x[i] for i in (0,1)), (x[j] for j in (2,3)))))
cmp = (lambda a, b: 'Left'*(gt(a,b))+('Balanced')*(eq(a,b))+('Right')*(lt(a,b)))
print(cmp(*sides))