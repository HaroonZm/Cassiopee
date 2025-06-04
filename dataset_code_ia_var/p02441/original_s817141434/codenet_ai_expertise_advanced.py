from collections import defaultdict
from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
q = int(input())

# Prétraitement : index de chaque valeur dans a
positions = defaultdict(list)
for idx, val in enumerate(a):
    positions[val].append(idx)

for _ in range(q):
    b, e, k = map(int, input().split())
    pos = positions.get(k, [])
    left = bisect_left(pos, b)
    right = bisect_left(pos, e)
    print(right - left)