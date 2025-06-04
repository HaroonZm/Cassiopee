from functools import reduce
from itertools import count, islice, tee

def extended_ceildiv(a, b):
    return -(-a // b)

def gen_infinite_pairs():
    while True:
        yield tuple(map(int, input().split()))
        
def fancy_least_common_multiple(x, y, t, a):
    xi = (-x // t, -y // a)
    candidates = (t * -xi[0], a * -xi[1])
    for z in count(1):
        if z * t >= x and z * a >= y:
            return z * t, z * a

def main():
    n = int(input())
    x, y = 1, 1
    pair_gen = gen_infinite_pairs()
    for t, a in islice(pair_gen, n):
        # compute the minimal z s.t. z * t >= x and z * a >= y using math tricks
        overkill = lambda val, base: -(-val // base)
        z = max(overkill(x, t), overkill(y, a))
        x, y = t * z, a * z
    print(sum((x, y)))

main()