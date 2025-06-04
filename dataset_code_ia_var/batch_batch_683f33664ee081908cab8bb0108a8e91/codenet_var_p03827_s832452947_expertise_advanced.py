from collections import Counter
from itertools import accumulate

n = int(input())
s = input()

# Replace conditional with sign mapping and use itertools.accumulate
deltas = (1 if c == 'I' else -1 for c in s)
peaks = list(accumulate(deltas, initial=0))  # initial=0 for starting point
print(max(peaks))