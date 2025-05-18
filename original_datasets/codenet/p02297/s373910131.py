def area(a,b):
  return (a.real*b.imag-a.imag*b.real)/2

q=int(input())

A=[]
for _ in range(q):
  x,y=map(int,input().split())
  A.append(x+y*1j)

S=0.0
for i in range(1,q-1):
  S+=area(A[i]-A[0],A[i+1]-A[0])

print("{:.1f}".format(S))