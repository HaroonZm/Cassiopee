while True:
    n = int(input())
    if n == 0:
        break
    walls = []
    for _ in range(n):
        wx, wy, r = map(int, input().split())
        walls.append((wx, wy, r))
    m = int(input())
    for _ in range(m):
        tx, ty, sx, sy = map(int, input().split())
        safe = True
        for (wx, wy, r) in walls:
            # line segment from (sx, sy) to (tx, ty)
            dx = tx - sx
            dy = ty - sy
            fx = sx - wx
            fy = sy - wy
            a = dx*dx + dy*dy
            b = 2*(fx*dx + fy*dy)
            c = fx*fx + fy*fy - r*r
            discriminant = b*b - 4*a*c
            if discriminant < 0:
                # no intersection
                continue
            else:
                discriminant_sqrt = discriminant**0.5
                t1 = (-b - discriminant_sqrt)/(2*a)
                t2 = (-b + discriminant_sqrt)/(2*a)
                # check if any intersection point lies on the segment (0<=t<=1)
                if (0 < t1 < 1) or (0 < t2 < 1):
                    safe = False
                    break
        if safe:
            print("Danger")
        else:
            print("Safe")