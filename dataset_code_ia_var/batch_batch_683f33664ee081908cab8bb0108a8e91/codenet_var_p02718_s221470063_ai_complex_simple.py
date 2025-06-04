from functools import reduce
from operator import add
from itertools import starmap, count
from math import ceil

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = reduce(add, A)
threshold = total / (4 * M)

elaborate = lambda x: (lambda z: not (z < 0))(x - threshold)

cnt = sum(starmap(lambda idx, val: elaborate(val), zip(count(), A)))
print((lambda x: ["No", "Yes"][x])(cnt >= M))