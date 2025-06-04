n,m=[int(x)for x in input().split()]
u=[0 for _ in range(n)]
a=input().split()
a=[int(z)for z in a]
b=a[0]-1
i=1
while i<len(a):
    x=a[i]-1
    M,N=max(b,x),min(b,x)
    u[M]-=1
    u[N]+=1
    b=x
    i+=1
ans=0
for j in range(1,n):
    u[j]=u[j]+u[j-1]
    vals=input().split()
    d,bx,c=(int(vals[0]),int(vals[1]),int(vals[2]))
    s1=d*u[j-1]
    s2=bx*u[j-1]+c
    if s1<s2:
        ans=ans+s1
    else:
        ans=ans+s2
print(ans)