while True:
    n = int(input())
    if n == 0:
        break
    p = []
    for i in range(n):
        x, y = map(int, input().split())
        p.append((x, y))
    m = int(input())
    q = []
    for i in range(m):
        x, y = map(int, input().split())
        q.append((x, y))
    found = False
    for px, py in p:
        if found:
            break
        for qx, qy in q:
            if found:
                break
            dx = qx - px
            dy = qy - py
            all_match = True
            for x, y in p:
                mx = x + dx
                my = y + dy
                if (mx, my) not in q:
                    all_match = False
                    break
            if all_match:
                print(dx, dy)
                found = True