n,m=map(int,input().split())
a={}
for i in range(m):
    b,c=map(int,input().split())
    a[i]=(b,c-1)
a=sorted(a.items(),key=lambda x:x[1])
b=[0]*(n+1);c=[0]*(n+1)
for i in range(n):b[i]=c[i]=i
for i in range(m):
    x=a[i][1][1]
    b[x]=max(b[x],b[x+1])
    c[x+1]=min(c[x],c[x+1])
print(*[b[i]-c[i]+1 for i in range(n)])