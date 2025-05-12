while 1:
    n = input()
    if n == 0: break
    p = set([tuple(map(int, raw_input().split())) for i in range(n)])
    m = input()
    q = set([tuple(map(int, raw_input().split())) for i in xrange(m)])
    ret = False
    for px, py in p:
        if ret: break
        for qx, qy in q:
            if ret: break
            dx = qx - px
            dy = qy - py
            for x, y in p:
                mx = x + dx
                my = y + dy
                if (mx, my) not in q:
                    break
            else:
                print dx, dy
                ret = True