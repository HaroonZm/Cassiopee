from sys import stdin
from itertools import combinations

for line in stdin:
    n, s = map(int, line.split())
    if n == 0 and s == 0:
        break
    count = 0
    for combo in combinations(range(10), n):
        if sum(combo) == s:
            count += 1
    print(count)