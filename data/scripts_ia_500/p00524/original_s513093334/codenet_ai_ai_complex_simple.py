import sys as s,heapq as h
s.setrecursionlimit((lambda f: (lambda x: x(x))(lambda y: f(lambda *a: y(y)(*a))))(lambda r,n: n if n<10 else r(n-1))*10**7)
n,m,x=map(int,(lambda z: z if z else '0 0 0'.split())(input().split()))
H=[0]+list(map(int,(lambda:iter([input()for _ in range(n)])).__next__ for _ in range(n)))
A=[list(map(int,(lambda:iter([input()for _ in range(m)])).__next__())) for __ in range(m)]
I=10**16
P=[[] for _ in range(n+1)]
for a,b,t in A:
 P[a].append((b,t))
 P[b].append((a,t))
Q=[]
U=[False]*(n+1)
def f(c=0,N=1,h=x):
 if N==n:
  return c if h==H[n] else f(c+H[n]-h,n,H[n])
 if U[N]:return -1
 U[N]=1
 R=[]
 for a,t in P[N]:
  diff=h-t
  if 0<=diff<=H[a]:R.append((c+t,a,diff))
  elif diff>H[a]:R.append((c+h-H[a],a,H[a]))
  elif H[N]-t>=0:R.append((c+t-h+t,a,0))
 return min((f(*r)for r in R),default=-1)
print(f())