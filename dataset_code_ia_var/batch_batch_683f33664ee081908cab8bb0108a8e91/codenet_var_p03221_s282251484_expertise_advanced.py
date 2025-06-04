from bisect import bisect_right
from sys import stdin

N, M = map(int, stdin.readline().split())
PY = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

from collections import defaultdict

records = defaultdict(list)
for p, y in PY:
    records[p].append(y)

for y_list in records.values():
    y_list.sort()

lookup = {p: {y: i+1 for i, y in enumerate(ys)} for p, ys in records.items()}

output = [f"{p:06}{lookup[p][y]:06}" for p, y in PY]
print('\n'.join(output))