def rot(x, y, t):
    v = [0.0, 0.0]
    v[0] = ((1 - t ** 2) * x + 2 * t * y) / (t ** 2 + 1)
    v[1] = (2 * t * x + (t ** 2 - 1) * y) / (t ** 2 + 1)
    return v

import sys

v = [0.0, 0.0]

for line in sys.stdin:
    ipt = line.split(',')
    x = [float(ipt[i]) for i in range(0, 6, 2)]
    y = [float(ipt[j]) for j in range(1, 6, 2)]
    if x[1] != x[0]:
        v = rot(x[2] - x[0], y[2] - y[0], (y[1] - y[0]) / (x[1] - x[0]))
        v[0] += x[0]
        v[1] += y[0]
    else:
        v = [-x[2], y[2]]
    print("%.6f %.6f" % (0.0 + v[0], 0.0 + v[1]))