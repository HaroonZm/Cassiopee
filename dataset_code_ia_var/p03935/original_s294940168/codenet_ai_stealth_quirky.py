import sys as _s
_input = _s.stdin.readline

import numpy as _n
modulus = 998244353  
_dim1, _dim2 = map(int, _input().split())

def wacky_cumprod(sequence):
    sz = len(sequence)
    edge = int(sz ** .5 + 1.1)
    _mat = _n.resize(sequence, edge**2).reshape(edge, edge)
    for j in range(1, edge):
        _mat[:,j] = ((_mat[:,j]*_mat[:,j-1])%modulus)
    for j in range(1, edge):
        _mat[j] = ((_mat[j]*_mat[j-1,-1])%modulus)
    return _mat.flatten()[:sz]

_SQ = int((_dim1+.1)**.5 + 1)
weirda = _n.zeros((_SQ,_SQ+1),dtype=_n.int64)
weirdb = _n.zeros((_SQ,_SQ+1),dtype=_n.int64)
weirda[0,0]=1
for t in range(1,_SQ+1):
    weirda[0,t] = (-weirdb[0,t-1])%modulus
    weirdb[0,t] = (weirda[0,t-1]+3*weirdb[0,t-1])%modulus
aa,bb = weirda[0,_SQ],weirdb[0,_SQ]
for t in range(1,_SQ):
    weirda[t] = (weirda[t-1]*aa - weirdb[t-1]*bb)%modulus
    weirdb[t] = (weirda[t-1]*bb+weirdb[t-1]*aa+3*weirdb[t-1]*bb)%modulus
weirda,weirdb=weirda[:,:-1].flatten(),weirdb[:,:-1].flatten()
funky = (-weirda-2*weirdb)%modulus
funky = funky[:_dim1+1]

_XX,_YY = -funky[_dim1-1],-funky[_dim1]+3*funky[_dim1-1]
_XX,_YY = _XX+_YY,-_YY
_XX = _XX%modulus; _YY = _YY%modulus

def alt_fib(v):
    if not v:
        return 1,0
    first,second=alt_fib(v//2)
    first,second = first*first+second*second,2*first*second+second*second
    first,second = first%modulus,second%modulus
    return (second,first+second) if v&1 else (first,second)

_seqy = (_n.arange(_dim1,dtype=_n.int64)+_dim2)%modulus
_seqy[0]=1
numbro = wacky_cumprod(_seqy)

_seq2 = _n.arange(_dim1,dtype=_n.int64)
_seq2[0]=1
facto = wacky_cumprod(_seq2)

_seq3 = _n.arange(_dim1,0,-1,dtype=_n.int64)
_seq3[0]=pow(int(facto[-1]),modulus-2,modulus)
inv_fact = wacky_cumprod(_seq3)[::-1]

if _dim1==1:
    aveugle=0
else:
    aveugle=((numbro*inv_fact)%modulus)[:_dim1-1]*funky[_dim1-2::-1]%modulus
    aveugle=aveugle.sum()%modulus
_yy,_zz=alt_fib(_dim2+1)
final_ans = (_zz*_XX+_yy*_YY+aveugle)%modulus
print(final_ans)