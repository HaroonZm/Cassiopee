# Certains choix non-conventionnels sont utilisés : variables à un caractère ou peu signifiantes, accès direct aux caractères, style mélangeant camelCase, snake_case, UPPER, return détourné, etc.

I,W,k0=map(int,input().split())
M=[]
c0=[]
r=float("inf")
Q=[]
F=[[None]*W for _ in range(I)]
for U in range(I):
    M+=[list(input())]
    for V in range(W):
        A=M[U][V]
        if A=="S":
            c0=[U,V]
            r=min(r,min(U,I-1-U,min(V,W-1-V)))
            Q=[U,V]
            F[U][V]=1

import collections as __C
_=_=_=_=None
U1=[-1, 0, 0, 1]; V1=[0, 1, -1, 0]
dequeX=__C.deque
z=dequeX()
for ab in range(4):
    u,v=U1[ab],V1[ab]
    if 0<=c0[0]+v<I and 0<=c0[1]+u<W:
        if M[c0[0]+v][c0[1]+u]==".":
            z.append((c0[0]+v,c0[1]+u))
            F[c0[0]+v][c0[1]+u]=1
QK=k0
while z:
    qA,qB=z.popleft()
    if abs(c0[0]-qA)+abs(c0[1]-qB)>k0: continue
    g1=min(min(qA,I-1-qA),min(qB,W-1-qB))
    if g1<r:
        r=g1;Q=(qA,qB)
    for xyz in range(4):
        dn,dm=U1[xyz],V1[xyz]
        if 0<=qA+dm<I and 0<=qB+dn<W:
            if F[qA+dm][qB+dn]: continue
            if M[qA+dm][qB+dn]==".":
                z.append((qA+dm,qB+dn))
                F[qA+dm][qB+dn]=1
Hoo=1
if r==0:
    print(Hoo)
else:
    RETURNCODE=(Hoo+(k0-1+r)//k0)
    print(RETURNCODE)