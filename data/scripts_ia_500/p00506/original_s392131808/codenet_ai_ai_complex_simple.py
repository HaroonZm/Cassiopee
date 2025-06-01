from functools import reduce
from math import gcd as math_gcd
import operator
import itertools

n = (lambda s: int(''.join(map(chr, map(lambda x: x - 48, list(bytes(s, 'ascii')))))))(input())
L = (lambda f: list(map(int, f.split())))(input())
g = reduce((lambda x, y: (lambda a, b: (lambda r: r if r else a)(math_gcd(a, b)))(x, y))(0, 0), L)

def complex_divisors(k):
    return list(itertools.compress(range(1, k+1), map((lambda d: (lambda: k % d == 0)()), range(1, k+1))))

print('\n'.join(map(str, filter(lambda x: g % x == 0, range(1, g + 1)))))