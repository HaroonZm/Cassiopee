import sys
import math

input = sys.stdin.readline
N = int(input())
t = [int(input()) for _ in range(N)]
max_t = max(t)

min_sum = float('inf')
for L in range(max_t, max_t + 10001):
    s = 0
    for x in t:
        r = L % x
        s += (0 if r == 0 else x - r)
    if s < min_sum:
        min_sum = s
print(min_sum)