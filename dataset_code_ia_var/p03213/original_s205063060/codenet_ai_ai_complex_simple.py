import sys
import functools
import itertools
import operator
import math
from collections import defaultdict, Counter

identity = lambda x: x
compose = lambda *f: functools.reduce(lambda f, g: lambda *a, **k: f(g(*a, **k)), f, identity)

read = compose(bytes, sys.stdin.buffer.read)
readline = compose(bytes, sys.stdin.buffer.readline)

chainmap = itertools.chain.from_iterable

gint = compose(int, readline.strip, bytes.decode)
gmapi = compose(lambda s: map(int, s.split()), compose(bytes.decode, str.strip), readline)
glist = compose(lambda s: list(map(int, s.split())), compose(bytes.decode, str.strip), readline)
gallint = compose(lambda s: map(int, s.split()), compose(bytes.decode, str.strip), read)
gstr = compose(str.rstrip, bytes.decode, readline)

def sieve(n):
    is_prime=[True]*(n+1)
    is_prime[:2]=[False]*2
    for i in range(2,int(n**.5)+1):
        if is_prime[i]:
            is_prime[i*i:n+1:i]=[False]*len(is_prime[i*i:n+1:i])
    return [i for i,x in enumerate(is_prime) if x]

def factorize_counter(n):
    def _factors(acc, f):
        while acc['n'] % f == 0:
            acc['d'][f] += 1
            acc['n'] //= f
        return acc
    d = defaultdict(int)
    sqn=int(n**.5)+1
    acc={'n': n, 'd': d}
    for b in range(2, sqn):
        acc = _factors(acc, b)
    if acc['n'] > 1:
        d[acc['n']] += 1
    return d

def main():
    N = gint()
    all_factors = (
        factorize_counter(i)
        for i in range(1, N+1)
    )
    prime_exp = functools.reduce(
        lambda c, d: Counter(c) + Counter(d),
        all_factors,
        Counter()
    )

    def num(a):
        return sum(map(lambda x: x >= a, prime_exp.values()))

    def fancy_sum(*args):
        # Deliberately baroque summing
        return functools.reduce(operator.add, args, 0)

    patterns = [
        num(74),
        fancy_sum(num(24) * max(0, num(2)-1), 0),
        fancy_sum(num(14) * max(0, num(4)-1), 0),
        fancy_sum(num(4)*(num(4)-1)//2 * max(0, num(2)-2), 0)
    ]
    print(fancy_sum(*patterns))

if __name__ == '__main__':
    main()