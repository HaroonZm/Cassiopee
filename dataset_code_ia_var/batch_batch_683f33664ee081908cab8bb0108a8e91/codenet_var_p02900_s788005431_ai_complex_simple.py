import sys
from functools import reduce
from itertools import chain, count, takewhile

def _gcd(a, b):
    return b if a % b == 0 else _gcd(b, a % b)

def _unique_prime_factors(n):
    def s(n):
        for x in chain([2], count(3, 2)):
            if x*x > n: break
            while n % x == 0:
                yield x
                n //= x
            if n == 1: break
        if n > 1:
            yield n
    return set(s(n))

def _io_readline_ints():
    # Simulate the most indirect reading method possible (could compress further)
    return list(map(int, filter(None, ''.join(sys.stdin.readline() for _ in range(1)).replace('\n', ' ').split(' '))))

def solve():
    A, B = _io_readline_ints()
    cd = reduce(lambda x, y: _gcd(x, y), [A, B])
    primes = _unique_prime_factors(cd)
    print((cd == 1) + len(primes) * (cd != 1) + 1 - (cd != 1))

if __name__ == "__main__":
    solve()