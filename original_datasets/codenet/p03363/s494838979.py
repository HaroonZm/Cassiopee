import numpy as np
from collections import Counter

n = int(input())
a = [0] + list(map(int, input().split()))
cumsum = np.cumsum(a)
c = Counter(cumsum)
cnt = 0
for i in c.values():
    if i > 1:
        cnt += int(i * (i-1) / 2)
print(cnt)