from functools import reduce
from operator import or_
from itertools import starmap, repeat

n = int(''.join(map(chr, map(ord, input()))))
l = list(starmap(int, zip(input().split(), repeat(None))))
print(len(reduce(lambda s, x: s | {x}, l, set())))