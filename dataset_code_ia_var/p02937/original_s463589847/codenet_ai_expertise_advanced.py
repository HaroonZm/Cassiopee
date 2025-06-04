from collections import defaultdict
from bisect import bisect_right
from sys import exit
from string import ascii_lowercase

S, T = input(), input()
positions = defaultdict(list)
for idx, char in enumerate(S):
    positions[char].append(idx)

if any(not positions[c] for c in set(T)):
    print(-1)
    exit()

id, ans, n = -1, 0, len(S)
for c in T:
    idx_list = positions[c]
    i = bisect_right(idx_list, id)
    if i == len(idx_list):
        ans += n
        id = idx_list[0]
    else:
        id = idx_list[i]

print(ans + id + 1)