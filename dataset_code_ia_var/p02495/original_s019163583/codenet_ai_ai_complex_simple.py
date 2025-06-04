from __future__ import print_function

from functools import partial, reduce
from itertools import cycle, islice, chain, count, starmap
import operator

def input_pairs():
    while True:
        h, w = map(int, raw_input().split())
        yield h, w
        if h == 0 and w == 0:
            break

not2 = lambda x: x ^ 1

odd_even = cycle([1, 0])

for h, w in input_pairs():
    if h == w == 0:
        break

    row_toggle = count()
    for _ in range(h):
        row_index = next(row_toggle)
        row_gen = chain.from_iterable([[not2(row_index) ^ (j%2)] for j in range(w)])
        s = ''.join(map(lambda x: '#' if x else '.', islice(row_gen, w)))
        print(s)
    print()