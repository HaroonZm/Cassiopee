import sys
import math

MAX_N = 10**6

# Créer une table de crible de primes (True = premier)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(math.sqrt(MAX_N)) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_N+1, i):
            is_prime[j] = False

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    count = 0
    for p in range(2, n//2 + 1):
        if is_prime[p] and is_prime[n - p]:
            count += 1
    print(count)