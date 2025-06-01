from math import sqrt, cos, sin, acos, pi

def norm_sq(v):
    return sum(x**2 for x in v)

def convert_deg_to_rad(angle):
    return (angle / 360) * 2 * pi

def vector_from_angles(a, b):
    return [cos(b)*cos(a), sin(b)*cos(a), sin(a)]

def dot_product(u, v):
    res = 0
    for i in range(len(u)):
        res += u[i]*v[i]
    return res

while 1:
    s = input()
    if s == '-1 -1 -1 -1':
        break
    parts = s.split()
    floats = list(map(float, parts))
    angles_rad = list(map(convert_deg_to_rad, floats))
    a, b, c, d = angles_rad
    x1, y1, z1 = vector_from_angles(a, b)
    x2, y2, z2 = vector_from_angles(c, d)
    dp = dot_product([x1, y1, z1], [x2, y2, z2])
    if dp > 1: dp = 1
    elif dp < -1: dp = -1
    theta = acos(dp)
    dist = round(6378.1 * theta)
    print(dist)