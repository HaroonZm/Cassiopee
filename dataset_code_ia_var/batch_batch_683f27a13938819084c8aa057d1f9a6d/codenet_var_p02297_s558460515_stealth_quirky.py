import sys as _S;I=_S.stdin.readline
Z=lambda:map(int,I().split())
n=int(I());z=range(n)
A=[[*Z()] for __ in z]
A.append(A[0])
Σ=0
for a in z:
 S=a+1
 Σ+=A[a][0]*A[S][1]-A[a][1]*A[S][0]
print(.5*Σ)