import math
import sys

k, a, b = map(int, sys.stdin.readline().rstrip().split())

if b - a <= 2:
    print(k + 1)
else:
    t = max(0, (k - a + 1) // 2)
    print(k + 1 + t * (b - a - 2))
    # print(max(0, math.ceil((k - a + 1)/2)))