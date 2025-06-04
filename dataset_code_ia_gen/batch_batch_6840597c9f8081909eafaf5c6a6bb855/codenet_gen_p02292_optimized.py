def ccw(ax, ay, bx, by, cx, cy):
    dx1, dy1 = bx - ax, by - ay
    dx2, dy2 = cx - ax, cy - ay
    cross = dx1 * dy2 - dy1 * dx2
    if cross > 0:
        return 1  # COUNTER_CLOCKWISE
    if cross < 0:
        return 2  # CLOCKWISE
    dot = dx1 * dx2 + dy1 * dy2
    if dot < 0:
        return 3  # ONLINE_BACK
    sq_len = dx1 * dx1 + dy1 * dy1
    if dot > sq_len:
        return 4  # ONLINE_FRONT
    return 5  # ON_SEGMENT

p0x, p0y, p1x, p1y = map(int, input().split())
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    r = ccw(p0x, p0y, p1x, p1y, x, y)
    if r == 1:
        print("COUNTER_CLOCKWISE")
    elif r == 2:
        print("CLOCKWISE")
    elif r == 3:
        print("ONLINE_BACK")
    elif r == 4:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")