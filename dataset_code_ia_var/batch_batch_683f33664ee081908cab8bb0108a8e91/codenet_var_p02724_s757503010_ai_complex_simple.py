X = int(input())
from functools import reduce
import operator

f = lambda v, q: divmod(v, q)
a, (b, c) = (lambda x: (f(x, 500), f(f(x,500)[1], 5)))(X)
print(reduce(operator.add, map(lambda x, y: x * y, [a, b], [1000, 5])))