from functools import reduce
from operator import itemgetter

s = input().split()
t = tuple(map(int, s))
labels = 'ABC'
result = reduce(lambda x, y: x if x[0] > y[0] else y, zip(t, labels))
print(itemgetter(1)(result))