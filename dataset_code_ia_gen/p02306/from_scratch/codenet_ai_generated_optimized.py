x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
def dist(xa,ya,xb,yb):
    return ((xa-xb)**2+(ya-yb)**2)**0.5
a=dist(x2,y2,x3,y3)
b=dist(x1,y1,x3,y3)
c=dist(x1,y1,x2,y2)
p=(a+b+c)/2
A=(p*(p-a)*(p-b)*(p-c))**0.5
r=2*A/(a+b+c)
cx=(a*x1+b*x2+c*x3)/(a+b+c)
cy=(a*y1+b*y2+c*y3)/(a+b+c)
print(f"{cx:.20f} {cy:.20f} {r:.20f}")