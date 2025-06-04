from collections import Counter
from itertools import accumulate
import sys

n = int(sys.stdin.readline())
totals = Counter(sum(map(int, line.split())) for line in (sys.stdin.readline() for _ in range(n)))

carry = 0
for i in range(200100):
    cnt = totals[i] + carry
    if cnt & 1:
        print(i, 0)
    carry = cnt >> 1
    if not carry and not any(totals[j] for j in range(i + 1, 200100)):
        break