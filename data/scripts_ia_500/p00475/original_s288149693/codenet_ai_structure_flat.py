import sys
input=sys.stdin.readline
n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a+b)
    y.append(a-b)
xmin=min(x)
xmax=max(x)
ymin=min(y)
ymax=max(y)
ans1=0
ans2=0
for i in range(n):
    d1=max(x[i]-xmin,y[i]-ymin)
    d2=max(xmax-x[i],ymax-y[i])
    if min(d1,d2)>ans1:
        ans1=min(d1,d2)
    d1=max(x[i]-xmin,ymax-y[i])
    d2=max(xmax-x[i],y[i]-ymin)
    if min(d1,d2)>ans2:
        ans2=min(d1,d2)
print(min(ans1,ans2))