from math import sin, cos, sqrt, pi

def get_vals():
    vals = input()
    return [float(x) for x in vals.strip().split()]

(a, b, deg) = get_vals()
rad = deg/180*pi

def triangle_area(base, height):
    return base * height * 0.5

h = sin(rad) * b

def perimeter(x, y, angle):
    c = sqrt(x**2 + y**2 - 2*x*y*cos(angle))
    return [x + y + c, c]

L, c = perimeter(a, b, rad)
S = triangle_area(a, h)

print("{0:.5f} {1:.5f} {2:.5f}".format(S, L, h))