W, H, M = map(int, input().split())
walls = []
for _ in range(M):
    px, py, qx, qy = map(int, input().split())
    walls.append((px, py, qx, qy))

Q = int(input())
queries = []
for _ in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    queries.append((sx, sy, gx, gy))

def crosses_wall(x1, y1, x2, y2, wall):
    wx1, wy1, wx2, wy2 = wall
    # 壁はx軸かy軸に平行なので、水平か垂直のどちらか
    if wy1 == wy2:  # 水平な壁（y固定）
        wall_y = wy1
        wall_x_min = min(wx1, wx2)
        wall_x_max = max(wx1, wx2)
        # 線分が壁のyをまたぐか判定
        if (y1 - wall_y) * (y2 - wall_y) < 0:
            # 壁のxの範囲内で交差しているか
            # 線分のx座標で壁yと交わる位置を求める
            # 線分の方程式：y = y1 + (y2 - y1)*t, x = x1 + (x2 - x1)*t
            # t は (wall_y - y1) / (y2 - y1)
            t = (wall_y - y1) / (y2 - y1)
            cross_x = x1 + (x2 - x1)*t
            if wall_x_min < cross_x < wall_x_max:
                return True
        return False
    else:  # 垂直な壁（x固定）
        wall_x = wx1
        wall_y_min = min(wy1, wy2)
        wall_y_max = max(wy1, wy2)
        # 線分が壁のxをまたぐか判定
        if (x1 - wall_x) * (x2 - wall_x) < 0:
            t = (wall_x - x1) / (x2 - x1)
            cross_y = y1 + (y2 - y1)*t
            if wall_y_min < cross_y < wall_y_max:
                return True
        return False

for sx, sy, gx, gy in queries:
    count = 0
    for wall in walls:
        if crosses_wall(sx, sy, gx, gy, wall):
            count += 1
    print(count)