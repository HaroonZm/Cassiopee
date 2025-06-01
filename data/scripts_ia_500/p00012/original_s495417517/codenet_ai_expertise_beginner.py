def point_in_triangle():
    while True:
        try:
            values = input().split()
            if len(values) != 8:
                break
            x1, y1, x2, y2, x3, y3, xp, yp = map(float, values)
            
            a = x2 - x1
            b = x3 - x1
            c = xp - x1
            d = y2 - y1
            e = y3 - y1
            f = yp - y1
            
            det = a * e - b * d
            if det == 0:
                print("NO")
                continue
            
            s = (c * e - b * f) / det
            t = (a * f - c * d) / det
            
            if 0 < s < 1 and 0 < t < 1 and 0 < s + t < 1:
                print("YES")
            else:
                print("NO")
        except EOFError:
            break

point_in_triangle()