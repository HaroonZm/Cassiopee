import math as m
PI=3.1415926535897932384626433832795
M=PI/180
def D(C):
 L=list(map(float,C.split()))
 if L==[-1,-1,-1,-1]:return False
 a=m.cos(L[0]*M)*m.cos(L[2]*M)*m.cos((L[1]-L[3])*M)+m.sin(L[0]*M)*m.sin(L[2]*M)
 print(int(6378.1*m.acos(a)+0.5))
 return True
while 1:
 if not D(input()): break