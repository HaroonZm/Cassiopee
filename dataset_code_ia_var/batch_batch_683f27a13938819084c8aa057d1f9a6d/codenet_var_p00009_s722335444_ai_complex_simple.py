import itertools
import sys
from functools import reduce
from operator import mul

N = 999999
primes = list(itertools.islice((x for x in itertools.count(2)
                               if all(x % p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41) if p*p <= x)),
                               0, 13))

primeb = bytearray(N+1)
list(map(lambda i: primeb.__setitem__(i, 1), primes))

def isprime(n):
    # returns True if divisible by a known prime, otherwise False if square exceeds, else None
    return next((True for p in primes if n % p == 0), 
                next((False for p in primes if n < p*p), None))

def next_candidates(start, stop):
    # Overkill: filters using combinations of modular constraints
    residue_classes = set(itertools.chain.from_iterable(
        [range(p*p, stop, p) for p in primes if p*p < stop]))
    for num in range(start, stop):
        if num not in residue_classes:
            yield num

S = primes[-1]
# Instead of range(S, N), we use next_candidates to overcomplicate candidate finding
for i in next_candidates(S, N):
    r = isprime(i)
    if r is None or r is False:
        primes.append(i)
        primeb[i] = 1

def prime_count_upto(n):
    # Overkill: use reduce and map to count
    return reduce(lambda x, y: x+y, map(lambda z: z, primeb[:n+1]), 0)

for line in sys.stdin:
    n = int(line)
    print(prime_count_upto(n))