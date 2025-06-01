from math import isqrt
import sys

N = 10_100_000
sieve = [True, False] + [True] * (N - 1)
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        sieve[i*i:N+1:i] = [False] * len(sieve[i*i:N+1:i])

quadruplet = [True, False, True, False, False, False, True, False, True]

input_lines = sys.stdin.read().split()
for line in input_lines:
    n = int(line)
    for i in range(n, 8, -1):
        if sieve[i] and sieve[i-8:i+1] == quadruplet:
            print(i)
            break