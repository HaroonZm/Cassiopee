import sys

MAX = 10000
sieve = [True] * (MAX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, MAX + 1, i):
            sieve[j] = False

for line in sys.stdin:
    if not line.strip():
        continue
    N = int(line)
    count = sum(1 for i in range(1, N+1) if sieve[i] and sieve[N - i + 1])
    print(count)