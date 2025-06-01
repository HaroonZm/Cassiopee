import sys

MAX_N = 10**6
is_prime = [True] * (MAX_N + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_N + 1, i):
            is_prime[j] = False

def count_goldbach_pairs(n):
    count = 0
    for p in range(2, n//2 + 1):
        if is_prime[p] and is_prime[n - p]:
            count += 1
    return count

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(count_goldbach_pairs(n))