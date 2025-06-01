from math import isqrt
import bisect
import sys

LENGTH = 10**6

def eratosthenes(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b'\x00\x00'
    sieve[4::2] = b'\x00' * ((n - 4) // 2 +1)
    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if sieve[i]:
            sieve[i*i:n+1:i*2] = b'\x00' * ((n - i*i) // (i*2) +1)
    return sieve

primes_sieve = eratosthenes(LENGTH)
prime_list = [i for i, prime in enumerate(primes_sieve) if prime]

input = sys.stdin.readline
while (input_count := int(input())) != 0:
    pay = 0
    for _ in range(input_count):
        p, m = map(int, input().split())
        lower, upper = max(p - m, 0), min(p + m, LENGTH)
        left = bisect.bisect_left(prime_list, lower)
        right = bisect.bisect_right(prime_list, upper)
        pay += max(0, right - left - 1)
    print(pay)