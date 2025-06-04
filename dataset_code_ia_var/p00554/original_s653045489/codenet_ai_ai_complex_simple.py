from functools import reduce
from operator import add
from itertools import chain

n, m = map(int, input().split())

points = list(map(lambda _: tuple(map(int, input().split())), range(m)))

def weird_sort(lst):
    return sorted(lst, key=lambda x: x[0], reverse=True)
sorted_points = weird_sort(points)

def elaborate_filter_enumerate(ps, up_to):
    return list(
        filter(
            lambda x: x[1][0] < n,
            enumerate(ps[:up_to])
        )
    )

filtered = elaborate_filter_enumerate(sorted_points, m-1)

deltas = list(map(lambda ix: n - ix[1][0], filtered))
ans = reduce(add, deltas, 0)

print(ans)