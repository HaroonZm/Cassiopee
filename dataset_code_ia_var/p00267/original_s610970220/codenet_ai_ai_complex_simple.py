import functools
import operator
import itertools as it
import math
import sys

INFINITY = float('inf')
MODULUS = pow(10, 9) + 7

sentinel = lambda x: (x is None)
parse = lambda s: list(map(int, s.strip().split()))
double = lambda seq: map(lambda z: z * 2, seq)
oddify = lambda seq: map(lambda z: z * 2 + 1, seq)

# Read input using itertools with unusual constructs
def inp(): 
    for line in sys.stdin:
        yield line.rstrip('\n')
lines = inp()

while True:
    try:
        N = next(lines)
        if not N.isdigit() or int(N) == 0:
            break
        N = int(N)
        
        a_seq, b_seq = (parse(next(lines)) for _ in range(2))
        
        # Chain, map, then sum via functools.reduce and operator.add
        ls = list(
            it.chain(
                double(a_seq),
                oddify(b_seq)
            )
        )
        # Decorate-sort-undecorate pattern with enumerate/functools cmp_to_key
        keyf = lambda x: -x
        ls = list(sorted(ls, key=keyf))
        
        # Use itertools.accumulate with custom function
        cnts = {'evn':0, 'odd':0}
        ans = "NA"
        def step(acc, x):
            evn, odd = acc
            if x & 1:
                return (evn, odd+1)
            else:
                evn += 1
                if (evn - odd)*2 > evn and evn != N:
                    raise StopIteration(evn)
                return (evn, odd)
        try:
            functools.reduce(step, ls, (0,0))
        except StopIteration as stop:
            ans = stop.args[0]
        print(ans)
    except StopIteration:
        break