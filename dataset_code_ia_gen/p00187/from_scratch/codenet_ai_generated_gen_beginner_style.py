def line_intersection(a1, a2, b1, b2):
    # 2点a1, a2を通る直線と2点b1, b2を通る直線の交点を求める
    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = b1
    x4, y4 = b2

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        return None  # 平行または同一直線
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return (px, py)

def on_segment(p1, p2, q):
    # qが線分p1-p2上にあるか判定
    x1, y1 = p1
    x2, y2 = p2
    x, y = q
    if min(x1,x2) - 1e-9 <= x <= max(x1,x2) + 1e-9 and min(y1,y2) - 1e-9 <= y <= max(y1,y2) + 1e-9:
        return True
    return False

def segment_intersection(p1, p2, p3, p4):
    # 2つの線分が交わるか判定し、交点を返す（なければNone）
    pt = line_intersection(p1, p2, p3, p4)
    if pt is None:
        return None
    if on_segment(p1, p2, pt) and on_segment(p3, p4, pt):
        return pt
    return None

def area_triangle(p1, p2, p3):
    # 3点から面積計算
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def is_colinear(p1, p2, p3):
    # 3点が同一直線上か判定
    return abs((p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])) < 1e-9

while True:
    segments = []
    for _ in range(3):
        line = input()
        if line == '':
            break
        x1,y1,x2,y2 = map(int, line.split())
        segments.append(((x1,y1),(x2,y2)))
    if len(segments) < 3:
        break
    if segments == [((0,0),(0,0))]*3:
        break

    # 3線分の交点を求める
    pts = []
    pairs = [(0,1),(1,2),(2,0)]
    any_none = False
    for i,j in pairs:
        inter = segment_intersection(segments[i][0], segments[i][1], segments[j][0], segments[j][1])
        if inter is None:
            any_none = True
            break
        pts.append(inter)
    if any_none:
        print("kyo")
        continue

    # 3つの交点が同一点か(3点一致)や同一直線上か判定
    # 3点が全て近いか
    d01 = (pts[0][0]-pts[1][0])**2 + (pts[0][1]-pts[1][1])**2
    d12 = (pts[1][0]-pts[2][0])**2 + (pts[1][1]-pts[2][1])**2
    d20 = (pts[2][0]-pts[0][0])**2 + (pts[2][1]-pts[0][1])**2
    if d01 < 1e-12 and d12 < 1e-12 and d20 < 1e-12:
        print("kyo")
        continue
    if is_colinear(pts[0], pts[1], pts[2]):
        print("kyo")
        continue

    # さらに2本以上の線分が同一直線状にある場合除外
    # 各線分のベクトルを計算して比を調べる（簡易版）
    v = []
    for seg in segments:
        x1,y1 = seg[0]
        x2,y2 = seg[1]
        v.append((x2 - x1, y2 - y1))
    # 2つのベクトルの外積が0なら同一直線
    same_line_flag = False
    for i in range(3):
        for j in range(i+1,3):
            cross = v[i][0]*v[j][1] - v[i][1]*v[j][0]
            if abs(cross) < 1e-9:
                # 同一直線判定
                same_line_flag = True
    if same_line_flag:
        print("kyo")
        continue

    # 面積計算
    area = area_triangle(pts[0], pts[1], pts[2])
    if area <= 0:
        print("kyo")
        continue

    if area >= 1900000:
        print("dai-kichi")
    elif area >= 1000000:
        print("chu-kichi")
    elif area >= 100000:
        print("kichi")
    else:
        print("syo-kichi")