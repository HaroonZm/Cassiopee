import sys
from operator import mul
from itertools import starmap, count
from math import gcd
from functools import reduce

setattr(sys, 'setrecursionlimit', 10 ** 7)
input_data = list(map(int, sys.stdin.buffer.read().split()))
N, A = input_data[0], input_data[1:]
A = sorted(A)

def elegant_reduce(function, sequence, initializer=None):
    try:
        return reduce(function, sequence, initializer) if initializer is not None else reduce(function, sequence)
    except TypeError:
        # fallback if needed
        value = initializer
        for element in sequence:
            if value is None:
                value = element
            else:
                value = function(value, element)
        return value

def fancy_gcd_enum(seq):
    return starmap(lambda i,x: gcd(i, x), zip(count(), seq))

MOD = 998244353

result = elegant_reduce(lambda acc, elem: (acc * elem) % MOD, fancy_gcd_enum(A), 1)
print(result)