import sys

P=[1]*55000;P[:2]=0,0
i=1
while(i:=i+1)<55000:
    if P[i]:
        for J in range(i<<1,55000,i):P[J]=0

rd=sys.stdin.read
for S in rd().split('\n'):
    if not S.strip():continue
    N=int(S)
    a,b=None,None
    z=N-1
    while z and not P[z]:z-=1
    a=z
    z=N+1
    while z<55000 and not P[z]:z+=1
    b=z
    print("%d %d"%(a,b))