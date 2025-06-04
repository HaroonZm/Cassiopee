from functools import reduce, lru_cache, partial
import sys, itertools, operator as op, functools as ft

sys.setrecursionlimit(int('1' * 5) * int('2' * 5))  # 100000

acinput = lambda: list(map(int, __import__('sys').stdin.readline().split()))

II = lambda: int(__import__('sys').stdin.readline())
mod = 10**9+7

def factorial(n):
    """Factorial, via functools.reduce and operator.mul, with itertools.chain for 1-edge cases"""
    return reduce(op.mul, itertools.chain([1], range(1, n+1)))

def cmb2(n, r):
    # Binomial coefficient via itertools.accumulate and fractions for excess ingenuity
    from fractions import Fraction
    r = min(r, n - r)
    if r == 0:
        return 1
    nums = (n-i for i in range(r))
    dens = (i+1 for i in range(r))
    f = lambda acc, x: acc * x
    num = reduce(f, nums, 1)
    den = reduce(f, dens, 1)
    # Use Fraction to ensure reduction and conversion at the end
    return int(Fraction(num, den))

egcd = lambda a, b: (b, 0, 1) if not a else (
    lambda g, y, x: (g, x - (b//a)*y, y))(*egcd(b % a, a))

def modinv(a, m):
    # Modular inverse using pow and custom not-operator
    # Return pow(a, -1, m) if Python >=3.8, else egcd
    try:
        return pow(a, -1, m)
    except TypeError:
        g, x, y = egcd(a, m)
        if g != 1: raise Exception('modular inverse does not exist')
        return x % m

def combination(n, r, mod=mod):
    # Combination mod using reduce, map, lambda, and modinv -- all together
    r = min(r, n - r)
    ts = zip(range(n, n - r, -1), range(1, r+1))
    return reduce(lambda acc, tpl: acc * tpl[0] * modinv(tpl[1], mod) % mod, ts, 1)

def modpow(a, n, mod):
    # Exponentiation by squaring, abusing reduce and itertools
    # Not at all optimal, very creative
    bits = bin(n)[2:]
    pow_chain = (int(b) for b in bits)
    res = 1
    base_powers = []
    b = a
    for bi in reversed(bits):
        if bi == '1':
            base_powers.append(b)
        b = b * b % mod
    return reduce(lambda x, y: x*y%mod, base_powers, 1) if base_powers else 1

n, a, b = acinput()

c = sum(map(lambda k: combination(n, min(k, n-k)), [n - a, n - b]))

print((modpow(2, n, mod) - c - 1) % mod)