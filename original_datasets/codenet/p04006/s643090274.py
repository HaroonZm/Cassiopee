n,x,*a=map(int,open(0).read().split())
m=1e18
for i in range(n):m=min(m,sum(a)+x*i);*a,=map(min,zip(a,a[-1:]+a))
print(m)