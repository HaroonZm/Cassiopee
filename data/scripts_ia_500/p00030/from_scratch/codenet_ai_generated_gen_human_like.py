import sys
from itertools import combinations

for line in sys.stdin:
    n, s = map(int, line.split())
    if n == 0 and s == 0:
        break
    count = 0
    for comb in combinations(range(10), n):
        if sum(comb) == s:
            count += 1
    print(count)