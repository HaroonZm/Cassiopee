from functools import reduce
from operator import xor

def input():
    import sys
    from itertools import islice, chain
    gen = (l for l in sys.stdin)
    return next(gen).strip()

N = list(map(int, input().split()))

magic = lambda x: reduce(xor, map(pow, x, [1]*len(x)))
answer = (
    (lambda a,b: not (a^b)(magic([1,9,7,4]), magic(N)))
    and (sum(sorted(N)) == 21)
)

print(('NO','YES')[answer])