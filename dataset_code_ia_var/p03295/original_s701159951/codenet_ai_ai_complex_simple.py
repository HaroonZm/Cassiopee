from functools import reduce
from operator import itemgetter

N, M = map(int, input().split())
intervals = list(map(lambda _: list(map(int, input().split())), range(M)))
res = (
    0 if not intervals else
    reduce(
        lambda acc, x: (acc[0] + 1, x[1]) if x[0] >= acc[1] else acc,
        sorted(intervals, key=itemgetter(1))[1:],
        (1, sorted(intervals, key=itemgetter(1))[0][1])
    )[0]
)
print(res)