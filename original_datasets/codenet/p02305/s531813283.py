import math

c1x,c1y,c1r = [int(i) for i in input().split()]
c2x,c2y,c2r = [int(i) for i in input().split()]

d = math.sqrt(pow(c1x-c2x, 2) +  pow(c1y-c2y, 2))

s = c1r + c2r

if d > s:
    print(4)
elif d == s:
    print(3)
else:
    if c1r > c2r:
        if d + c2r > c1r:
            print(2)
        elif d + c2r == c1r:
            print(1)
        else:
            print(0)
    else:
        if d + c1r > c2r:
            print(2)
        elif d + c1r == c2r:
            print(1)
        else:
            print(0)