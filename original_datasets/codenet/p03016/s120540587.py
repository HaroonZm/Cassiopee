L,A,B,M=map(int,input().split())

def partsum(a,b,l,n):
    doublingconst=[0 for i in range(0,60)]
    doublingconst[0]=1
    doublingline=[0 for i in range(0,60)]
    doublingline[0]=0
    for i in range(1,60):
        doublingconst[i]=((pow(10,l*2**(i-1),M)+1)*doublingconst[i-1]%M)
        doublingline[i]=((pow(10,l*2**(i-1),M)+1)*doublingline[i-1]+pow(2,i-1,M)*pow(10,l*2**(i-1),M)*doublingconst[i-1])%M

    ansconst=0
    chousei=0
    for i in range(0,60):
        if n>>i &1==1:
            ansconst+=doublingconst[i]*pow(10,chousei*l,M)
            ansconst%=M
            chousei+=2**i

    ansline=0
    chousei=0
    for i in range(0,60):
        if n>>i &1==1:
            ansline+=(doublingline[i]+chousei*doublingconst[i])*pow(10,chousei*l,M)
            ansline%=M
            chousei+=2**i

    return ansline*a+ansconst*b

start=len(str(A))
end=len(str(B*L+A-B))
part=[]
for i in range(start-1,end):
    l=1+(10**i-A-1)//B
    r=(10**(i+1)-A-1)//B
    l=max(0,l)
    r=min(L-1,r)
    part.append([i+1,l,r])

part.sort(reverse=True)
ans=0
chousei=0
for i in range(0,len(part)):
    length,l,r=part[i]
    const=B*r+A
    line=B
    ans+=(partsum(-line,const,length,r-l+1)*pow(10,chousei,M))%M
    ans%=M
    chousei+=length*(r-l+1)
print(ans)