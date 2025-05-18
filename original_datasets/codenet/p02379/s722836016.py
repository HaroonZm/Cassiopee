import math
x1, y1, x2, y2=map(float,input().split())
x=abs(x1-x2)
y=abs(y1-y2)
print('{:.5f}'.format(math.sqrt(x*x+y*y)))