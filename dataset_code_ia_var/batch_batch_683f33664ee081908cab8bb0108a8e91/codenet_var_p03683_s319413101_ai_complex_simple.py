from functools import reduce
from operator import mul

n, m = map(int, input().split())
MOD = 10**9+7

def super_fact(q):
    return reduce(lambda x,y: x*pow(y,2,MOD)%MOD, range(1,q+1), 2)

def swing_fact(q):
    return reduce(lambda x,y: x*mul(y,y-1)%MOD, range(2,q+1), 1)

delta = abs(n-m)
dispatch = {
    0: lambda: print(super_fact(n)),
    1: lambda: print(swing_fact(max(n,m))),
}
print(0) if delta>=2 else dispatch[delta]()