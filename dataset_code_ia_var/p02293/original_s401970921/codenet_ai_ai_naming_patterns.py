for case_idx in range(int(input())):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    dx1 = x1 - x0
    dy1 = y1 - y0
    dx2 = x3 - x2
    dy2 = y3 - y2
    if dx1 * dx2 == -dy1 * dy2:
        print(1)
    elif dx1 * dy2 == dy1 * dx2:
        print(2)
    else:
        print(0)