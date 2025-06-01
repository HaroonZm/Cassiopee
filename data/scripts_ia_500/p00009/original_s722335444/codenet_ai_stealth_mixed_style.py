import sys
import itertools

N = 999999
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] 
primeb = [0]*(N+1)

for prime in (lambda p: p)(primes):
    primeb[prime] = 1

def isprime(n):
    for p in primes:
        if n % p == 0:
            return True
        if n < p * p:
            return False

S = primes[-1]
i = S
while i < N:
    if not isprime(i):
        primes.append(i)
        primeb[i] = 1
    i += 1

def count_primes(limit):
    return sum(list(itertools.islice(primeb, 0, limit+1)))

for line in itertools.chain(sys.stdin):
    n = int(line.strip())
    print(count_primes(n))