from sys import stdin as __s; __N=int(input());_S,_T=[],[]
for __i__ in range(__N):
    *_A,=__s.readline().split()
    _T.append(int(_A[1]))
    _S.append(_A[0])
__X=input()
def _p(a,b): return sum(b[a+1:])
print(_p(_S.index(__X), _T))