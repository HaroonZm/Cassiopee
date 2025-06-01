import sys as s
from math import sqrt as S, hypot as H

def H_(A,B):
 def D(x,y):return y - x
 return H(D(A[0],B[0]),D(A[1],B[1]))

def heron(*points):
 a,b,c=points
 e = [H_(a,b),H_(b,c),H_(a,c)]
 p = sum(e)/2
 return (p* (p - e[0]) * (p - e[1]) * (p - e[2])) ** 0.5

A=list(map(lambda x:tuple(map(float,x.split(','))), s.stdin))
R=0
i=1
while i < len(A)-1:
 R+=heron(A[0],A[i],A[i+1])
 i+=1
print(R)