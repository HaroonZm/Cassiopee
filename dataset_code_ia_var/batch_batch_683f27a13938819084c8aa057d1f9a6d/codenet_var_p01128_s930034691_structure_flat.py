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
        parts = input().split()
        sx = int(parts[0])
        sy = int(parts[1])
        tx = int(parts[2])
        ty = int(parts[3])
        o = int(parts[4])
        l = int(parts[5])
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
        intersections.add((r, o == l))
    sorted_inters = sorted(intersections)
    pl = -1
    counter = -1
    i = 0
    while i < len(sorted_inters):
        r, l = sorted_inters[i]
        if pl != l:
            counter += 1
        pl = l
        i += 1
    if counter < 0:
        print(0)
    else:
        print(counter)