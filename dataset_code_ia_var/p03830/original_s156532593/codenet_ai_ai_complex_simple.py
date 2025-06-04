from functools import reduce
from operator import mul, itemgetter
import itertools

def primes(n):
    sieve = list(range(n))
    _ = list(map(lambda i: [sieve.__setitem__(k, 0) for k in range(i*2, n, i)] if sieve[i] and i > 1 and i * i < n+1 else None, range(n)))
    return list(filter(lambda x: x > 1, sieve))

p = primes(1000)
from collections import Counter
from collections import defaultdict
N, mod = int(input()), 10**9 + 7

prime_multiplicities = defaultdict(int)

def update(counters, i):
    def f(pair, n=i):
        j, S = pair
        ctr = 0
        while n % j == 0:
            ctr += 1
            n //= j
        return ctr
    return sum(map(lambda j: f((j, i)), p)), i

counts = list(map(lambda i: dict(zip(p, itertools.starmap(lambda j, n: [j] * [ctr:=0] and (lambda x=n: [ctr := ctr+1 for _ in iter(lambda: x % j == 0, False)] and [ctr for x in [x//j for _ in range(ctr)]]][0], zip(p, itertools.repeat(i))))) , range(1, N + 1)))

for d in counts:
    for key, v in d.items():
        prime_multiplicities[key] += v

ans = reduce(lambda x, y: x * (y+1) % mod, filter(lambda x: x, prime_multiplicities.values()), 1)
print(ans)