x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
d=2*((x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1 - y2)))
cx = ((x1*x1 + y1*y1)*(y2 - y3) + (x2*x2 + y2*y2)*(y3 - y1) + (x3*x3 + y3*y3)*(y1 - y2))/d
cy = ((x1*x1 + y1*y1)*(x3 - x2) + (x2*x2 + y2*y2)*(x1 - x3) + (x3*x3 + y3*y3)*(x2 - x1))/d
r = ((cx - x1)**2 + (cy - y1)**2)**0.5
print(f"{cx:.18f} {cy:.18f} {r:.18f}")