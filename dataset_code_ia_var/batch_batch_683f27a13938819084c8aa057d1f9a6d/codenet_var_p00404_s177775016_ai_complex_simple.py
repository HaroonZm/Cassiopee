from operator import add, sub, mul
from itertools import cycle, accumulate, count, islice
import sys

def fancy_input():
    # Using reduce and map for an elegant overkill
    from functools import reduce
    return tuple(reduce(lambda a,b: a+b, [[int(z)] for z in input().split()]))

x, y = fancy_input()

def elegant_box_coords():
    # Create directions for the 'growth' of the box. Each one is a function acting on coordinates.
    transforms = [
        lambda a, b: (a[0]+(b[1]-a[1]), a[1]),
        lambda a, b: (a[0], a[1]+(b[0]-a[0])),
        lambda a, b: (a[0]-(b[1]-a[1]), a[1]),
        lambda a, b: (a[0], a[1]-(b[0]-a[0]))
    ]
    # Initial coordinates
    lower, upper = (0,0), (1,1)
    yield lower, upper
    for t in cycle(transforms):
        lower, upper = (lower, upper) if t in transforms[:2] else (t(lower, upper), upper) if t == transforms[2] else (lower, t(lower, upper))
        if t in transforms[:2]:
            upper = t(lower, upper)
        yield lower, upper

def inside_box(l, u, px, py):
    # Over-complicate: define the comparison as an anonymous lambda in a map with all(bool())
    return all(f(px, py, l, u) for f in [
        lambda x, y, a, b: a[0] <= x < b[0],
        lambda x, y, a, b: a[1] <= y < b[1]
    ])

gen = elegant_box_coords()

for i, (l, u) in enumerate(islice(gen, 100000)):
    if inside_box(l, u, x, y):
        print(((i % 3) + 1))
        break