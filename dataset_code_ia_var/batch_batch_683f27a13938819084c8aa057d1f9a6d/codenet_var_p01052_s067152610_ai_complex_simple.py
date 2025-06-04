from functools import reduce
from operator import add, mul

n = int(input())
tbl = sorted(map(lambda ab: (int(ab.split()[1]), int(ab.split()[0])), [input() for _ in range(n)]))
seen = set()
sch = [(d, i) for i, (d, b) in enumerate(tbl) for day in range(max(1, b), min(32, d+1)) for _ in (0,)]
cover = [next(
    (100 * (not i in seen) * (seen.add(i) is None or True) for d, i in sch if day >= tbl[i][1] and tbl[i][0] >= day and i not in seen),
    0
) for day in range(1, 32)]
rslt = reduce(add, cover, 0) + (31-len(seen))*50
print(rslt)