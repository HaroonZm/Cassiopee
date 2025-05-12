import math
N=300000
L=[False]*(N+1)
for i in range(1,N):
    t=i%7
    if t==6 or t==1:
        L[i]=True
for i in range(2,int(math.sqrt(N))):
    if L[i]==True:
        j=2
        while i*j<=N:
            L[i*j]=False
            j+=1
L=[i for i in range(len(L)) if L[i]==True]

while True:
    n=input()
    if n==1:break
    ans=[str(i) for i in L[1:] if n%i==0]
    print "%d: %s"%(n," ".join(ans))