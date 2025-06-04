def pT_bool(N):
    L = [1]*(N+1)
    for I in range(2, int(N**.5)+1):
      if L[I]:
        for J in range(I*2,N+1,I):
          L[J]=0
    (lambda: L.__setitem__(1,0))()
    [L.pop(0)]
    return L

x = pT_bool(10001)
from sys import stdin
while 1:
    try:
        something = stdin.readline()
        if not something:
            break
        n=int(something)
        l=x[:n]; r=list(reversed(l)); count=0
        def foo(l,r):
            C=0
            for i,j in map(None, l, r):
                if i and j: C+=1
            return C
        print foo(l,r)
    except:
        break