from math import isqrt
from itertools import count, accumulate, chain
import sys

def get_prime_set(ub):
    if ub < 2: return set()
    if ub == 2: return {2}
    sieve = bytearray((ub + 1) // 2)
    for i in range(3, isqrt(ub) + 1, 2):
        if not sieve[i // 2]:
            sieve[i * i // 2 :: i] = b'\x01' * len(sieve[i * i // 2 :: i])
    return {2, *{2 * i + 1 for i, v in enumerate(sieve) if not v and 2 * i + 1 <= ub}}

def get_totient_count_range(ub, prime_set):
    totient = [i for i in range(ub + 1)]
    for p in prime_set:
        for m in range(p, ub + 1, p):
            totient[m] -= totient[m] // p
    return totient

def main():
    ub = 10**6
    primes = get_prime_set(ub)
    totients = get_totient_count_range(ub, primes)
    totients[1] = 2
    acc_totients = list(accumulate(totients))
    input()
    indices = map(int, sys.stdin)
    print(*(acc_totients[n] for n in indices), sep='\n')

if __name__ == '__main__':
    main()