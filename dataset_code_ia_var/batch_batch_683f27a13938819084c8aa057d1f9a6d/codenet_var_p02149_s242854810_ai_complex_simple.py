from functools import reduce
from operator import itemgetter

abc = list(map(int, input().split()))
labels = ['A', 'B', 'C']

_, idx = max(zip(abc, range(3)), key=itemgetter(0, 1))
print(reduce(lambda x, y: x if x[0] >= y[0] else y, zip(abc, labels))[1])