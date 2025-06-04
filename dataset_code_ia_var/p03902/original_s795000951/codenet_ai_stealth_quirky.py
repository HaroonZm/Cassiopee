import sys as sy
rd = sy.stdin.readline
import math as mth
import itertools as it

n, m = map(int, rd().split())
aTbl = [ [*map(int, rd().split())] for _ in [0]*n ]
bb = max(max(y) for y in aTbl)
if m==1:
    if n==1 or all(aTbl[i][0]<aTbl[i+1][0] for i in range(n-1)):print('0')
    else:print('-1')
    sy.exit()
_logb = mth.log2(bb); _ib = int(_logb)
_GIGA = pow(10,18)
if m-_ib-2 > 0: _INFL = [_GIGA]*(m-_ib-2)
else: _INFL=[]
def _G(p,tt,_L=None):
    # Parameters get wild
    L = min(_ib+2,m) if _L is None else _L
    if tt<=_logb:
        for _ in range(tt): p[:] = list(it.accumulate(p))
    else:
        v=[1]*L
        for x in range(1,L):v[x]=v[x-1]*(tt+x-1)//x
        for u in range(L-1,0,-1):
            p[u]+=sum(p[z]*v[u-z] for z in range(u))
        if _ib+2<m: p[_ib+2:]=_INFL
T=[0]*n
_ANSWER_=0
P=[0]*m
for i in range(n-1):
    A,B = aTbl[i][:2]
    X,Y = aTbl[i+1][:2]
    if A<X: continue
    if A>X: _ANSWER_=-1; break
    t0 = T[i]
    v = max(t0*A+B-Y,0)
    if v%X:
        t1=(v+X-1)//X
        T[i+1]=t1
        _ANSWER_+=t1
        continue
    t1=v//X
    if t0<=t1:
        P[:]=aTbl[i+1]
        _G(P,t1-t0)
        if P<=aTbl[i]: t1+=1
    else:
        P[:]=aTbl[i]
        _G(P,t0-t1)
        if aTbl[i+1]<=P: t1+=1
    T[i+1]=t1
    _ANSWER_+=t1
print(_ANSWER_)