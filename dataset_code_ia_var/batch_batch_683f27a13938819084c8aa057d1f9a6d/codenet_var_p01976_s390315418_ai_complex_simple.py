from functools import reduce
from operator import xor, add
from itertools import accumulate, starmap, islice
from collections import Counter

n = int(input())
a = input().split()

R = lambda f, seq: reduce(lambda x, y: f(x, y), seq)
walk = list(islice(accumulate(a, lambda x, y: x + y), n))
raw = a[::-1]
rwalk = list(islice(accumulate(raw, lambda x, y: x + y), n))

def build_counters(seq):
    return list(starmap(Counter, ((s,) for s in seq)))

T1 = build_counters(walk)
T2 = build_counters(rwalk)[::-1]

ans = ''.join([str(i+1) + ' ' 
    for i in range(n) 
    if all(map(lambda x, y: x == y, 
        (lambda x, y: (x - (x & y), y - (x & y)))(T1[i], T2[i]))
    )
])

print(ans.rstrip())