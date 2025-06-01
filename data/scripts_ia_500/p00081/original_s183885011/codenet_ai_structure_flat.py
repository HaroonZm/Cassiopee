import sys
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
        denom = t * t + 1
        v0 = ((1 - t * t) * (x2 - x0) + 2 * t * (y2 - y0)) / denom + x0
        v1 = (2 * t * (x2 - x0) + (t * t - 1) * (y2 - y0)) / denom + y0
    else:
        v0 = -x2
        v1 = y2
    print("%.6f %.6f" % (v0, v1))