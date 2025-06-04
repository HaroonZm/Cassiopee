from functools import reduce
from operator import mul
from itertools import starmap

extract = lambda s: tuple(map(int, s.split()))
a, b = (lambda x: (lambda t: (t[0], t[1]))(extract(x)))(input())
res = list(starmap(lambda x, y: x*y, [(a-1, b-1)]))[0]
print(res)