import sys
X,Y,Z,A,B,C,N=map(int,sys.stdin.read().split())
from collections import Counter

def count_distances(L,pos):
    left=pos
    right=L-1-pos
    res=Counter()
    for d in range(left+right+1):
        low=max(0,d-right)
        high=min(d,left)
        res[d]=high-low+1 if high>=low else 0
    return res

cx=count_distances(X,A)
cy=count_distances(Y,B)
cz=count_distances(Z,C)

# Convolve cx and cy
cxy=Counter()
for dx,vx in cx.items():
    for dy,vy in cy.items():
        cxy[dx+dy]+=vx*vy

res=[0]*N
for d,v in cxy.items():
    for dz,vz in cz.items():
        dist=d+dz
        res[dist%N]+=v*vz
print(*res)