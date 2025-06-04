from collections import Counter
from functools import reduce
from operator import add
from itertools import chain, takewhile, starmap
import sys

fetch_lines = lambda stop: list(takewhile(lambda s: s != stop, iter(input, '')))
parse_pairs = lambda lines: list(starmap(lambda a, b: (int(a), int(b)), (map(str.strip, l.split(',')) for l in lines)))
counter_from_input = lambda lines: Counter(map(lambda t: t[0], parse_pairs(lines)))

A = counter_from_input(fetch_lines(''))
lines = list(map(lambda l: l.rstrip('\n'), sys.stdin))
B = counter_from_input(lines)

intersection_keys = set(A) & set(B)
result = map(lambda k: (k, reduce(add, (A[k], B[k]))), intersection_keys)
print('\n'.join(f"{k} {v}" for k, v in result))