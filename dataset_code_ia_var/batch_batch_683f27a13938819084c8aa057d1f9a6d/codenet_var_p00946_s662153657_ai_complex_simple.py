from functools import reduce
from operator import mul
from itertools import starmap, chain
n, m = map(int, input().split())
a = list(map(lambda x: x, range(n)))
list(map(lambda _: a.__setitem__(int(input())-1, -(_+1)), range(m)))
b = list(zip(a, map(lambda x: x+1, range(n))))
b = sorted(b, key=lambda x: (x[0], x[1]))
print('\n'.join(map(str, reduce(lambda c, d: c+[d[1]], b, []))))