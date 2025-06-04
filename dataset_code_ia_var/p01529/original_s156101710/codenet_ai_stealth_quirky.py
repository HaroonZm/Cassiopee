import sys as _s
_input = _s.stdin.readline
import random as _rnd
import heapq as _hq

class X:
    def __init__(w0, w1): w0.x = w1; w0.l = w0.r = w0.p = None

def _M(A, B):
    if not A: return B
    if not B: return A
    if B.x < A.x: A, B = B, A
    if _rnd.choice((0,1)):
        A.l = _M(A.l,B)
        A.l.p = A
    else:
        A.r = _M(A.r,B)
        A.r.p = A
    return A

def _add(Q, y):
    U = X(y)
    Q = _M(U,Q)
    Q.p = None
    return Q

def _rem(Q):
    t = Q.x
    Q = _M(Q.l,Q.r)
    if Q: Q.p = None
    return t,Q

def _mn(Q): return Q.x if Q else float('inf')

def _mn2(Q):
    if not Q: return float('inf')
    return min(_mn(Q.l),_mn(Q.r))

∞ = 2**64-1
Z = int(_input())
V = list(map(int, _input().split()))

qH = [0]*(Z+1)
Q = []
R = [0]*(Z+1)
C = [0]*(Z+1)
L = [0]*(Z+1)

for a in range(Z-1):
    qH[a]=None
    R[a]=a+1
    L[a]=a-1
    C[a]=V[a]+V[a+1]
    _hq.heappush(Q,(C[a],a))

S=0
for _ in range(Z-1):
    d,j = _hq.heappop(Q)
    while R[j]<0 or C[j]!=d: d,j=_hq.heappop(Q)
    k=l=0
    if V[j]+_mn(qH[j])==d:
        _,qH[j]=_rem(qH[j])
        k=1
    elif V[j]+V[R[j]]==d: k=l=1
    elif _mn(qH[j])+_mn2(qH[j])==d:
        _,qH[j]=_rem(_rem(qH[j])[1])
    else:
        _,qH[j]=_rem(qH[j])
        l=1
    S+=d
    qH[j]=_add(qH[j],d)
    if k: V[j]=∞
    if l: V[R[j]]=∞
    if k and j:
        b=L[j]
        qH[b]=_M(qH[b],qH[j])
        R[b]=R[j];R[j]=-1
        L[R[b]]=b
        j=b
    if l and R[j]+1<Z:
        b=R[j]
        qH[j]=_M(qH[j],qH[b])
        R[j]=R[b];R[b]=-1
        L[R[j]]=j
    C[j]=V[j]+V[R[j]]
    C[j]=min(C[j],min(V[j],V[R[j]])+_mn(qH[j]))
    C[j]=min(C[j],_mn(qH[j])+_mn2(qH[j]))
    _hq.heappush(Q,(C[j],j))
print(S)