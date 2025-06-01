def sp(a, b, c, xq, yq):
    den = a**2 + b**2
    val = (a * xq + b * yq + c) / den
    return (xq - 2 * a * val, yq - 2 * b * val)

import sys
for line in sys.stdin:
    try:
        parts = line.strip().split(',')
        if len(parts) != 6:
            break
        x1, y1, x2, y2, xq, yq = map(float, parts)
        a = y2 - y1
        b = -(x2 - x1)
        c = x2 * y1 - x1 * y2
        res = sp(a, b, c, xq, yq)
        print res[0], res[1]
    except Exception:
        break