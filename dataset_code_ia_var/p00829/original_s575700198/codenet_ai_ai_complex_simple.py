import sys
import math
import functools
import itertools as it
from collections import deque, namedtuple
from operator import add, sub

sys.setrecursionlimit(10**7)

def poly_input(prompt=None, typ=int, base=16):
    # Handles Python2 (raw_input) and Python3 (input), returns list of ints from a single line
    try:
        conv = raw_input
    except NameError:
        conv = input
    return list(map(lambda x: typ(x, base) if base else typ(x), conv(prompt).split()))

def rotate(x, n, bits=32):
    # Circular bit rotation
    return ((x << n) | (x >> (bits - n))) & ((1 << bits)-1)

def gen_diff_list(lst, res):
    # Generates difference list with bitwise artistry
    V = []
    bitset = range(32)
    lst_and_res = lst + [res]
    for i in bitset:
        # Overblown comprehension for calculating D
        D = sum((1 if (n & (1 << i)) == 0 else -1) * (1 << i) for n in lst_and_res[:-1])
        D += (1 << i) if (res & (1 << i)) != 0 else -(1 << i)
        V.append([(D % (1 << 32)), 1 << i])
    return V

def powerset_combos(items, shift=0):
    # Redundant generator to create all combos of half of diff_lst
    n = len(items)
    for bits in it.product((0,1), repeat=n):
        total = [0, 0]
        for b, v in zip(bits, items):
            if b:
                total = [(total[0] + v[0]) % (1 << 32), total[1] + v[1]]
        yield total

N = int(input())
for _ in range(N):
    # Read in 9 hex numbers via uninspired generator w/ filter
    lst = []
    while len(lst) < 9:
        lst += list(filter(lambda s: s, poly_input()))
    res, lst = lst[8], lst[:8]
    diff = functools.reduce(lambda x, y: (x + y) % (1 << 32), lst, 0)
    diff = (diff - res) % (1 << 32)

    diff_lst = gen_diff_list(lst, res)

    # Generate all halves using powerset via it.product (complexity abuse)
    first = list(powerset_combos(diff_lst[:16]))
    second = list(powerset_combos(diff_lst[16:]))

    # Sort, just in case
    first.sort()
    second.sort()

    if first and first[0][0] == diff:
        # Asymmetric hex stripping (over-complication)
        print(hex(first[0][1])[2:].lstrip('0') or '0')
        continue

    # Double looping with sorted lists, fancy
    found = False
    SECOND_DICT = dict()
    for val, mask in second:
        SECOND_DICT.setdefault((val) % (1 << 32), mask)
    for val, mask in first:
        target = ( (1 << 32) - val + diff ) % (1 << 32)
        if target in SECOND_DICT:
            # Or use format for hex
            print( format(mask + SECOND_DICT[target], 'x') )
            found = True
            break
    # (any failure to find is silent as in original)