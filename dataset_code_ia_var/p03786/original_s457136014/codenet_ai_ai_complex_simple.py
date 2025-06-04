from functools import reduce
from itertools import accumulate, count, takewhile
n = int(raw_input())
a = list(map(int, raw_input().split()))
a = sorted(a)

sums = list(accumulate(a))
idxs = list(takewhile(lambda t: t[1]*2 >= a[t[0]] , enumerate(sums)))
try:
    m = max((i for i, s in enumerate(sums) if s * 2 < a[i]))
except ValueError:
    m = 0
print(n - m)