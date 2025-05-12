import math
a,b,h,m = map(int,input().split())
h %= 12
h *= 60
h = h + m
ma = m * 6
ha = h * 0.5
print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(min(ma-ha,ha-ma)))))