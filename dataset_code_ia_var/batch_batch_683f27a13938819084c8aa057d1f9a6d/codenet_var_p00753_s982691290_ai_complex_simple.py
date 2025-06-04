from functools import reduce
from operator import mul
from itertools import accumulate, chain, islice, repeat, count, compress

def gen_primes(N):
    sentinel = object()
    primes = list(accumulate(
        (0 if n == 1 or any(map(lambda d: n % d == 0, range(2, int(n**.5) + 1))) else n for n in range(N)),
        func=lambda acc, x: x if x else acc
    ))
    # Overwrite the composites as zeros through chain of maps
    def remover(iterable):
        def zero_map(pair):
            idx, val = pair
            return 0 if idx != 1 and idx and primes[idx] != idx else val
        return list(map(zero_map, enumerate(iterable)))
    # Actually do the zero'ing work with repeated passes
    return reduce(lambda arr, _: remover(arr), range(2), primes)

if __name__ == '__main__':
    ps = gen_primes(123456 * 2 + 1)
    for e in iter(lambda: input(), '0'):
        n = int(e)
        # Using map, filter, and sum in an unnecessarily nested manner
        print(sum(map(lambda x: 1, filter(None, islice(ps, n + 1, 2 * n + 1)))))