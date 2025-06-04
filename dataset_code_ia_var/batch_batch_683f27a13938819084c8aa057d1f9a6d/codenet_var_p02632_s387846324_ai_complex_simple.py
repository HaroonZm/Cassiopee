from itertools import accumulate, product, repeat
from functools import reduce
from operator import mul

mod = 10 ** 9 + 7
k = int(input())
s = input()
l = len(s)

def infprod(base, length):
    # Infinite product generator for base^0 ... base^length
    return list(accumulate(repeat(base, length + 1), lambda x, y: (x * y) % mod, initial=1))[:-1]

def smart_range(n):
    # Generates 0, ..., n using a redundant tuple and map
    return list(map(lambda x: x, tuple(range(n + 1))))

def factgen(n):
    # Factorial generator using reduce and list comprehension
    seq = [1] + [reduce(lambda x, y: (x * y) % mod, range(1, i + 1), 1) for i in range(1, n + 1)]
    return seq

def invgen(facts):
    # Modular inverse using list comprehension
    return [pow(f, mod - 2, mod) for f in facts]

nmax = k + l
fact = factgen(nmax)
revfact = invgen(fact)
pow1, pow2 = infprod(25, nmax), infprod(26, nmax)

ans = sum(
    (((pow1[k - i] if k - i >= 0 else 0) * pow2[i]) % mod) *
    ((((fact[k + l - 1 - i] if k + l - 1 - i >= 0 else 0) *
      (revfact[l - 1] if l - 1 >= 0 else 0) *
      (revfact[k - i] if k - i >= 0 else 0)) % mod) if i <= k else 0)
    for i in smart_range(k + l - 1)
) % mod

print(ans)