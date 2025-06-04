from functools import reduce
from operator import add

N=int(input())
A=list(map(int,input().split()))

S=reduce(add,A)
k=N*(N+1)//2
R=divmod(S,k)
if R[1]:print("NO");exit()

r=R[0]
f=lambda i:divmod(A[i]-A[(i+1)%N]+r,N)
L=[f(i) for i in range(N)]
if any(x[0]<0 or x[1] for x in L):print("NO");exit()
print("YES"*(sum(x[0] for x in L)==r)or"NO")