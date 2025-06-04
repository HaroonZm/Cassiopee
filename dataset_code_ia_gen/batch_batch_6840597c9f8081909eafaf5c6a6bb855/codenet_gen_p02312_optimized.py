import math
def area_circle_polygon_intersection(n, r, points):
    def cross(ax, ay, bx, by):
        return ax*by - ay*bx
    def dist2(x, y):
        return x*x + y*y
    def angle(x, y):
        return math.atan2(y, x)
    def seg_circle_intersections(x1, y1, x2, y2, r):
        dx, dy = x2 - x1, y2 - y1
        A = dx*dx + dy*dy
        B = 2*(x1*dx + y1*dy)
        C = x1*x1 + y1*y1 - r*r
        disc = B*B - 4*A*C
        res = []
        if disc < -1e-14:
            return res
        if disc < 1e-14:
            t = -B/(2*A)
            if 0 <= t <= 1:
                res.append((x1 + t*dx, y1 + t*dy))
            return res
        sqrt_disc = math.sqrt(disc)
        t1 = (-B - sqrt_disc)/(2*A)
        t2 = (-B + sqrt_disc)/(2*A)
        if 0 <= t1 <= 1:
            res.append((x1 + t1*dx, y1 + t1*dy))
        if 0 <= t2 <= 1:
            res.append((x1 + t2*dx, y1 + t2*dy))
        return res
    def sector_area(x1, y1, x2, y2):
        a1 = angle(x1, y1)
        a2 = angle(x2, y2)
        da = a2 - a1
        if da <= -math.pi:
            da += 2*math.pi
        elif da > math.pi:
            da -= 2*math.pi
        return 0.5 * r*r * da
    area = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        d1 = dist2(x1, y1)
        d2 = dist2(x2, y2)
        inside1 = d1 <= r*r + 1e-15
        inside2 = d2 <= r*r + 1e-15
        inters = seg_circle_intersections(x1, y1, x2, y2, r)
        if inside1 and inside2:
            area += cross(x1, y1, x2, y2)/2
        elif inside1 and not inside2:
            if inters:
                ix, iy = inters[0]
                area += cross(x1, y1, ix, iy)/2
                area += sector_area(ix, iy, x2, y2)
            else:
                area += sector_area(x1, y1, x2, y2)
        elif not inside1 and inside2:
            if inters:
                ix, iy = inters[0]
                area += cross(ix, iy, x2, y2)/2
                area += sector_area(x1, y1, ix, iy)
            else:
                area += sector_area(x1, y1, x2, y2)
        else:
            if len(inters) == 2:
                (ix1, iy1), (ix2, iy2) = inters
                area += cross(ix1, iy1, ix2, iy2)/2
                area += sector_area(x1, y1, ix1, iy1)
                area += sector_area(ix2, iy2, x2, y2)
            else:
                area += sector_area(x1, y1, x2, y2)
    return abs(area)
n, r = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
res = area_circle_polygon_intersection(n, r, points)
print(res)