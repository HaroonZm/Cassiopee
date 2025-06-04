from functools import reduce
from itertools import starmap,groupby,chain
_=[tuple(sorted(map(int,input().split()))) for _ in range(6)]
r=sorted(_)
g = list(groupby(r))
s = all(len(list(b))==2 for a,b in g)
t = [list(x) for x in set(r)]
flat = lambda l: list(chain.from_iterable(l))
o = lambda: print(['no','yes'][s and len(t)==3 and all(a in flat(t) for a in flat(r)) and len(set(flat(t)))==3 and sorted(t,key=lambda x:(x[0],x[1]))[0][0]==sorted(t,key=lambda x:(x[0],x[1]))[1][0] and sorted(t,key=lambda x:(x[1],x[0]))[0][1]==sorted(t,key=lambda x:(x[1],x[0]))[2][1]])
o()