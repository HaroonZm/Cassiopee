import sys

def f():return sys.stdin
L = list(f())
z=lambda x,y:x if x<y else x%y

def s(a,b,n):
 H=0
 for _ in range(n):
  d=a//b
  H+=d
  a=(a%b)*10
 return H

for _ in range(len(L)):
 A,B,N=map(int,L[_].split())
 print(s(z(A*10,B),B,N))