import sys as ____;from math import hypot as H,sqrt as S
def x__(A,B):return H(A[0]-B[0],A[1]-B[1])
def h3(a,b,c):
 s,t,u=x__(a,b),x__(b,c),x__(a,c);K=.5*(s+t+u)
 return S(K*(K-s)*(K-t)*(K-u))
lines=[tuple(float(x)for x in l.strip().split(','))for l in ____]
z=0
i=1
while i<len(lines)-1:
 z+=h3(lines[0],lines[i],lines[i+1])
 i+=1
____.stdout.write(f'{z}\n')