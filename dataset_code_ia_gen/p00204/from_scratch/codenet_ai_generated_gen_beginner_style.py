while True:
    line = input()
    if line == '':
        continue
    R, N = map(int, line.split())
    if R == 0 and N == 0:
        break
    ufos = []
    for _ in range(N):
        x0, y0, r, v = map(int, input().split())
        ufos.append([x0, y0, r, v])
    # 時間 t を 1 分から初めて1分間隔でレーザー発射
    # 敵は原点に向かって直進する
    # 敵の位置は (x0, y0) -> 原点への単位ベクトル u = (-x0, -y0)/dist
    # t 分後の中心位置は (x0, y0) + v * t * u
    # 1分目以降のレーザー発射時点で一番近い敵を狙い撃ちし、その方向の一直線上にある敵は全て撃墜
    # 撃墜された敵は除去
    # レーザー威力がない範囲 R 内に入った敵は数える（撃墜されないで入る敵）
    # 時間は整数分で進む。ただしいつまで続けるかを決めないといけない
    # 敵は原点に向かうのでいずれ原点に到達（またはR内に入るか撃墜される）
    # なので敵全滅か、全てがR以内に入ったかで終了
    from math import sqrt
    alive = ufos[:]
    entered = 0
    t = 1
    while True:
        if len(alive) == 0:
            break
        # 現在の敵の位置を計算
        positions = []
        for ufo in alive:
            x0, y0, r, v = ufo
            dist = sqrt(x0*x0 + y0*y0)
            if dist == 0:
                # 既に原点にいる
                posx, posy = 0,0
            else:
                ux = -x0 / dist
                uy = -y0 / dist
                posx = x0 + v * t * ux
                posy = y0 + v * t * uy
            positions.append((posx, posy, r, ufo))
        # R以下の敵は数える（レーザー威力が出ない範囲内に入った）
        still_alive = []
        entered_this_time = 0
        for posx, posy, r, ufo in positions:
            distc = sqrt(posx*posx + posy*posy)
            if distc <= R:
                entered_this_time += 1
            else:
                still_alive.append((posx, posy, r, ufo))
        entered += entered_this_time
        # 撃墜する敵を狙うのは1分後以降なので1分目から発射
        # 狙う敵は今生きててRより遠い敵のうち一番近い敵
        targets = [e for e in still_alive if sqrt(e[0]*e[0]+e[1]*e[1]) > R]
        if len(targets) == 0:
            # 狙う敵なし => 残りはR以内かもういない
            break
        # 最も近い敵
        targets.sort(key=lambda e: sqrt(e[0]*e[0]+e[1]*e[1]))
        tx, ty, tr, tufo = targets[0]
        # レーザーは直線上で貫通。レーザーは原点からtx,ty方向の無限線
        # この線上にある敵は撃墜される
        # レーザーの方向ベクトルは (tx, ty)
        if tx == 0 and ty == 0:
            # 0ベクトルはありえないがもしあれば撃墜はすべて
            # 全敵撃墜
            alive = []
            break
        dx = tx
        dy = ty
        # dx, dy > 0 または < 0 は考えず符号はそのまま使う
        new_alive = []
        for posx, posy, r, ufo in still_alive:
            # 原点からの距離
            distc = sqrt(posx*posx + posy*posy)
            # 判定のためにベクトル内積を使う
            # ベクトルa = (posx, posy), ベクトルb = (dx, dy)
            # aはbの方向にあるかどうか（aとbの内積>0かつ外積=0に近いか）
            dot = posx*dx + posy*dy
            # 外積的にほぼ一直線上か（浮動小数点誤差考慮）
            cross = abs(posx*dy - posy*dx)
            # しきい値小さくとる（例1e-8）
            # dot>0：原点から見て同じ方向の半直線上にいる
            # cross<しきい値：一直線上にいる
            if dot > 0 and cross < 1e-8:
                # この敵は撃墜されるから除く
                continue
            else:
                new_alive.append((posx, posy, r, ufo))
        alive = [u[3] for u in new_alive]
        t += 1
    print(entered)