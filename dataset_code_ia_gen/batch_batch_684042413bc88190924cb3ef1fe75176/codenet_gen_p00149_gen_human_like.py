def classify(v):
    if v >= 1.1:
        return 0  # A
    elif v >= 0.6:
        return 1  # B
    elif v >= 0.2:
        return 2  # C
    else:
        return 3  # D

import sys

left_counts = [0, 0, 0, 0]
right_counts = [0, 0, 0, 0]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    l, r = map(float, line.split())
    left_counts[classify(l)] += 1
    right_counts[classify(r)] += 1

for i in range(4):
    print(left_counts[i], right_counts[i])