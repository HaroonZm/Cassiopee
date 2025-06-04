while 1:
    try:
        x1, y1, x2, y2, xq, yq = map(float, raw_input().split(','))
        a = y2 - y1
        b = -(x2 - x1)
        c = x2 * y1 - x1 * y2
        den = a ** 2 + b ** 2
        xr = xq - 2 * a * (a * xq + b * yq + c) / den
        yr = yq - 2 * b * (a * xq + b * yq + c) / den
        print xr, yr
    except:
        break