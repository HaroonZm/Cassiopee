from collections import Counter
from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
q = int(input())

# Pré-traitement : mappe des valeurs aux indices triés de ces valeurs
pos = {}
for idx, val in enumerate(A):
    pos.setdefault(val, []).append(idx)

for _ in range(q):
    b, e, k = map(int, input().split())
    indices = pos.get(k)
    if not indices:
        print(0)
        continue
    left = bisect_left(indices, b)
    right = bisect_left(indices, e)
    print(right - left)