import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
L=[i for i in range(N+2)]
P=1
C=[0 for i in range(N+2)]
C[P-1]=1
C[P+1]=1
C[P]=1
for i in range(Q):
    A,B=map(int,input().split())
    if A==P:
        P=B
    elif B==P:
        P=A
    L[A],L[B]=L[B],L[A]
    C[L[P-1]]=1
    C[L[P+1]]=1
ans=0
for i in range(1,N+1):
    if C[i]==1:
        ans+=1
print(ans)
#print(L)
#print(C)