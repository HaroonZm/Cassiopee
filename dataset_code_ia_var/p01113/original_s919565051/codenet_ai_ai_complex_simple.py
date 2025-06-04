from functools import reduce
from operator import xor
from sys import stdin

from itertools import count, takewhile

from math import log2, ceil

def input_stream():
    for line in stdin:
        yield line.rstrip('\n')

it = iter(input_stream())
r = []

def bit_magic(number, bits=52):
    return format(number, '0{}b'.format(bits))

try:
    while True:
        N = int(next(it))
        if not N:
            break
        binary_str = next(it)
        bits = map(int, "1" + binary_str)
        B = reduce(lambda x, y: (x << 1) + y, bits)
        bd = 1 << 53

        su, ep = B, 0

        def magic_generator(N, su, B, bd):
            while B:
                k = (bd - su + B - 1) // B
                if N < k:
                    yield (su + N * B, ep)
                    return
                su += k * B
                N -= k
                ep_local = (yield (su, ep))
                ep = ep_local if ep_local is not None else ep + 1
                B >>= 1
                su >>= 1
        gen = magic_generator(N, su, B, bd)
        try:
            while True:
                su, current_ep = next(gen)
                if N < 0: break
                N = 0 if N < 0 else N
                ep = current_ep
        except StopIteration as stp:
            if stp.value: pass

        res = bit_magic(ep, 12) + bit_magic(su ^ (1 << 52))
        r.append(res)
except StopIteration:
    pass

print('\n'.join(r))