from bisect import bisect_left

def primes(n):
    sieve = bytearray((0, 0) + (1,) * (n - 1))
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = bytearray(len(range(i*i, n+1, i)))
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def search_pair(x, prime_lst):
    from itertools import takewhile
    cnt = sum(
        bisect_left(prime_lst, x - p) < len(prime_lst) and prime_lst[bisect_left(prime_lst, x - p)] == x - p
        for p in takewhile(lambda p: p <= x // 2, prime_lst)
    )
    return cnt

prime_lst = primes(1_000_000)

import sys
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(search_pair(n, prime_lst))