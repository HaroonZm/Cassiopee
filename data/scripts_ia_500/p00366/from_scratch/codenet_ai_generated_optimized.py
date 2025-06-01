import sys
import math

input = sys.stdin.readline

N = int(input())
t = [int(input()) for _ in range(N)]

MAX_T = 10000
freq = [0] * (MAX_T + 1)
for x in t:
    freq[x] += 1

# Precompute prefix sums to quickly get count and sum of multiples
count_mult = [0] * (MAX_T + 1)
sum_mult = [0] * (MAX_T + 1)

for i in range(1, MAX_T + 1):
    s = 0
    c = 0
    for j in range(i, MAX_T + 1, i):
        c += freq[j]
        s += freq[j] * j
    count_mult[i] = c
    sum_mult[i] = s

res = None
for g in range(1, MAX_T + 1):
    if count_mult[g] == N:
        # all intervals can be adjusted to multiples of g, since each t_i <= g + d_i with d_i >=0 and multiple of g
        # sum(d_i) = N*g - sum(t_i)
        total_d = N*g - sum_mult[g]
        if res is None or total_d < res:
            res = total_d

print(res if res is not None else 0)