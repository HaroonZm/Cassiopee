from math import sin, cos, radians, acos

def calc_dist(a, b, c, d):
    a = radians(a)
    c = radians(c)
    alpha = sin(a) * sin(c) + cos(a) * cos(c) * cos(radians(d) - radians(b))
    return int((6378.1 * acos(alpha)) + 0.5)

while True:
    try:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) != 4:
            continue
        a, b, c, d = map(float, parts)
        if a == -1 and b == -1 and c == -1 and d == -1:
            break
        dist = calc_dist(a, b, c, d)
        print(dist)
    except EOFError:
        break