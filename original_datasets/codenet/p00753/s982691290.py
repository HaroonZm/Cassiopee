def gen_primes(N):
    from itertools import compress
    sieve = list(range(N))
    sieve[1] = 0
    for i in range(2, int(N**.5) + 1):
        sieve[i * 2::i] = [0] * len(sieve[i * 2::i])
    return sieve

if __name__ == '__main__':
    ps = gen_primes(123456 * 2 + 1)
    for e in iter(input, '0'):
        n = int(e)
        print(sum(1 for p in ps[n + 1:2 * n + 1] if p))