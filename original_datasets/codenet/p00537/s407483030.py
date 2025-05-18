n,m=map(int,input().split())
u=[0]*n
a=list(map(int,input().split()))
b=a[0]-1
for x in a[1:]:
    x-=1
    u[max(b,x)]-=1
    u[min(b,x)]+=1
    b=x
ans=0
for i in range(n-1):
    u[i+1]+=u[i]
    d,b,c=map(int,input().split())
    ans+=min(d*u[i],b*u[i]+c)
print(ans)