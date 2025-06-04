from functools import reduce
from operator import itemgetter

triple = tuple(map(int, input().split()))
labels = ('A','B','C')
indexed = list(zip(triple, labels))
max_index = reduce(lambda x, y: x if x[0] > y[0] else y, indexed)
others = [v for v in indexed if v != max_index]
if all(max_index[0] > x[0] for x in others) and len(set(triple)) == 3:
    print(max_index[1])