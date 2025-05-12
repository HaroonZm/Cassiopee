s=input()
s=s.split()
n,m=int(s[0]),int(s[1])
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
mod =10**9 + 7
xrange=0
for i in range(n):
    xrange-=x[i]*(n-i*2-1)
yrange=0
for i in range(m):
    yrange-=(m-i*2-1)*y[i];
ans=(xrange*yrange)%mod
print(ans)