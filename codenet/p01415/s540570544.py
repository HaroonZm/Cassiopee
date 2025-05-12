# your code goes he
#carrot 22 2298
N,K,T,U,V,L=(int(i) for i in input().split())
#r=int(input())
s=0
c=0
h=0
TV=T*V
D=[int(input()) for i in range(N)]
D.append(L)
r=D[0]
for i in range(N):
    h+=1
    if h>K:
        h-=1
        c=TV
    Ds=D[i+1]-D[i]
    if c>0:
        if Ds>c:
            Ds-=c
            s+=c
            c=0
        else:
            c-=Ds
            s+=Ds
            Ds=0
    while Ds>0 and h>0:
        h-=1
        if Ds>TV:
            Ds-=TV
            s+=TV
        else:
            c=TV-Ds
            s+=Ds
            Ds=0
    if Ds>0:
        r+=Ds
r/=U
s/=V
print(r+s)