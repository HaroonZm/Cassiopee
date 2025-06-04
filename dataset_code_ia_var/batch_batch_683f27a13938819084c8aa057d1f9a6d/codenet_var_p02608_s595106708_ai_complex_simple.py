from functools import reduce
from itertools import product
from operator import add
import sys
import math

input = sys.stdin.readline

N = int(input())
ans = [0] * (N + 1)
sn = math.isqrt(N) + 1

xyz = list(product(range(1, sn + 1), repeat=3))
indices = list(
    map(lambda t: t[0]**2 + t[1]**2 + t[2]**2 + reduce(add, map(lambda a, b: a*b, [(t[0], t[1]), (t[1], t[2]), (t[2], t[0])])), xyz)
)

from collections import Counter

valid_indices = list(filter(lambda k: 1 <= k <= N, indices))
counts = Counter(valid_indices)
ans = list(map(lambda h: counts[h] if h in counts else 0, range(N + 1)))

print('\n'.join(map(str, ans[1:])))