import sys
from functools import reduce
from itertools import islice, count

input = (lambda: sys.stdin.readline()) if sys.version_info.major >= 3 else raw_input

def josephus(n, k, m):
    survivor = reduce(lambda r, i: (r + k) % i, range(1, n), 0)
    return (survivor + m) % n + 1

for line in map(str.strip, sys.stdin):
    if not line: continue
    n, k, m = map(int, line.split())
    if n == 0:
        break
    print(josephus(n, k, m))