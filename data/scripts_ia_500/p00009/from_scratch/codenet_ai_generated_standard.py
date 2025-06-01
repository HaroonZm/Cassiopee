import sys

MAX_N = 10**6
sieve = [True] * (MAX_N + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MAX_N**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, MAX_N + 1, i):
            sieve[j] = False
prefix = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    prefix[i] = prefix[i-1] + (1 if sieve[i] else 0)
for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
    n = int(n)
    print(prefix[n])