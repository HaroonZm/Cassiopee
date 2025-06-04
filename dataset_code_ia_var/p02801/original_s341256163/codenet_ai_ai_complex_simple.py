from functools import reduce
from operator import add

c = __import__('functools').reduce(lambda a, _: a, iter([input()]), None)
code = list(map(ord, c))
inc = list(map(lambda x: x+1, code))
ans = reduce(add, map(chr, inc))
print(''.join([*ans]))