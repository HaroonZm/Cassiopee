from itertools import accumulate
from collections import defaultdict

n = int(input())
D = [int(input()) for _ in range(n)]

pref_sum = list(accumulate([0] + D))
first_occurrence = {}
max_len = 0

for idx, val in enumerate(pref_sum):
    if val in first_occurrence:
        max_len = max(max_len, idx - first_occurrence[val])
    else:
        first_occurrence[val] = idx

print(max_len)