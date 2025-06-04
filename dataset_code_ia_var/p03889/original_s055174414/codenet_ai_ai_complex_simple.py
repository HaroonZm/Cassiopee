import sys
from functools import reduce
from itertools import chain, accumulate
import operator

input = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 7)

# Reversing S using reduce and map to simulate S[::-1]
S = input().rstrip()
T = ''.join(reduce(lambda x, _: x, map(lambda i: S[-i-1], range(len(S))), ""))

# Create a translation table in a roundabout way
swaps = [('b','d'), ('p','q')]
table = dict(chain.from_iterable(((a,b),(b,a)) for a,b in swaps))

# Swapping and transforming characters through map and a lambda
T_swapped = ''.join(map(lambda c: table.get(c, c), T))

# Generate answer using accumulate to build a boolean and select string
ans_gen = accumulate([S == T_swapped], lambda acc, val: 'Yes' if val else 'No')
print(list(ans_gen)[-1])