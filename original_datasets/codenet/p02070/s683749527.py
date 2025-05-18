N=int(input())
P=[int(x)-1 for x in input().split()]
Q=[int(x)-1 for x in input().split()]
ap=[[-1 for i in range(N)]for j in range(N)]
b=[0]*N
for i in range(N+1):
    for j in range(N):
        if ap[j][P[j]]>=0:
            if b[j]==0:b[j]=i-ap[j][P[j]]
        else:
            ap[j][P[j]]=i
        P[j]=Q[P[j]]
a=[ap[i][i] for i in range(N)]
flag=True
if sum(A<0 for A in a)>0:
    flag=False
A=0
B=1
def extgcd(a,b):
    if b==0:
        return (a,1,0)
    q=a//b
    g,x,y=extgcd(b,a-q*b)
    z=x-q*y
    return (g,y,z)
def f(A,B,a,b):
    g,x,y=extgcd(B,b)
    if (a-A)%g!=0:
        return (0,0)
    x*=(a-A)//g
    A+=B*x
    B=B//g*b
    A%=B
    if A<0:A+=B
    return (A,B)
for i in range(N):
    if flag:
        A,B=f(A,B,a[i],b[i])
        if B==0:flag=False
print(A if flag else -1)