import sys
import math

MAX = 10_000_000

def sieve(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve

prime = sieve(MAX)
four_primes = []
for a in range(5, MAX-8+1):
    if prime[a] and prime[a+2] and prime[a+6] and prime[a+8]:
        four_primes.append(a+8)

import bisect
input_lines = sys.stdin.read().strip().split('\n')
for line in input_lines:
    n = int(line)
    if n == 0:
        break
    idx = bisect.bisect_right(four_primes, n)
    if idx == 0:
        print()
    else:
        print(four_primes[idx-1])