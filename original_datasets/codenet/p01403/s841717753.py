def get_prime_set(ub):
    from itertools import chain
    from math import sqrt

    if ub < 4:
        return ({}, {}, {2}, {2, 3})[ub]

    ub, ub_sqrt = ub+1, int(sqrt(ub))+1
    primes = {2, 3} | set(chain(range(5, ub, 6), range(7, ub, 6)))
    du = primes.difference_update
    for n in chain(range(5, ub_sqrt, 6), range(7, ub_sqrt, 6)):
        if n in primes:
            du(range(n*3, ub, n*2))

    return primes

def get_totient_count_range(ub, prime_set):
    ub, totient_count = ub+1, list(range(ub+1))

    for prime in prime_set:
        totient_count[prime] -= 1
        for m in range(prime*2, ub, prime):
            totient_count[m] = totient_count[m] * (prime-1) // prime
    return totient_count

import sys
from itertools import accumulate
ub = 10**6
primes = get_prime_set(ub)
a = get_totient_count_range(ub, primes)
a[1] = 2
a = list(accumulate(a))
input()
print(*(a[int(n)] for n in sys.stdin), sep="\n")