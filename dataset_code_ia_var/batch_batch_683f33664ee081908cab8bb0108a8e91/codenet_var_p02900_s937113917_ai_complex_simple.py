from functools import reduce
from math import isqrt
from operator import mul

A, B = map(int, input().split())

prime_decompose = lambda n: list(
    reduce(
        lambda acc, val: acc + [val[0]]*val[1],
        (
            (p, lambda x, y=0: (lambda f: f(f,x,y))(lambda f, n, c: f(f, n//p, c+1) if n%p==0 else c))(n)
            for p in range(2, isqrt(n)+1)
            if any((n:=n) and not n%p or None for _ in [0]) or None
        ),
        [] if n > 1 else []
    ) + ([n] if n > 1 else [])
)

def compute_prime_factors_set(num):
    s, x = set(), num
    for p in range(2, isqrt(x)+2):
        while x%p==0:
            s.add(p)
            x//=p
    if x>1:s.add(x)
    return s

A_dec = compute_prime_factors_set(A)
B_dec = compute_prime_factors_set(B)

ans = sum(map(lambda x: 1, filter(lambda x: x in B_dec, A_dec)))+1

print(ans)