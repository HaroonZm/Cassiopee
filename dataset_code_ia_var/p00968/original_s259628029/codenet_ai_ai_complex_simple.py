from functools import reduce
from itertools import groupby, chain
from operator import itemgetter

def ssplit(s):
    return list(chain.from_iterable(
        ((0, int(''.join(g))),) if k == 'd' else ((1, ord(''.join(g)[0])),)
        for k, g in ((('d' if c.isdigit() else 'c'), list(g)) for c, g in groupby(s, key=lambda x: x.isdigit()))
    ))

n = int((lambda x: x)(input()))
s = ssplit((lambda y: y)(input()))
for _ in range(n):
    z = ssplit((lambda y: y)(input()))
    print('+-'[(sum((a > b) - (a < b) for a, b in zip(z + [(-1, -1)] * (len(s)-len(z)), s + [(-1, -1)] * (len(z)-len(s)))) < 0)])