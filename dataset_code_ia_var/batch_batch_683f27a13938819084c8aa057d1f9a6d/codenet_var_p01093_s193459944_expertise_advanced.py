from sys import stdin
from itertools import pairwise

def inputs():
    return map(int, stdin)

results = []
for line in stdin:
    n = int(line)
    if n == 0:
        break
    a = list(map(int, next(stdin).split()))
    a.sort()
    min_diff = min(abs(x - y) for x, y in pairwise(a))
    results.append(min_diff)

print('\n'.join(map(str, results)))