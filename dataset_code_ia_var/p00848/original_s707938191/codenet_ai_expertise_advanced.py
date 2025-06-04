from itertools import islice
from math import isqrt
from sys import stdin

r = 1121

# Sieve of Eratosthenes with advanced slicing
p = bytearray([1]) * r
p[0:2] = b'\x00\x00'
for i in range(2, isqrt(r) + 1):
    if p[i]:
        p[i*i:r:i] = b'\x00' * len(p[i*i:r:i])

prime = [i for i, flag in enumerate(p) if flag]

# Dynamic programming table (using generator expressions for efficiency)
dp = [bytearray(r) for _ in range(15)]
dp[0][0] = 1
for idx, pr in enumerate(prime):
    for k in range(min(idx + 1, 14), 0, -1):
        row, prev_row = dp[k], dp[k - 1]
        for j in range(pr, r):
            row[j] += prev_row[j - pr]

for line in stdin:
    n, k = map(int, line.split())
    if n == 0:
        break
    print(dp[k][n])