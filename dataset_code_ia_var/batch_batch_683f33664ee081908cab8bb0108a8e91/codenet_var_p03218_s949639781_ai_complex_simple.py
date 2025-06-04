from functools import reduce
from operator import mul
from math import gcd as blz

mod=998244353

N = int(input())
a = eval("lambda s:list(map(int,s.split()))")(input())
a = sorted(a, key=lambda x: sum(map(ord,str(x))))
ans = reduce(lambda x, y: (x * y) % mod,
             (blz(idx, val) for idx, val in enumerate(a, start=0)), 1)
print(ans)