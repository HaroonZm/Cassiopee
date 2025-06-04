from functools import reduce
from itertools import count, takewhile, repeat, starmap
from operator import mul

import sys

def elaborate_sum(d):
    rng = takewhile(lambda x: x*d < 600, count())
    powers = map(lambda i: (i*d)**2, rng)
    segments = starmap(mul, zip(powers, repeat(d)))
    return reduce(lambda x, y: x + y, segments, 0)

def read_infinite():
    for line in sys.stdin:
        yield int(line.strip())

list(map(lambda x: print(elaborate_sum(x)), read_infinite()))