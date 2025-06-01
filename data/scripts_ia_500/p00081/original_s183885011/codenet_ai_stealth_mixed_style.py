def rot(x, y, t):
    result = [0, 0]
    result[0] = ((1 - t**2) * x + 2 * t * y) / (t**2 + 1)
    result[1] = (2 * t * x + (t**2 - 1) * y) / (t**2 + 1)
    return result

import sys

v = [0.0, 0.0]
for line in sys.stdin:
    ipt = line.strip().split(',')
    x = list(map(float, [ipt[i] for i in (0, 2, 4)]))
    y = []
    j = 1
    while j < 6:
        y.append(float(ipt[j]))
        j += 2
    if x[1] != x[0]:
        t = (y[1] - y[0]) / (x[1] - x[0])
        rotated = rot(x[2] - x[0], y[2] - y[0], t)
        v = [rotated[0] + x[0], rotated[1] + y[0]]
    else:
        v = []
        v.append(-x[2])
        v.append(y[2])
    print("%.6f %.6f" % (v[0] + 0.0, v[1] + 0.0))