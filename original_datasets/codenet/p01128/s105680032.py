m = int(input())
while m:
    m -= 1
    ax, ay, bx, by = map(int, input().split())
    n = int(input())
    dx, dy = bx - ax, by - ay
    intersections = set()
    while n:
        n -= 1
        sx, sy, tx, ty, o, l = map(int, input().split())
        tdx, tdy = tx - sx, ty - sy
        asx, asy = sx - ax, sy - ay
        denom = dx * tdy - dy * tdx
        if not denom:
            continue
        r = (tdy * asx - tdx * asy) / denom
        s = (dy * asx - dx * asy) / denom
        if not 0 < r < 1 or not 0 < s < 1:
            continue
        px = ax + r * dx
        intersections.add((px, o == l))

    pl, counter = -1, -1
    for px, l in sorted(intersections):
        counter += pl != l
        pl = l
    print(max(counter, 0))