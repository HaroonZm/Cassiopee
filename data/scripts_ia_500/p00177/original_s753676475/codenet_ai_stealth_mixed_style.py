from math import radians, cos, sin, acos
while True:
    A = raw_input().split()
    if A == ['-1', '-1', '-1', '-1']:
        break
    a, b, c, d = list(map(lambda x: radians(float(x)), A))
    product = cos(a)*cos(c)*cos(b - d) + sin(a)*sin(c)
    distance = 6378.1 * acos(product)
    print int(round(distance))