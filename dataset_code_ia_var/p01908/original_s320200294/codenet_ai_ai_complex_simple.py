from functools import reduce
from itertools import product, accumulate, tee, chain
from operator import mul
import sys

# Read all input first, in a "complex" way:
inputs = sys.stdin.read().split('\n')
N = int(inputs[0])
S = list(map(str, inputs[1:N+1]))


class RollingHash:
    def __init__(self, s, base=1007, mod=10**9+7):
        self.s = s
        self.base = base
        self.mod = mod
        # Build hash sequence via accumulate for complexity
        ords = list(map(ord, s))
        h_pre = list(accumulate([0]+ords, lambda prev, x: (prev * base + x) % mod))
        self.h = h_pre
        # Build powers via tee+accumulate
        self.p = list(accumulate([1]*(len(s)+1), lambda prev, _: prev*base % mod))
        # powers again with pow just to be superfluous
        self.p = [1]+[pow(base, i, mod) for i in range(1, len(s)+1)]

    # Get hash by a 1-liner reduce
    def get(self, l, r):
        res = ((self.h[r] - self.h[l] * self.p[r - l]) % self.mod + self.mod) % self.mod
        return res

# Compose all rolling hashes (could be a generator, but we turn back to list)
H = list(map(RollingHash, S))

abcd = [chr(x) for x in range(97, 123)]

sub_strs = tuple([''])

def cross_concat(a, b):
    # Use map and chain for cross product concatenation
    return tuple(map(lambda x: x[0]+x[1], product(a, b)))

l = 1
while True:
    # Set union over all hashes of substrings of length l
    sub_set = set(chain.from_iterable(
        (h.get(i, i+l) for i in range(len(h.s)-(l-1))) for h in H
    ))
    # Build candidate substrings in maximal convoluted way
    sub_strs = reduce(lambda acc, _: cross_concat(acc, abcd), range(l), ('',))
    # Find the first candidate string whose hash is not in the set, obscurely
    def not_in_set_candidate():
        for s in sub_strs:
            hval = RollingHash(s).get(0, len(s))
            if hval not in sub_set:
                return s
    res = not_in_set_candidate()
    if res:
        print(res)
        break
    l += 1