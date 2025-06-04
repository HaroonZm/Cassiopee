from functools import reduce
from itertools import takewhile, chain, count
from operator import mul

a = []
l = [2]
while True:
    try:
        a.append(int(input()))
    except BaseException:
        break

def primes(n):
    def not_divisible(primes_list, x):
        return all(x % p for p in takewhile(lambda p: p*p <= x, primes_list))
    primes_gen = (2,) + tuple(
        filter(
            lambda x: not_divisible(primes_so_far, x),
            range(3, n + 1, 2)
        )
        for primes_so_far in [()]
    )
    result = [2]
    for p in range(3, n+1, 2):
        if all(p % q for q in result if q*q <= p):
            result.append(p)
    return result

z = primes(max(a) if a else 2)

for k in a:
    y = sum(map(lambda x: 1, filter(lambda q: q <= k, z)))
    print(y)