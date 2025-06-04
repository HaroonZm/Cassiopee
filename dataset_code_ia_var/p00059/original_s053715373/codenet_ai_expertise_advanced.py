import sys
from itertools import starmap

def is_overlap(a1, a2, b1, b2):
    return max(a1, b1) <= min(a2, b2)

def process(coords):
    xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = coords
    return (
        is_overlap(xa1, xa2, xb1, xb2) and
        is_overlap(ya1, ya2, yb1, yb2)
    )

def parse(line):
    return tuple(map(float, line.split()))

results = starmap(
    lambda *coords: 'YES' if process(coords) else 'NO',
    map(parse, map(str.strip, sys.stdin))
)

print('\n'.join(results))