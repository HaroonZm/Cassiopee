from sys import stdin
from itertools import count, islice

def is_ugly(x):
    for f in (2, 3, 5):
        while x % f == 0:
            x //= f
    return x == 1

for line in stdin:
    n = tuple(map(int, line.split()))
    if not n[0]:
        break
    lo, hi = n
    print(sum(map(is_ugly, range(lo, hi + 1))))