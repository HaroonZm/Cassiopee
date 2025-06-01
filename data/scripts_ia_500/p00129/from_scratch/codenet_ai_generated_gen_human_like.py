import sys
import math

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def line_circle_intersect(s, t, c, r):
    # s, t, c: (x,y), r: radius
    # 判定：線分 st と円 c,r が交わるか
    # ベクトル st, sc を使って円との距離を計算

    sx, sy = s
    tx, ty = t
    cx, cy = c
    r2 = r * r

    vx = tx - sx
    vy = ty - sy
    wx = cx - sx
    wy = cy - sy

    proj = vx*wx + vy*wy
    line_len2 = vx*vx + vy*vy

    # 投影距離が0未満なら最近点はs
    if proj <= 0:
        closest_x, closest_y = sx, sy
    # 投影距離が線分長超えるなら最近点はt
    elif proj >= line_len2:
        closest_x, closest_y = tx, ty
    else:
        rat = proj / line_len2
        closest_x = sx + vx * rat
        closest_y = sy + vy * rat

    d2 = (cx - closest_x)**2 + (cy - closest_y)**2

    # 壁の円筒は「壁の上にはいない」とのことだから
    # 距離が半径以下なら線分上に壁があると判断
    return d2 <= r2

input = sys.stdin.readline

while True:
    n_line = sys.stdin.readline()
    if not n_line:
        break
    n = int(n_line)
    if n == 0:
        break
    walls = []
    for _ in range(n):
        wx, wy, r = map(int, sys.stdin.readline().split())
        walls.append((wx, wy, r))
    m = int(sys.stdin.readline())
    for _ in range(m):
        tx, ty, sx, sy = map(int, sys.stdin.readline().split())
        visible = True
        for (wx, wy, r) in walls:
            if line_circle_intersect((sx, sy), (tx, ty), (wx, wy), r):
                visible = False
                break
        print("Danger" if visible else "Safe")