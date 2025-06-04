from itertools import compress, islice, count
from math import isqrt

def primes_up_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b'\0\0'
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b'\0' * ((limit - i*i)//i + 1)
    return sieve

def prime_count_in_range(n, sieve):
    return sum(islice(sieve, n+1, 2*n+1))

def main():
    import sys
    input_iter = (int(line) for line in sys.stdin)
    limits = []
    for n in input_iter:
        if n == 0:
            break
        limits.append(n)
    if not limits: return
    max_n = max(limits)
    sieve = primes_up_to(max_n*2)
    for n in limits:
        print(prime_count_in_range(n, sieve))

main()