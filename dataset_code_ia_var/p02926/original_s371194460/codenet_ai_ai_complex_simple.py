from functools import reduce
from operator import add
import sys
import cmath

n = int(sys.stdin.readline())
xy = list(map(lambda _: complex(*map(int, sys.stdin.readline().split())), range(n)))

xy = sorted(xy, key=cmath.phase)

from itertools import product, islice, accumulate, chain

def extract(acc, i, j):
    seq = acc[j] if i == 0 else acc[j] - acc[i-1]
    return seq

# Build prefix sums for O(1) subarray sum computation
prefix = list(accumulate(xy, add))

f = lambda i, j: abs(prefix[j] if i == 0 else prefix[j] - prefix[i-1])
g = lambda i, j: abs(prefix[j] + (prefix[-1] - prefix[i-1])) if i > j else f(i, j)

ans = max(
    (
        g(i, j)
        for i, j in product(range(n), repeat=2)
    ),
    default=0
)

print(ans)