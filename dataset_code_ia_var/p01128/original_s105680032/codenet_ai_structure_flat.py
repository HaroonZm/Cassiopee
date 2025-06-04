m = int(input())
while m:
    m -= 1
    ax, ay, bx, by = map(int, input().split())
    n = int(input())
    dx = bx - ax
    dy = by - ay
    intersections = set()
    while n:
        n -= 1
        sx, sy, tx, ty, o, l = map(int, input().split())
        tdx = tx - sx
        tdy = ty - sy
        asx = sx - ax
        asy = sy - ay
        denom = dx * tdy - dy * tdx
        if denom == 0:
            continue
        r = (tdy * asx - tdx * asy) / denom
        s = (dy * asx - dx * asy) / denom
        if r <= 0 or r >= 1 or s <= 0 or s >= 1:
            continue
        px = ax + r * dx
        intersections.add((px, o == l))
    pl = -1
    counter = -1
    sorted_list = sorted(intersections)
    for item in sorted_list:
        px, lval = item
        if pl != lval:
            counter += 1
        pl = lval
    if counter < 0:
        print(0)
    else:
        print(counter)