import sys
from fractions import Fraction
from math import gcd
from functools import reduce
from operator import mul
from typing import NamedTuple

class Runner(NamedTuple):
    d: int
    v: int

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    readline = sys.stdin.readline
    while (n := int(readline())):
        runners = [Runner(*map(int, readline().split())) for _ in range(n)]
        r0 = runners[0]
        denominators = [Fraction(r0.d * ri.v, r0.v * ri.d).denominator for ri in runners[1:]]
        round_of_0 = reduce(lcm, denominators, 1)
        base_time = Fraction(r0.d * round_of_0, r0.v)
        results = (float(base_time * ri.v / ri.d) for ri in runners)
        print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()