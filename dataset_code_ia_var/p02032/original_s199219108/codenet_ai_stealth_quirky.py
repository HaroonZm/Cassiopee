from math import sqrt as _s;N=int(input())
_P=[];i=2;_M=int(_s(N)+1)
while i<_M:
    z=0
    while N%i<1:
        z+=1;N//=i
    if z:_P+=[z]
    i+=1
if N-1:_P.append(1)
__x=1;_=lambda t:t+1
for q in _P:__x*=_ (q)
print(len(_P),__x-1)