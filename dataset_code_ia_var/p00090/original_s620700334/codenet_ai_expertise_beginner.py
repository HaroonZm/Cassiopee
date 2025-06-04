EPS = 1e-8

def get_cross_points(c1, c2, cross_points):
    # Get intersection points of two circles of radius 1
    x1, y1 = c1.real, c1.imag
    x2, y2 = c2.real, c2.imag
    dx = (x1 - x2) / 2
    dy = (y1 - y2) / 2
    dist = (dx * dx + dy * dy) ** 0.5
    if dist * dist > 1.0 + EPS:
        return
    h = (1.0 - dist * dist) ** 0.5
    if dist == 0:
        return
    k = h / dist
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    cross_points.append(complex(cx + k * dy, cy - k * dx))
    cross_points.append(complex(cx - k * dy, cy + k * dx))

while True:
    n = int(input())
    if n == 0:
        break
    circles = []
    for _ in range(n):
        s = input()
        x_str, y_str = s.split(',')
        x = float(x_str)
        y = float(y_str)
        circles.append(complex(x, y))
    cross_points = []
    for i in range(n):
        for j in range(i+1, n):
            get_cross_points(circles[i], circles[j], cross_points)
    max_cover = 0
    for pt in cross_points:
        count = 0
        for c in circles:
            dx = c.real - pt.real
            dy = c.imag - pt.imag
            d2 = dx*dx + dy*dy
            if abs(d2 - 1.0) <= EPS or d2 <= 1.0:
                count += 1
        if count > max_cover:
            max_cover = count
    if max_cover == 0:
        print(1)
    else:
        print(max_cover)