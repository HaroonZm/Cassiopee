n,m=map(int,input().split())
d=[-1]*n
def find(x):
    if d[x]<0:
        return x
    d[x]=find(d[x])
    return d[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if d[x]>d[y]:
        x,y=y,x
    d[x]+=d[y]
    d[y]=x
    return
ans=(int)(n*(n-1)/2)
a=[0]*m
b=[0]*m
stack=[]
for i in range(m):
    a[i],b[i]=map(int,input().split())
    a[i]-=1
    b[i]-=1
a.reverse()
b.reverse()
for i in range(m):
    stack.append(ans)
    a[i]=find(a[i])
    b[i]=find(b[i])
    if find(a[i])!=find(b[i]):
        ans-=(int)(-d[a[i]])*(-d[b[i]])
        unite(a[i],b[i])
while stack:
    print(stack.pop())