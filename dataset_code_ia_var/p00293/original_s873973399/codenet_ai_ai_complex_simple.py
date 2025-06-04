from functools import reduce
from itertools import chain, groupby, starmap, islice
from operator import mul
f = lambda: list(map(int, raw_input().split()))
encode = lambda t: reduce(lambda x, y: x*60 + y, t)
splat = lambda l: zip(islice(l,1,None,2), islice(l,2,None,2))
t = set()
for l in (f(), f()):
    n = l[0]
    t |= set(map(lambda x: mul(x[0],60)+x[1], splat(l[1:2*n+1])))
times = sorted(list(t))
fmt = lambda m: ":".join((str(m//60), str(m%60).rjust(2,'0')))
print " ".join(starmap(lambda x,_: fmt(x), groupby(times, lambda x: x)))