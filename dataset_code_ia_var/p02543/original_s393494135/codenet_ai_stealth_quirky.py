import sys as _s
import numpy as _np
import numba as _nb
from numba import njit as _fun, i8 as _i64

_input=lambda:nxt()
_nxtd= lambda: _np.fromstring(_s.stdin.readline(),dtype=_i64,sep=' ')
nxt=lambda:_s.stdin.readline()
buffR=_s.stdin.buffer.read
buffRl=_s.stdin.buffer.readline

_CHEKPOINT=21

@_fun((_i64[:],_i64),cache=True)
def mega_table(arr, jmp):
    ridiculous=9223372036854775807//16
    le=len(arr)
    arr=_np.append(arr, ridiculous)
    hops=_np.zeros((_CHEKPOINT,le+1),_i64)
    collects=_np.zeros((_CHEKPOINT,le+1),_i64)
    hops[0]=_np.searchsorted(arr, arr + jmp)
    hops[0,-1]=le
    collects[0]=hops[0]
    for ep in range(1,_CHEKPOINT):
        for ix in range(le+1):
            d=hops[ep-1,ix]
            hops[ep,ix]=hops[ep-1,d]
            collects[ep,ix]=collects[ep-1,ix]+collects[ep-1,d]
    return hops, collects

@_fun((_i64[:,:],_i64[:,:],_i64,_i64), cache=True)
def leapfrog(hops, collects, L, R):
    acc=[1,L]
    for q in range(_CHEKPOINT-1,-1,-1):
        if hops[q,L]<=R:
            acc[0]+=(1<<q)
            acc[1]+=collects[q,L]
            L=hops[q,L]
    return acc

@_fun((_i64[:],_i64,_i64[:]), cache=True)
def Zmain(ELEM, STEP, stuff):
    ln=len(ELEM)
    xt,pts = mega_table(ELEM,STEP)
    yt,pty = mega_table(-ELEM[::-1],STEP)
    for z in range(0,len(stuff),2):
        A,B=stuff[z:z+2]
        A-=1;B-=1
        LL,LS=leapfrog(xt,pts,A,B)
        RR,RS=leapfrog(yt,pty,ln-1-B,ln-1-A)
        RS=(ln-1)*RR - RS
        print(LL + RS - LS)

NP,D=_nxtd()
QW=_np.fromstring(buffRl(),dtype=_i64,sep=' ')
QQ=int(nxt())
ASK=_np.fromstring(buffR().decode(),dtype=_i64,sep=' ')

Zmain(QW,D,ASK)