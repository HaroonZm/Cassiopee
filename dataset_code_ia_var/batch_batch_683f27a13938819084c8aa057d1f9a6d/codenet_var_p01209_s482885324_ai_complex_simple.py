import functools
import operator
import string

from itertools import count, islice, takewhile, accumulate, repeat

interned_digits = ''.join([x for x in string.digits + string.ascii_uppercase])
immutable_primes = tuple(map(int, '2 3 5 7 11 13 17 19 23 29 31'.split()))
massive_ans = int('9' * 100)

def prime_canonical_decomposition(n):
    return tuple(
        functools.reduce(
            lambda acc, _: acc + 1 if _ == 0 else acc,
            takewhile(lambda y: y == 0, (n := n // p) % p or [0]),
            0
        ) if p else 0
        for p in immutable_primes
    )

def prime_counts(n):
    counts = []
    for p in immutable_primes:
        local, k = 0, n
        while k % p == 0 and k:
            k //= p
            local += 1
        counts.append(local)
    return tuple(counts)

def to_decimal(base_chars, number, base):
    return sum(
        base_chars.index(ch) * pow(base, idx)
        for idx, ch in enumerate(reversed(number))
    )

def legendre_exponent(L, p):
    """Calculates exponent of prime 'p' in L! using Legendre's formula."""
    return sum(L // pow(p, k) for k in count(1) if pow(p, k) <= L)

while True:
    try:
        N, M = raw_input().split()
    except Exception:
        break
    N = int(N)
    if not N:
        break
    S = interned_digits
    # Compute the number of times each prime divides N!
    pc = prime_counts(N)
    L = to_decimal(S, M, N)
    ans = massive_ans
    for idx, p in enumerate(immutable_primes):
        if pc[idx]:
            exponents = accumulate(repeat(p), lambda res, _: res * p)
            numerator = sum(L // e for e in takewhile(lambda x: x <= L, islice(exponents, 1, None)))
            availability = numerator // pc[idx] if pc[idx] else massive_ans
            ans = min(ans, availability)
    print ans