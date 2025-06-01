def F(a): return [P[a][i]-P[0][i] for i in [0,1,2]]

def D(X):
  a,b,c,d,e,f,g,h,i=X
  return a*e*i+d*h*c+g*b*f-a*h*f-d*b*i-c*e*g

def G(a):
  X=A[:]; X[a::3]=V;
  return 1.0*D(X)/D0

P=[map(int,raw_input().split()) for _ in [0]*5]
A=[0]*9
V=F(1)
for i in [0,1,2]: A[i::3]=F(i+2)

f=0
D0=D(A)
if D0!=0:
  r1,r2,r3=G(0),G(1),G(2)
  if r1>=0 and r2>=0 and r3>=0 and r1+r2+r3>=1: f=1
print ["HIT","MISS"][f]