n,m,t=map(int,input().split())
d=0
a=[int(i) for i in input().split()]
b=a[0]-m
c=a[0]+m
for i in range(1,n):
    if a[i]>c+m:
        d+=c-b
        b=a[i]-m
    c=a[i]+m
if c<t:d+=c-b
else:d+=t-b
print(t-d)