from bisect import bisect_left as bl
from collections import defaultdict as dd
from functools import reduce as rd
from operator import mul as ml

from itertools import chain as ch

exec("""
while True:
 r,c,q=map(int,raw_input().split())
 if not r:break
 X,Y=[[0,0]for _ in[0]*r],[[0,0]for _ in[0]*c]
 [[(X,b.__setitem__(B,[i,order])) if not A else (Y,b.__setitem__(B,[i,order])) for A,B,order in[map(int,raw_input().split())]][0] for i in range(1,q+1) for b in [X if not map(int,raw_input().split())[0] else Y]]
 S=lambda d:sorted([Y[j][0]for j in range(c)if Y[j][1]==d])
 T=[S(1),S(0)]
 ans=rd(ml,[r,sum(Y[j][1]for j in range(c))])
 ans-=(sum(((-1)**X[i][1])*bl(T[X[i][1]],X[i][0]) for i in range(r)))
 print ans
""")