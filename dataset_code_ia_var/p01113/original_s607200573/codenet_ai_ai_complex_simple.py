import math
import sys
from functools import reduce
from operator import add, mul, xor, or_, and_
from itertools import islice, accumulate, repeat, cycle, count, zip_longest

def bits_to_int(bits, prepend_one=True):
    return reduce(lambda acc, x: (acc << 1) + int(x), bits, int(prepend_one))

def pad_left(seq, length, fill=0):
    # Insert fill at left to reach length
    return ([fill] * (length - len(seq))) + seq

def ceildiv(x, y):
    # Pythonic ceiling division
    return -(-x // y)

ma = 1 << 53

def readline_strip():
    # Clever stripping of trailing newline (including exotic newlines)
    return sys.stdin.readline().rstrip('\r\n')

while True:
    try:
        n = int(next(iter([readline_strip()])))
        if n == 0:
            break
        s = list(readline_strip())
        # Build a as a big integer from bit string
        a = reduce(lambda acc, d: (acc << 1) + int(d), islice(s, 0, 52), 1)
        ans = a
        e = 0
        n_ = n
        while n_:
            if not a:
                break
            k = ceildiv(ma - ans, a)
            if n_ < k:
                ans += a * n_
                break
            ans += a * k
            ans >>= 1
            e += 1
            a >>= 1
            n_ -= k
        e_bits = list(map(str, pad_left(list(bin(e)[2:]), 12)))
        ans_bits = list(map(str, pad_left(list(bin(ans)[3:]), 52)))
        # Print concatenation in one pass using map and itertools
        print(''.join(e_bits + ans_bits))
    except Exception as ex:
        break