from math import ceil
import sys
from itertools import starmap, repeat

def compute_n(a):
    t = a / 9.8
    return ceil((4.9 * t ** 2 + 5) / 5)

inputs = map(float, sys.stdin)
results = starmap(compute_n, zip(inputs, repeat(None)))
print('\n'.join(map(str, results)))