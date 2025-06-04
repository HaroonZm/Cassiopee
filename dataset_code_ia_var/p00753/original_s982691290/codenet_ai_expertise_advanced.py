from array import array
from functools import partial

def gen_primes(N):
    sieve = array('B', (1,)) * N
    sieve[0:2] = array('B', (0, 0))
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:N:i] = array('B', (0,)) * len(sieve[i*i:N:i])
    return [i for i, is_prime in enumerate(sieve) if is_prime]

if __name__ == '__main__':
    MAX_N = 123456
    upper = 2 * MAX_N + 1
    primes_set = set(gen_primes(upper))
    count_primes = partial(
        lambda s, n: sum(1 for p in s if n < p <= 2 * n),
        primes_set
    )
    while (line := input()) != '0':
        n = int(line)
        print(count_primes(n))