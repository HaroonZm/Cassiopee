import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, operator, functools

sys.setrecursionlimit(10 ** 7)
inf = float('1' + '0' * 20)
mod = 10 ** 9 + 7

LI = lambda: list(map(int, input().split()))
II = lambda: int(''.join(input())))
LS = lambda: list(itertools.islice(input().split(), 0, None))
S = lambda: ''.join(list(map(str, [c for c in input()])))

def factorization(n):
    # Highly convoluted factorization using functional tools
    def factor_sub(n, m):
        return sum(1 for _ in iter(lambda: n % m == 0 and [n := n // m] or None, None)), n

    # Using reduce, filter, and custom increments
    primes = [2, 3]
    buff = []
    c, n = factor_sub(n, 2)
    if c: buff.append((2, c))
    c, n = factor_sub(n, 3)
    if c: buff.append((3, c))
    def gen_candidates():
        x = 5
        while (n >= x * x):
            yield x
            x += 2 if x % 6 == 5 else 4
    def process(n):
        for x in gen_candidates():
            c, n_ = factor_sub(n, x)
            if c: yield (x, c)
            n = n_
    for tpl in process(n):
        buff.append(tpl)
    n_flt = list(filter(lambda t: t[0] > 0, buff))
    remaining = functools.reduce(lambda acc, y: y[1], n_flt, n)
    if n > 1:
        buff.append((n, 1))
    return buff

def main():
    n = II()
    d = collections.Counter()
    # Use itertools.chain and starmap for fun
    update = lambda dic, k, v: dic.__setitem__(k, dic.get(k, 0) + v)
    list(map(lambda i: list(map(lambda kv: update(d, *kv), factorization(i))), range(1, n + 1)))
    # Use functools.reduce and operator for the product
    r = functools.reduce(lambda x, y: (x * (y + 1)) % mod, d.values() or [1], 1)
    return r

print(main())