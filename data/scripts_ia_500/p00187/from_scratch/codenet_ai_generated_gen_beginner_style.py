def line_intersection(a1, b1, a2, b2):
    # 直線の交点を求める (x, y)
    # 線分は (x1,y1)-(x2,y2) で与えられる
    x1, y1, x2, y2 = a1[0], a1[1], b1[0], b1[1]
    x3, y3, x4, y4 = a2[0], a2[1], b2[0], b2[1]

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None  # 平行または同一直線上
    t = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        return (x, y)
    else:
        return None  # 線分の範囲外

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def triangle_area(p1, p2, p3):
    # 座標3点の三角形の面積
    return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2

def same_line(p1, p2, p3):
    # 3点が同一直線上か
    return abs((p2[1]-p1[1])*(p3[0]-p2[0]) - (p3[1]-p2[1])*(p2[0]-p1[0])) < 1e-10

def main():
    while True:
        lines = []
        for _ in range(3):
            line = input().strip()
            if line == '':
                return
            x1, y1, x2, y2 = map(int, line.split())
            lines.append(((x1,y1),(x2,y2)))
        if lines == [((0,0),(0,0)), ((0,0),(0,0)), ((0,0),(0,0))]:
            break

        p1 = line_intersection(lines[0][0], lines[0][1], lines[1][0], lines[1][1])
        p2 = line_intersection(lines[1][0], lines[1][1], lines[2][0], lines[2][1])
        p3 = line_intersection(lines[2][0], lines[2][1], lines[0][0], lines[0][1])

        if p1 is None or p2 is None or p3 is None:
            print("kyo")
            continue

        # 3点が同一直線上か
        if same_line(p1, p2, p3):
            print("kyo")
            continue

        # 3つが1点に集中してないか (小さい範囲で全部同じ点)
        if distance(p1,p2) < 1e-10 and distance(p2,p3) < 1e-10:
            print("kyo")
            continue

        area = triangle_area(p1, p2, p3)

        if area >= 1900000:
            print("dai-kichi")
        elif area >= 1000000:
            print("chu-kichi")
        elif area >= 100000:
            print("kichi")
        elif area > 0:
            print("syo-kichi")
        else:
            print("kyo")

main()