from functools import reduce
from operator import or_
from itertools import chain, compress, starmap
n, *rest = map(int, input().split())
B = set(rest[1:])
Bmask = reduce(or_, (1 << s for s in B), 0)
def bits_on(x):
    return list(compress(range(n), map(int, bin(x)[:1:-1])))
for x in range(1 << n):
    if not B.difference(i for i, c in enumerate(bin(x)[:1:-1]) if c == '1'):
        sep = ': ' if x else ':'
        out = ' '.join(map(str, starmap(lambda i, b: i, filter(lambda t: t[1]=='1', enumerate(bin(x)[:1:-1]))))
        print(f"{x}{sep}{out}")