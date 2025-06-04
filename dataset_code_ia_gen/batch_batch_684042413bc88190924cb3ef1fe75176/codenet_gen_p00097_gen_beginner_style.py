import sys
from itertools import combinations

for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    n, s = map(int, line.split())
    if n == 0 and s == 0:
        break
    count = 0
    nums = list(range(101))
    for comb in combinations(nums, n):
        if sum(comb) == s:
            count += 1
    print(count)