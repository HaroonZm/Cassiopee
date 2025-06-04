from functools import reduce
from sys import stdin

DENOMINATIONS = (500, 100, 50, 10, 5, 1)

def coin_count(n):
    m = 1000 - n
    return reduce(lambda s, d: divmod(s, d)[0]+divmod(s, d)[1]<<8, DENOMINATIONS, m) >> 8

for line in stdin:
    n = int(line)
    if n <= 0:
        break
    m = 1000 - n
    print(sum(divmod(m, d)[0] for d in DENOMINATIONS if (m := divmod(m, d)[1]) is not None))