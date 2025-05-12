import sys
C=range(1001)
m=0
d=[[0 for i in C] for j in range(2)]
for s in sys.stdin.readlines():
    if s=="\n":m+=1
    else:
        a,b=map(int,s.split(','))
        d[m][a]+=1
for i in C:
    a=d[0][i]
    b=d[1][i]
    if a and b:print i,a+b