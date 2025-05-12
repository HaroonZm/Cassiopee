from sys import stdin
readline = stdin.readline

from fractions import Fraction
from fractions import gcd
from functools import reduce

from collections import namedtuple
Runner = namedtuple('Runner', 'd v')

def common_denominator(r0, ri):
    return Fraction(r0.d * ri.v, r0.v * ri.d).denominator

def lcm(a, b):
    return a * b / gcd(a, b)

while True:
    n = int(readline())
    if n == 0:
        break
    runners = [Runner(*map(int, readline().split())) for _ in range(n)]
    
    denominators = [common_denominator(runners[0], ri) for ri in runners[1:]]
    
    round_of_0 = int(reduce(lcm, denominators))
    time = Fraction(runners[0].d * round_of_0, runners[0].v)
    
    for ri in runners:
        print(time * ri.v / ri.d)