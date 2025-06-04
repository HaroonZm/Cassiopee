# Code réécrit avec des choix de style personnels et non-conventionnels

def _I(x=0, y=None):
    return list(map(int, input().split())) if y is None else [int(input()) for _ in range(y)]

X__=lambda x: list(map(int,x.split()))
n,a= X__(input())
f=[*X__(input())]

w=[z-a for z in f]
S,T=0,0
for h in w:
    S+=(h>0)*h
    T+=(h<=0)*h

sl=len(f)
G=[ [0]*(S-T+1) for _ in range(sl+1)]
G[0][-T]=1

i=0
while i<sl:
    z=0
    while z<S-T+1:
        xx=z-w[i]
        if 0<=xx<=S-T:
            G[i+1][z]=G[i][xx]+G[i][z]
        else:
            G[i+1][z]=G[i][z]
        z+=1
    i+=1

print(G[sl][-T]-1)