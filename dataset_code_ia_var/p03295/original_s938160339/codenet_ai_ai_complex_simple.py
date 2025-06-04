from itertools import islice, starmap, accumulate, groupby
from operator import itemgetter, sub, ge

n, m = map(int, input().split())
c = list(starmap(lambda *row: list(map(int, row)), zip(*(input().split() for _ in range(m)))))
c = list(map(list, map(tuple, sorted(tuple(map(int, row.split())) for row in map(' '.join, c)))))
intervals = []
for k, g in groupby(c, key=itemgetter(0)):
    intervals.append([k, min(map(lambda x: x[1] - 1, g))])
merges = list(accumulate(intervals, lambda a, b: [max(a[0], b[0]), min(a[1], b[1]) if not a[1] < b[0] else b[1]]))
counter = 1 + sum(a[1] < b[0] for a, b in zip(merges, islice(merges, 1, None)))
print(counter)