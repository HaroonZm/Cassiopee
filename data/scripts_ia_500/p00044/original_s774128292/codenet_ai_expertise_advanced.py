import sys

MAX = 55000
primes = [True] * MAX
primes[0:2] = [False, False]
for i in range(2, int(MAX**0.5) + 1):
    if primes[i]:
        primes[i*i:MAX:i] = [False] * len(primes[i*i:MAX:i])

def nearest_primes(n):
    lower = next((x for x in range(n-1, 0, -1) if primes[x]), None)
    upper = next((x for x in range(n+1, MAX) if primes[x]), None)
    return lower, upper

for line in sys.stdin:
    n = int(line)
    m1, m2 = nearest_primes(n)
    print(m1, m2)