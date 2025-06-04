from itertools import groupby
from functools import reduce
from operator import or_

n = int(input())
l = list(map(int, input().split()))

# Équivalent set via reduce, map et lambda
uniq = list(map(lambda x: x[0], groupby(sorted(l))))
res = reduce(lambda a, b: a + 1, uniq, 0)
print(res)