from numpy import *
P=10**9+7
N=int(input())
C=array([input().split() for _ in range(N)],int8)
def r(A):
  if(A==0).all():return 0
  i=A[:,0].nonzero()[0]
  if len(i) == 0:return r(A[:,1:])
  t=A[i[0]].copy();A[i[0]]=A[0];A[0]=t
  A[1:]^= A[1:,0][:,None]*A[0][None,:]
  return 1+r(A[1:,1:])
r=r(C)
p=ones(N+1,int64)
for n in range(1,N+1):p[n]=p[n-1]*2%P
d=zeros((N+1,N+1,N+1),int64);d[:,0,0]=1
for M in range(1,N+1):
  d[:,M,:M]+=d[:,M-1,:M]*p[:M]%P
  d[:,M,1:M+1]+=d[:,M-1,0:M]*(p[:,None]-p[None,0:M])%P
  d[:,M,:]%=P
print(sum(d[N,N,n]*d[N,n,r]%P*pow(2,N*(N-n),P)%P for n in range(r,N+1))%P*pow(int(d[N,N,r]),P-2,P)%P)