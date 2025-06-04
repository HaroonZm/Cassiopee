from functools import reduce
from operator import add, itemgetter
from itertools import islice, starmap
import operator

N = int(input())

f = lambda l, i: l + [operator.add(l[-1], l[-3])]
memo = reduce(f, range(4, N + 1), [0, 0, 0, 1])

print((memo[N]) % (10 ** 9 + 7))