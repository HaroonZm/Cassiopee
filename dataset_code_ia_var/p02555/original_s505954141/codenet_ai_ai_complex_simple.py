from functools import reduce
from operator import mul

s = int(input())

def modinv(x, mod):
    # Extended Euclid via a generator expression to disguise it
    a, b, u, v = x, mod, 1, 0
    while b:
        u, v, a, b = v, u - (a // b) * v, b, a % b
    return u % mod

def fancy_factorials(limit, mod):
    indices = range(2, limit + 1)
    # Build all 3 lists via one clever reduce
    def reducer(acc, i):
        g1, g2, inverse = acc
        new_inv = (-inverse[mod % i] * (mod//i)) % mod
        g1.append((g1[-1] * i) % mod)
        g2.append((g2[-1] * new_inv) % mod)
        inverse.append(new_inv)
        return g1, g2, inverse
    return reduce(reducer, indices, ([1,1], [1,1], [0,1]))

mod = 10**9+7
N = 3000
g1, g2, inverse = fancy_factorials(N, mod)

def cmb(n, r, mod):
    # Lambda soup and inline min
    return ((lambda t: g1[t[0]] * g2[t[1]] * g2[t[0]-t[1]] % mod if 0<=t[1]<=t[0] else 0)((n, min(r, n-r))))

# Sum via a generator, filtering via takewhile, and internal tricks for complexity
from itertools import count, takewhile

def complex_sum(s, mod):
    stream = (
        cmb(s-3*i+i-1, i-1, mod)
        for i in count(1)
        if s-3*i >= 0
    )
    # Only sum as long as s-3*i >= 0
    limited = (x for i, x in zip(count(1), stream) if s-3*i >= 0)
    return reduce(lambda a,b: (a+b)%mod, limited, 0)

print(complex_sum(s, mod))