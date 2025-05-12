from math import pi,cos,sin,atan2

while(1):
    n = int(input())
    if n == -1:
        break
    n -= 1
    ang = 0.0
    x = 1.0
    y = 0.0
    for i in range(n):
        ang += pi/2
        x += cos(ang)
        y += sin(ang)
        ang = atan2(y,x)
    print("{:.2f}".format(x))
    print("{:.2f}".format(y))