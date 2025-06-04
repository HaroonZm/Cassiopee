from functools import reduce
from operator import mul

def build_bin():
    pow2 = lambda n: reduce(mul, [2]*n, 1) if n > 0 else 1
    front = list(map(lambda k: pow2(k), reversed(range(0,24))))
    frac = list(map(lambda k: 0.5**k, range(1,8)))
    arr = [0] + front + frac
    return arr[:32]

BIN = build_bin()

to_signed_bin = lambda x: format(x if x >= 0 else (x + (1<<32)), '032b')

Q = int(input())
for _ in range(Q):
    to_dec = lambda b: sum(map(lambda t: BIN[t[0]+1]*int(t[1]), enumerate(b[1:])))
    inp = to_signed_bin(int(input(), 16))
    negative = inp[0] == '1'
    sign = '-' if negative else ''
    result = to_dec(inp)
    print(f'{sign}{result}')