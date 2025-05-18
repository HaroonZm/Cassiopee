#!/usr/bin/env python3

import array
import bisect

MAX_PRIME = 1299709

def sieve_of_eratosthenes(end, typecode="L"):
    assert end > 1
    is_prime = array.array("B", (True for i in range(end)))
    is_prime[0] = False
    is_prime[1] = False
    primes = array.array(typecode)
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return primes

def main():
    primes = sieve_of_eratosthenes(MAX_PRIME + 1)

    def length_of_gap_containing(n):
        index = bisect.bisect_left(primes, n)
        next_prime = primes[index]
        if next_prime == n:
            return 0
        else:
            prev_prime = primes[index - 1]
            return next_prime - prev_prime
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            print(length_of_gap_containing(n))

if __name__ == '__main__':
    main()