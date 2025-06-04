from functools import reduce
from itertools import count, takewhile, chain
from collections import Counter
from operator import mul

def factorization(n):
    sieve = lambda n: filter(lambda x: n % x == 0, takewhile(lambda x: x * x <= n, count(2)))
    def genf(n):
        for p in sieve(n):
            yield (p, (lambda n, p: next(i for i in count(1) if n % (p**i) or not n % (p**(i+1))))(n, p))
            n //= p ** (lambda n, p: next(i for i in count(1) if n % (p**i) or not n % (p**(i+1))))(n, p)
            while n % p == 0:
                n //= p
        if n > 1: yield (n,1)
    arr = list(genf(n))
    return arr if arr else [[n,1]]

N = int(input())
MOD = 10 ** 9 + 7
z = lambda x, y: x | y
factors = map(lambda i: Counter(dict(factorization(i))), range(N,1,-1))
merged = reduce(lambda x,y: x+y, factors, Counter())
q = (v+1 for v in merged.values())
ans = reduce(lambda a,b: a*b%MOD, q, 1)
print(ans)