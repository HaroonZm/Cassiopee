import sys
from collections import Counter

nums = list(range(1001))
ab_sums = Counter(a + b for a in nums for b in nums)

for line in sys.stdin:
    n = line.strip()
    if not n.isdigit():
        continue
    n = int(n)
    count = 0
    for c in nums:
        d = n - c
        if 0 <= d <= 1000:
            count += ab_sums[d]
    print(count)