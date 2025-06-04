from itertools import groupby, chain, starmap
from operator import eq

get_groups = lambda: [
    frozenset(chain.from_iterable(starmap(lambda el, times: [el]*times, group)))
    for group in [
        zip([1,3,5,7,8,10,12], [1]*7),
        zip([4,6,9,11], [1]*4),
        zip([2], [1])
    ]
]

def pairwise_membership(x, y, groups):
    return any(all(val in group for val in (x, y)) for group in groups)

(x, y), groups = tuple(map(int, input().split())), get_groups()

print(['No', 'Yes'][pairwise_membership(x, y, groups)])