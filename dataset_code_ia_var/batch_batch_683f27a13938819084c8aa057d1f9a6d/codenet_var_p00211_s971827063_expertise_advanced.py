from math import gcd
from functools import reduce
from sys import stdin

def lcm(*args):
    return reduce(lambda x, y: x * y // gcd(x, y), args, 1)

def read_int():
    while True:
        line = stdin.readline()
        if not line:
            return None
        stripped = line.strip()
        if stripped:
            return int(stripped)

while True:
    n = read_int()
    if not n:
        break
    s = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    denoms = tuple(r[1] for r in s)
    lcm_denoms = lcm(*denoms)
    num_factors = tuple(r[0] * lcm_denoms // r[1] for r in s)
    lcm_numerators = lcm(*num_factors)
    results = (str(lcm_numerators * r[1] // lcm_denoms // r[0]) for r in s)
    print('\n'.join(results))