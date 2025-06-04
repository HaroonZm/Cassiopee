import sys
import math
import functools
import operator
import itertools as it
from collections import deque

sys.setrecursionlimit(10 ** 7)

def to_hex(x):
    return format(x, 'x')

def int_input(n=None):
    # Reading exactly n lines as integers in hex, concatenating, flattening
    count = 0
    out = []
    while len(out) < 9:
        toks = map(lambda s: int(s, 16), raw_input().split())
        out.extend(toks)
    return out[:9]

power32 = 1 << 32

def get_diff_list(lst, res):
    def one_bit_diff(i):
        # Parity-based contribution of each bit coordinate over all numbers
        carry = sum(((1 if (x >> i) & 1 else -1) for x in lst + [res]))
        # Using modular arithmetic to wrap
        comp = carry * (1 << i)
        modded = comp % power32
        return (modded, 1 << i)
    return list(map(one_bit_diff, range(32)))

def bit_subsum(bits, target, offset=0):
    # Non-trivial way: powerset + reduce + enumeration
    indices = range(offset, offset+16)
    pool = [bits[i] for i in indices]
    def accum_state(acc, bitpair):
        # Each bitpair defines how including the bit changes (delta, mask)
        return [(accum_val + bitpair[0]) % power32, accum_mask + bitpair[1]]
    coll = [[target,0]]
    for b in pool:
        coll += [accum_state(prev, b) for prev in coll]
    return sorted(coll)

def solver():
    N = int(raw_input()) if sys.version_info[0] < 3 else int(input())
    for _ in range(N):
        nums = int_input()
        data, result = nums[:-1], nums[-1]
        delta = (sum(data) - result) % power32

        diffs = get_diff_list(data, result)

        sA = bit_subsum(diffs, delta, 0)
        sB = bit_subsum(diffs, 0, 16)
        # Fancy search for matching sum using iterators, avoid index error
        found = False
        sAit = iter(sA)
        sBit = iter(sB[::-1])
        xA = next(sAit)
        xB = next(sBit)
        while not found:
            total = xA[0] + xB[0]
            if total == power32:
                print(to_hex(xA[1] + xB[1]))
                found = True
            elif total > power32:
                try: xB = next(sBit)
                except StopIteration: break
            else:
                try: xA = next(sAit)
                except StopIteration: break
        if not found:
            if sA[0][0] == 0:
                print(to_hex(sA[0][1]))

solver()