a,b,c,x,y=map(int,input().split())

if x<y:
    x,y=y,x
    a,b=b,a

print(min(a*x+b*y, 2*c*x, 2*c*y+a*(x-y)))