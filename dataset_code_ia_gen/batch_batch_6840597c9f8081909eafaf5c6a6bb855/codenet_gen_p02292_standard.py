def ccw(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    dx1, dy1 = x1 - x0, y1 - y0
    dx2, dy2 = x2 - x0, y2 - y0
    cross = dx1*dy2 - dy1*dx2
    if cross > 0:
        return 1  # COUNTER_CLOCKWISE
    if cross < 0:
        return 2  # CLOCKWISE
    dot = dx1*dx2 + dy1*dy2
    if dot < 0:
        return 3  # ONLINE_BACK
    sq_len = dx1*dx1 + dy1*dy1
    sq_len2 = dx2*dx2 + dy2*dy2
    if sq_len < sq_len2:
        return 4  # ONLINE_FRONT
    return 5  # ON_SEGMENT

x0, y0, x1, y1 = map(int, input().split())
q = int(input())
p0, p1 = (x0, y0), (x1, y1)
for _ in range(q):
    x2, y2 = map(int, input().split())
    res = ccw(p0, p1, (x2, y2))
    if res == 1:
        print("COUNTER_CLOCKWISE")
    elif res == 2:
        print("CLOCKWISE")
    elif res == 3:
        print("ONLINE_BACK")
    elif res == 4:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")