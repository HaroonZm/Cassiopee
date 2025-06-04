x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
D=2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
cx=((x1**2+y1**2)*(y2-y3)+(x2**2+y2**2)*(y3-y1)+(x3**2+y3**2)*(y1-y2))/D
cy=((x1**2+y1**2)*(x3 - x2)+(x2**2 + y2**2)*(x1 - x3)+(x3**2 + y3**2)*(x2 - x1))/D
r=((cx - x1)**2 + (cy - y1)**2)**0.5
print(f"{cx:.18f} {cy:.18f} {r:.18f}")