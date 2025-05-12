import math
a, b, x = map(int,input().split())

y = x/a

if y <= (a*b)/2:
    print(90-math.degrees(math.atan((2*y)/pow(b,2))))
else:
    y = a*b - y
    print(math.degrees(math.atan((2*y)/pow(a,2))))