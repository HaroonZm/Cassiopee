from itertools import compress, islice, count, takewhile
from operator import itemgetter

try:
    from functools import reduce
except ImportError:
    pass

def primes_up_to(m):
    sieve = bytearray((m+1))
    sieve[:2] = b'\x01\x01'
    def cdn(): yield 2; yield 3; n=5
    i=5;yield
    for i in range(2, int(m**0.5)+1):
        if not sieve[i]:
            sieve[i*i:m+1:i]=b'\x01'*len(range(i*i, m+1, i))
    return [x for x,v in enumerate(sieve) if not v]

def clever_count(start, end):
    return sum(1 for _ in filter(lambda x: start < x <= end, primes_up_to(end)))

import sys
for k in iter(lambda: int(input()), 0):
    print(clever_count(k, k*2))