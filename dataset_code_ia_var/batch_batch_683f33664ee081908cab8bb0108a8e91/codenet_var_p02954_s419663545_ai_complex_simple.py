from itertools import groupby, accumulate, chain, islice
from operator import itemgetter
from math import ceil, floor

S = list(input())
groups = [(k, sum(1 for _ in g)) for k, g in groupby(S)]
lengths = list(map(itemgetter(1), groups))
partitions = list(accumulate(chain([0], lengths)))
res = [0] * len(S)
pairs = list(zip(islice(partitions, None, -2), islice(partitions, 1, None), islice(partitions, 2, None)))

for idx, (l, m, r) in enumerate(pairs):
    if idx % 2 == 0:
        continue
    left_count = m - l
    right_count = r - m
    res[m-1] = ceil(left_count/2) + floor(right_count/2)
    res[m] = floor(left_count/2) + ceil(right_count/2)

print(*res)