import math

def distance(point):
    return (point[0]**2 + point[1]**2) ** 0.5

def read_points(num):
    points = []
    for _ in range(num):
        line = input()
        x, y, *rest = line.split()
        points.append([int(x), int(y)] if not rest else [int(x), int(y), int(rest[0])])
    return points

def compare(a, b):
    return a > b or abs(a - b) < 0.000001

def is_safe(point):
    tx, ty, sx, sy = point
    results = []
    for wp in WP:
        wx, wy, r = wp
        wt = [tx - wx, ty - wy]
        rwt = distance(wt)
        sw = [wx - sx, wy - sy]
        rsw = distance(sw)
        st = [tx - sx, ty - sy]
        rst = distance(st)

        inside_wp = [rwt < r, rsw < r]

        if rst == 0:
            c = 1
        elif inside_wp == [True, True]:
            c = 1
        elif inside_wp == [True, False] or inside_wp == [False, True]:
            c = 0
        else:
            a = math.pi/2 - math.acos(r/rsw)
            dot_product = sw[0]*st[0] + sw[1]*st[1]
            cos_angle = round(dot_product / (rsw * rst), 4)
            b = math.acos(cos_angle)
            if compare(a, b) and compare(rst**2, rsw**2 - r**2):
                c = 0
            else:
                c = 1
        results.append(c)
    return all(results)

while True:
    n = int(input())
    if n == 0:
        break
    WP = read_points(n)
    p_num = int(input())
    P = read_points(p_num)
    for point in P:
        print("Safe" if is_safe(point) else "Danger")