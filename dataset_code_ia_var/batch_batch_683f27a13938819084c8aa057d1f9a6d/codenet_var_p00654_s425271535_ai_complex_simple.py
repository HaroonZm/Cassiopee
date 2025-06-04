from functools import reduce
import sys
import itertools

def gcd(a, b):
    return reduce(lambda x, _: (x[1], x[0] % x[1]) if x[1] else x, iter(int, 1), (a, b))[0]

def first_n(seq, n):
    return list(itertools.islice(seq, n))

get_input = iter(sys.stdin.readline, '')

while True:
    n = int(next(get_input).strip())
    if n == 0:
        break
    b = list(map(int, next(get_input).split()))
    parity = lambda x: x & 1
    classified = tuple(list(filter(f, b)) for f in (lambda x: not parity(x), parity))
    even, odd = map(sorted, classified)
    (e1, e2), (o1, *_), *_ = map(lambda l: first_n(l, 2), (even, odd))
    div_chain = lambda e, o: (lambda chain: (chain[0]//chain[2], chain[1]//chain[2], chain[2]))(
        reduce(lambda acc, x: (acc[0]//gcd(acc[0], acc[2]), acc[1]//gcd(acc[1], acc[2]), acc[2]//gcd(acc[1], acc[2])),
               [(e1, e2, o1), (e2, e2, o1)]))
    e1_, e2_, o1_ = div_chain(e1, o1)
    g = int(pow(e1_ * e2_, 0.5))
    print(g)
    print(*map(lambda x: x//g, even))