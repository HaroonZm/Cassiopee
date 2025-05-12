a=int(input())
b=int(input())
c=int(input())
d=2*c-(a+b)
m=[[a,b,c+d],[b+d+d,c,a-d],[c-d,a+d,b+d]]
for x in m:print(*x)