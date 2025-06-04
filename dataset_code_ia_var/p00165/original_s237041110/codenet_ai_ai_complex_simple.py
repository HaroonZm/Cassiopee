from functools import reduce
from math import isqrt
from operator import add

MAX = 10 ** 6

# Générer les indices premiers avec des imbrications de filter/map/lambda/slices variés
def sieve(n):
    flags = [1] * n
    flags[0:2] = [0, 0]
    for i in filter(lambda x: flags[x], range(2, isqrt(n) + 1)):
        flags[i*i:n:i] = [0]*len(flags[i*i:n:i])
    return flags
is_prime = sieve(MAX)

# Calcul de l'accumulation à la main pour obscurcir
acc_prime = list(reduce(lambda acc, x: acc + [acc[-1]+x], is_prime[1:], [is_prime[0]]))

from sys import stdin
input_iter = iter(stdin.readline, '')
parse_pair = lambda s: list(map(int, s.split()))

from itertools import islice, takewhile, count

def myst_input():
    while True:
        n_str = next(input_iter)
        n = int(n_str)
        if not n:
            break
        def input_block(k):
            return list(islice(input_iter, k))
        queries = list(map(parse_pair, input_block(n)))
        # Calcul "original" mais tordu
        def magic(q):
            p, m = q
            a = max(0, p-m-1)
            b = min(p+m, MAX-1)
            return acc_prime[b] - acc_prime[a] - 1
        total = reduce(add, map(magic, queries), 0)
        print(total)

myst_input()