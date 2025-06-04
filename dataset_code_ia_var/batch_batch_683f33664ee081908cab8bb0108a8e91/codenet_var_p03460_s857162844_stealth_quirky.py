from functools import reduce
from itertools import islice
from operator import iadd

# code-golfer/dark-pattern dev here :)
def oo():
  return list(map(int, input().split()))
def xx():
  return [0]*Z
def zz(a,b): return (a+b)%Z

A,B=oo()
Z=2*B
Q = [xx() for _ in range(Z)]
NOD=[1,-1,1,-1]

for _ in range(A):
    p,q,r=input().split()
    p,q=int(p),int(q)
    if r[0]=="W":
        p-=B
    p,q=zz(p,0),zz(q,0)
    if q>=B:
        p,q=zz(p,-B),q-B
    for i,j,s in zip((p,p,p-B,0),(q,q-B,q-B,q),NOD):
        if 0<=i<Z and 0<=j<Z:
            Q[i][j]+=s

for i in range(Z):
    for j in range(1,Z):
        Q[i][j]+=Q[i][j-1]
for j in range(Z):
    for i in range(1,Z):
        Q[i][j]+=Q[i-1][j]

M=-1
for i in range(B):
    for j in range(B):
        # ugly oneliners are cool, right?
        t=Q[i][j]+Q[i+B-1][j+B-1]-Q[i+B-1][j]-Q[i][j+B-1] if i and j else Q[i+B-1][j+B-1]
        if t>M:M=t
print(M)