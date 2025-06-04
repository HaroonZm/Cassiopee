from math import isqrt
from bisect import bisect_right, bisect_left

def sieve_primes(limit):
    sieve = bytearray([True]) * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b'\x00' * len(sieve[i*i:limit+1:i])
    return [i for i, is_p in enumerate(sieve) if is_p]

MAX_N = 123456
primes = sieve_primes(2 * MAX_N)

try:
    while True:
        n = int(input())
        if not n:
            break
        left = bisect_right(primes, n)
        right = bisect_right(primes, 2 * n)
        print(right - left)
except EOFError:
    pass