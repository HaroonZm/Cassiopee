while True:
    try:
        line = input()
        if not line:
            break
        parts = line.strip().split(',')
        x1 = float(parts[0])
        y1 = float(parts[1])
        x2 = float(parts[2])
        y2 = float(parts[3])
        xq = float(parts[4])
        yq = float(parts[5])

        # 線分P1P2の方向ベクトル
        dx = x2 - x1
        dy = y2 - y1

        # 点Qから直線P1P2への垂線の足の座標を求める
        # ベクトルP1Q
        vx = xq - x1
        vy = yq - y1

        # 直線P1P2の単位方向ベクトルの内積による射影距離 t
        t = (vx*dx + vy*dy) / (dx*dx + dy*dy)

        # 垂線の足の座標H
        hx = x1 + t*dx
        hy = y1 + t*dy

        # QとHを通じて、Qを対称軸で反転させた点Rを求める
        rx = 2*hx - xq
        ry = 2*hy - yq

        print(f"{rx:.6f} {ry:.6f}")

    except EOFError:
        break