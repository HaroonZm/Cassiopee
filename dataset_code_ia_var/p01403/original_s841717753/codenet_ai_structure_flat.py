from itertools import chain, accumulate
from math import sqrt
import sys

ub = 10**6

if ub < 4:
    if ub == 0:
        primes = {}
    elif ub == 1:
        primes = {}
    elif ub == 2:
        primes = {2}
    else:
        primes = {2, 3}
else:
    primes = {2, 3}
    for i in range(5, ub+1, 6):
        primes.add(i)
    for i in range(7, ub+1, 6):
        primes.add(i)
    ub1 = ub + 1
    ub_sqrt = int(sqrt(ub)) + 1
    for n in chain(range(5, ub_sqrt, 6), range(7, ub_sqrt, 6)):
        if n in primes:
            for m in range(n*3, ub1, n*2):
                if m in primes:
                    primes.discard(m)

totient_count = list(range(ub+2))
for prime in primes:
    totient_count[prime] -= 1
    for m in range(prime*2, ub+1, prime):
        totient_count[m] = totient_count[m] * (prime-1) // prime

totient_count[1] = 2

a = list(accumulate(totient_count))

input()
for n in sys.stdin:
    n = int(n)
    print(a[n])