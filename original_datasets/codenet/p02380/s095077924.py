import math
a,b,C = map(float,input().split())
C_rad=math.pi*C/180
print("{0:.8f}".format(math.sin(C_rad)*a*b/2))
print("{0:.8f}".format(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(C_rad))))
print("{0:.8f}".format(b*math.sin(C_rad)))