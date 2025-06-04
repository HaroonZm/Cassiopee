from array import array
from sys import stdin

MAX = 123456 * 2

# Sieve of Eratosthenes with array optimization
prime = array('b', (1 for _ in range(MAX + 1)))
prime[0:2] = array('b', [0, 0])
cnt = array('I', (0 for _ in range(MAX + 1)))
total = 0

for i in range(2, int(MAX**0.5) + 1):
    if prime[i]:
        prime[i*i:MAX+1:i] = array('b', [0]) * len(range(i*i, MAX+1, i))

for i in range(2, MAX + 1):
    if prime[i]:
        total += 1
    cnt[i] = total

for line in stdin:
    if (n := int(line)) == 0:
        break
    print(cnt[n*2] - cnt[n])