# 参考 http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3277276#1
from math import acos, hypot, isclose, sqrt

def intersection(circle, polygon):
    # 円と多角形の共通部分の面積
    # 多角形の点が反時計回りで与えられれば正の値、時計回りなら負の値を返す
    x, y, r = circle
    polygon = [(xp-x, yp-y) for xp, yp in polygon]
    area = 0.0
    for p1, p2 in zip(polygon, polygon[1:] + [polygon[0]]):
        ps = seg_intersection((0, 0, r), (p1, p2))
        for pp1, pp2 in zip([p1] + ps, ps + [p2]):
            c = cross(pp1, pp2)  # pp1 と pp2 の位置関係によって正負が変わる
            if c == 0:  # pp1, pp2, 原点が同一直線上にある場合
                continue
            d1 = hypot(*pp1)
            d2 = hypot(*pp2)
            if le(d1, r) and le(d2, r):
                area += c / 2  # pp1, pp2, 原点を結んだ三角形の面積
            else:
                t = acos(dot(pp1, pp2) / (d1 * d2))  # pp1-原点とpp2-原点の成す角
                sign = 1.0 if c >= 0 else -1.0
                area += sign * r * r * t / 2  # 扇形の面積
    return area

def cross(v1, v2):  # 外積
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - x2 * y1

def dot(v1, v2):  # 内積
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2

def seg_intersection(circle, seg):
    # 円と線分の交点（円の中心が原点でない場合は未検証）
    x0, y0, r = circle
    p1, p2 = seg
    x1, y1 = p1
    x2, y2 = p2

    p1p2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    op1 = (x1 - x0) ** 2 + (y1 - y0) ** 2
    rr = r * r
    dp = dot((x1 - x0, y1 - y0), (x2 - x1, y2 - y1))

    d = dp * dp - p1p2 * (op1 - rr)
    ps = []

    if isclose(d, 0.0, abs_tol=1e-9):
        t = -dp / p1p2
        if ge(t, 0.0) and le(t, 1.0):
            ps.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
    elif d > 0.0:
        t1 = (-dp - sqrt(d)) / p1p2
        if ge(t1, 0.0) and le(t1, 1.0):
            ps.append((x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)))
        t2 = (-dp + sqrt(d)) / p1p2
        if ge(t2, 0.0) and le(t2, 1.0):
            ps.append((x1 + t2 * (x2 - x1), y1 + t2 * (y2 - y1)))

    # assert all(isclose(r, hypot(x, y)) for x, y in ps)
    return ps

def le(f1, f2):  # less equal
    return f1 < f2 or isclose(f1, f2, abs_tol=1e-9)

def ge(f1, f2):  # greater equal
    return f1 > f2 or isclose(f1, f2, abs_tol=1e-9)

N, cx, cy, r = map(int, input().split())
ans = 0
from math import pi
circle_area = pi * r * r
for _ in range(N):
    p, score = map(int, input().split())
    ps = []
    for _ in range(p):
        x, y = map(int, input().split())
        ps.append((x, y))
    area = intersection((cx, cy, r), ps)
    ans += abs(area) * score / circle_area

print(f"{ans:.10f}")