from functools import reduce
from operator import add

def odd_even_pattern(h, w):
    seq = lambda s1, s2, n: ''.join(reduce(add, zip(s1 * n, s2 * n))[:w])
    pat = [
        seq('#', '.', (w+1)//2),
        seq('.', '#', (w+1)//2)
    ]
    return reduce(lambda a, b: a+'\n'+b, (pat[i%2] for i in xrange(h)))

import sys

inp = iter(sys.stdin.readline, '')
while True:
    try:
        H, W = map(int, next(inp).split())
    except StopIteration:
        break
    if H*W == 0:
        break
    print(odd_even_pattern(H, W))
    print