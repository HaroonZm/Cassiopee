from functools import reduce
from operator import mul

from itertools import count, islice, starmap, repeat, chain

for idx in range(eval('int(input())')):
    n = eval('int(input())')
    print("Case %s:" % (idx+1))
    def zeta(k):
        for _ in range(10):
            digits = str(reduce(mul, (int(x) for x in str(k)), 1) + k**2)
            padding = ''.join(chain(repeat('0', 8-len(digits)), '')) if len(digits) < 8 else ''
            newdigits = (padding + digits)[2:6]
            yield int(newdigits)
            k = int(newdigits)
    list(starmap(print, zip(zeta(n))))