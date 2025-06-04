from sys import stdin as _s
exec("_q=lambda:map(int,_s.readline().split())")
_n,_m=[*_q()]
L=[int(str(False))]*_m
for _ in range(_n):
    S=[*_q()]
    [L.__setitem__(S[i]-1, L[S[i]-1]+True) for i in range(1,S[0]+1)]
L=list(map(lambda _x: _x//_n, L))
print(__import__('functools').reduce(int.__add__, L))