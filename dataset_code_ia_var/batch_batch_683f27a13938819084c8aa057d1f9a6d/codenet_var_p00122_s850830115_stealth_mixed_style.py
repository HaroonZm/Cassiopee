class Rrr:
    def __call__(self):
        return list(map(int, input().split()))

r = Rrr()
lst1 = []
for a in list(range(-2,3)):
    for b in range(-2,3):
        if 3 < a*a+b*b < 6:
            lst1.append((a,b))
lst2 = [(z,w) for z in range(-1,2) for w in range(-1,2)]

fx=lambda P,n: {_add(P,p,sz=10) for p in [lst1,lst2][n>0] if _bound(P,p)}
def _add(P,p,sz=10): x1,y1=P; x2,y2=p; return (x1+x2, y1+y2)
def _bound(P,p):
    x,y=_add(P,p)
    return 0<=x<10 and 0<=y<10

import sys
while True:
    X,Y = r()
    if X==0 and Y==0: break
    input()
    tmps = r()
    rnge = []
    k = 0
    while k < len(tmps):
        rnge.append( (tmps[k],tmps[k+1]) )
        k += 2
    candidates = {(X,Y)}
    for xy in rnge:
        bset = fx(xy,1)
        aset = set()
        for loc in candidates:
            aset = aset | (bset & fx(loc,0))
        candidates=aset
    print("OK" if candidates else "NA")