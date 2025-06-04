import sys
v = [0.0, 0.0]
for line in sys.stdin:
    ipt = line.split(',')
    x0 = float(ipt[0])
    y0 = float(ipt[1])
    x1 = float(ipt[2])
    y1 = float(ipt[3])
    x2 = float(ipt[4])
    y2 = float(ipt[5])
    if x1 != x0:
        t = (y1 - y0) / (x1 - x0)
        xx = x2 - x0
        yy = y2 - y0
        denom = t ** 2 + 1
        v0 = ((1 - t ** 2) * xx + 2 * t * yy) / denom
        v1 = (2 * t * xx + (t ** 2 - 1) * yy) / denom
        v[0] = v0 + x0
        v[1] = v1 + y0
    else:
        v[0] = -x2
        v[1] = y2
    print("%.6f %.6f" % (v[0], v[1]))