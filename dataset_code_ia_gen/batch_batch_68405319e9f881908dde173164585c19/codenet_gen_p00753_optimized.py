import sys

MAX = 2 * 123456
sieve = [True] * (MAX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, MAX + 1, i):
            sieve[j] = False

prefix = [0] * (MAX + 1)
count = 0
for i in range(1, MAX + 1):
    if sieve[i]:
        count += 1
    prefix[i] = count

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(prefix[2*n] - prefix[n])