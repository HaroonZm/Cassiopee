import math
def l2(x,y,z):
    return math.sqrt(x*x+y*y+z*z)
while True:
    s = input()
    if s == '-1 -1 -1 -1':
        break
    a,b,c,d = map(float, s.split())
    a = (a / 360) * 2 * math.pi
    b = (b / 360) * 2 * math.pi
    c = (c / 360) * 2 * math.pi
    d = (d / 360) * 2 * math.pi
    x1 = math.cos(b)*math.cos(a)
    y1 = math.sin(b)*math.cos(a)
    z1 = math.sin(a)
    x2 = math.cos(d)*math.cos(c)
    y2 = math.sin(d)*math.cos(c)
    z2 = math.sin(c)
    theta = math.acos(x1*x2 + y1*y2 + z1*z2)
    print(round(6378.1*theta))