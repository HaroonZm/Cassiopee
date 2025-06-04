from sys import stdin
from functools import partial

h, n = map(int, stdin.readline().split())
state_lst = [0] * h
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    state_lst[y] |= 1 << x

masks = (0b0011, 0b0110, 0b1100)
all_mask = 0b1111
INF = float('-inf')
dp = [ [-INF] * 16 for _ in range(h + 1) ]
dp[0][all_mask] = 0

for i, state in enumerate(state_lst):
    dp_next = dp[i+1]
    for mask in masks:
        if state & mask: continue
        for pre_mask, val in enumerate(dp[i]):
            if pre_mask & mask: continue
            dp_next[state | mask] = max(dp_next[state | mask], val + 1)
    if not state:
        dp_next[all_mask] = max(dp_next[all_mask], dp[i][0] + 2)
    dp_next[state] = max(dp_next[state], max(dp[i]))

print(max(dp[h]))