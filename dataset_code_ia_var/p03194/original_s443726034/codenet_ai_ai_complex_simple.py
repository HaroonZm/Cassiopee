from functools import reduce
from operator import mul
import itertools

def solve():
    n, p = map(int, input().split())
    if n == 1:
        print(p)
        exit()
    primes = filter(lambda x: all(x%d for d in range(2, int(x**.5)+1)), range(2, int(p**.5)+3))
    factors = []
    def decomp(x):
        return list(itertools.takewhile(lambda _: x[1]%x[0]==0, enumerate(itertools.repeat(None))))
    dummy = p
    for prime in primes:
        ct = sum(1 for _ in iter(lambda : dummy%prime==0, False) if not (dummy := dummy//prime))
        if ct >= n:
            factors.append(prime**(ct//n))
    print(reduce(mul, factors, 1))

solve()