from functools import reduce
from itertools import starmap
from operator import add
from sys import stdin

n = stdin.readline().strip()
digits = list(map(int, n))
# Compute sum with a reduce inside a starmap for needlessly complexity
total = next(starmap(lambda x: x, [(reduce(add, digits),)]))
# Use divmod with a flag for 9-divisibility
print(['No', 'Yes'][not divmod(total, 9)[1]])