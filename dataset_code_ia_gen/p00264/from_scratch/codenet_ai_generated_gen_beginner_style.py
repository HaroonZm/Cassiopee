import math
import sys

def in_fan_area(px, py, cx, cy, w, a, d):
    # px, py: 点の座標
    # cx, cy: 扇形の中心(花の位置)
    # w: 風の向かう方向(角度度数法、0はx正方向、反時計回り)
    # a: 扇形の半径
    # d: 扇形の広がり角度
    # 原点からのベクトル
    dx = px - cx
    dy = py - cy
    dist = math.sqrt(dx*dx + dy*dy)
    if dist > a + 0.000001:
        return False
    # 点の角度 [0,360)
    angle = math.degrees(math.atan2(dy, dx))
    if angle < 0:
        angle += 360
    # 風の方向wは扇形の中心
    # 扇形はwを中心に±d/2
    left_bound = (w - d/2) % 360
    right_bound = (w + d/2) % 360

    if left_bound <= right_bound:
        return left_bound <= angle <= right_bound
    else:
        # 角度が360をまたぐ場合
        return angle >= left_bound or angle <= right_bound

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        H_R = line.strip().split()
        if len(H_R) != 2:
            continue
        H, R = map(int, H_R)
        if H == 0 and R == 0:
            break
        houses = []
        count = 0
        while len(houses) < H:
            line = sys.stdin.readline()
            if not line:
                return
            if line.strip() == '':
                continue
            x, y = map(int, line.strip().split())
            houses.append( (x, y) )
        # U M S du dm ds
        while True:
            line = sys.stdin.readline()
            if not line:
                return
            if line.strip() == '':
                continue
            break
        U, M, S, du, dm, ds = map(int, line.strip().split())
        ume_others = []
        for _ in range(U):
            while True:
                line = sys.stdin.readline()
                if not line:
                    return
                if line.strip() == '':
                    continue
                break
            x, y = map(int, line.strip().split())
            ume_others.append( (x, y) )
        momo = []
        for _ in range(M):
            while True:
                line = sys.stdin.readline()
                if not line:
                    return
                if line.strip() == '':
                    continue
                break
            x, y = map(int, line.strip().split())
            momo.append( (x, y) )
        sakura = []
        for _ in range(S):
            while True:
                line = sys.stdin.readline()
                if not line:
                    return
                if line.strip() == '':
                    continue
                break
            x, y = map(int, line.strip().split())
            sakura.append( (x, y) )
        wind = []
        for _ in range(R):
            while True:
                line = sys.stdin.readline()
                if not line:
                    return
                if line.strip() == '':
                    continue
                break
            w_i, a_i = map(int, line.strip().split())
            wind.append( (w_i, a_i) )
        # 私の梅は原点（0,0）
        # 香り判定
        # 風の向かう方向 w, 強さ a, 扇形は w方向を中心にdu/2広がり、距離aまで
        # 他花は同様に扇形(角度dm, ds)、距離a
        # 判定
        # 香りが届くかを判定：私の梅(0,0)と風(R)で香りの扇形内に家があるかなど
        # ただし私の梅の香りは距離a,角度duで扇形。家がこの範囲なら梅の香りが届く。
        # 他花も同様に判定
        # 一日ごとに家の位置を判定し、私の梅の香りだけが届く日はカウントする

        # 全家に対し日数格納
        only_ume_counts = [0]*H

        for w_i, a_i in wind:
            for i in range(H):
                hx, hy = houses[i]
                # 私の梅の香りが届くか？
                ume_reach = in_fan_area(hx, hy, 0, 0, w_i, a_i, du)
                if not ume_reach:
                    continue
                # 他の花の香りが届くか調べる
                others_reach = False
                # 梅以外の梅
                for ux, uy in ume_others:
                    if in_fan_area(hx, hy, ux, uy, w_i, a_i, du):
                        others_reach = True
                        break
                if others_reach:
                    continue
                # 桃
                for mx, my in momo:
                    if in_fan_area(hx, hy, mx, my, w_i, a_i, dm):
                        others_reach = True
                        break
                if others_reach:
                    continue
                # 桜
                for sx, sy in sakura:
                    if in_fan_area(hx, hy, sx, sy, w_i, a_i, ds):
                        others_reach = True
                        break
                if others_reach:
                    continue
                # 私の梅だけの香りが届く日
                only_ume_counts[i] += 1

        max_days = max(only_ume_counts)
        if max_days == 0:
            print("NA")
        else:
            result = []
            for i, val in enumerate(only_ume_counts):
                if val == max_days:
                    # 家番号は1から
                    result.append(str(i+1))
            print(" ".join(result))

if __name__ == "__main__":
    main()