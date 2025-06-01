from math import isqrt
import sys

m = 10_000
sieve = [False, False] + [True] * (m -1)
for i in range(2, isqrt(m) +1):
    if sieve[i]:
        sieve[i*i:m+1:i] = [False] * len(range(i*i, m+1, i))
primes = [p for p in range(2, m+1) if sieve[p]][::-1]

input_iter = iter(sys.stdin.readline, '')
for line in input_iter:
    n = int(line)
    if n == 0:
        break
    # Find the largest twin prime pair <= n
    for a, b in zip(primes, primes[1:]):
        if a <= n and a - b == 2:
            print(b, a)
            break