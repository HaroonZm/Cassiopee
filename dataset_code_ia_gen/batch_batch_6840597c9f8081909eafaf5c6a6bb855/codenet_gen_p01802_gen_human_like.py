import math
import sys

for line in sys.stdin:
    D, E = map(int, line.split())
    if D == 0 and E == 0:
        break
    min_diff = float('inf')
    for x in range(D + 1):
        y = D - x
        cost = math.sqrt(x * x + y * y)
        diff = abs(cost - E)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)