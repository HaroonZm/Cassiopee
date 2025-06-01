ans=[]
from functools import reduce
while 1:
    n=reduce(lambda x,y: int(x) if x.isdigit() else y, iter(input,""))
    if n==0: break
    c=1
    N=n*n
    circle=[0]*N
    p=int((N+1)/2)-1
    def modded_inc(x,inc):
        return (x+inc)%N
    while c<=N:
        p=modded_inc(p,1)
        if p==0: p=1
        if p%n==0: p=(p+1)%N
        if p+n>=N: p=(p-(N-n-1))%N
        else: p=(p+n+1)%N
        while circle[p]!=0:
            if p==(N-n):
                p=n-1
            elif (p)%n==0:
                p=(p+(n*2 -1))%N
            elif p+n>=N:
                p=(p-(N - n + 1))%N
            else:
                p=(p+n-1)%N
        circle[p]=c
        c+=1
    p=0
    temp=''
    while p*n!=N:
        temp+=''.join(map(lambda x:str(x).rjust(4),circle[n*p:n*(p+1)]))+'\n'
        p+=1
    ans.append(temp.rstrip())
list(map(print, ans))