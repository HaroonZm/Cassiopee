import math
ss = input().split()
while 1:
    x1, y1, x2, y2, x3, y3, xp, yp = map(float, ss)
    a = x2 - x1
    b = x3 - x1
    c = xp - x1
    d = y2 - y1
    e = y3 - y1
    f = yp - y1
    detA = a * e - b * d
    At00 = e
    At01 = -b
    At10 = -d
    At11 = a
    x = (At00 * c + At01 * f) / detA
    y = (At10 * c + At11 * f) / detA
    s = x
    t = y
    if 0 < s < 1 and 0 < t < 1 and 0 < s + t < 1:
        print('YES')
    else:
        print('NO')
    try:
        ss = input().split()
    except EOFError:
        break