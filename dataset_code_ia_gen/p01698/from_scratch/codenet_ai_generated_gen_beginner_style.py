import sys
import math

def solve():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        stars = []
        for _ in range(n):
            px, py, pz, vx, vy, vz, r, vr = map(float, input().split())
            stars.append([px, py, pz, vx, vy, vz, r, vr])

        # 初期はすべて自然消滅時刻に設定
        # 自然消滅時刻 = r / vr
        destruction = [star[6] / star[7] for star in stars]
        destroyed = [False] * n

        # 衝突時刻をすべてのペアで調べる（簡単な二次方程式の解法）
        # 球の距離の二乗が半径和の二乗以下の時点が衝突時刻
        # 距離^2 = (px_i + t vx_i - (px_j + t vx_j))^2 + ...
        # 半径和 = (r_i - t vr_i) + (r_j - t vr_j)
        # 距離^2 = d0^2 + 2 d0 d_vel t + (d_vel)^2 t^2
        # 半径和^2 = (r_i + r_j - t(vr_i + vr_j))^2
        # 整理して二次方程式 a t^2 + b t + c = 0 を解く

        for i in range(n):
            for j in range(i+1, n):
                px1, py1, pz1, vx1, vy1, vz1, r1, vr1 = stars[i]
                px2, py2, pz2, vx2, vy2, vz2, r2, vr2 = stars[j]

                dx0 = px1 - px2
                dy0 = py1 - py2
                dz0 = pz1 - pz2
                dvx = vx1 - vx2
                dvy = vy1 - vy2
                dvz = vz1 - vz2
                dr = r1 + r2
                dvr = vr1 + vr2

                # 距離^2の係数
                a = dvx*dvx + dvy*dvy + dvz*dvz - dvr*dvr
                b = 2 * (dx0*dvx + dy0*dvy + dz0*dvz) + 2*dr*dvr
                c = dx0*dx0 + dy0*dy0 + dz0*dz0 - dr*dr

                # 二次方程式 a t^2 + b t + c = 0
                # 衝突時刻t >= 0かつt <=消滅時間
                # 注意: a = 0 の場合線形方程式となる
                if abs(a) < 1e-14:
                    if abs(b) < 1e-14:
                        continue
                    t = -c / b
                    if t >= 1e-9:
                        # 半径が自然消滅より前なら更新
                        if t < destruction[i] and t < destruction[j]:
                            destruction[i] = t
                            destruction[j] = t
                    continue

                disc = b*b - 4*a*c
                if disc < -1e-14:
                    continue
                if disc < 0:
                    disc = 0.0
                sqrt_disc = math.sqrt(disc)

                t1 = (-b - sqrt_disc) / (2*a)
                t2 = (-b + sqrt_disc) / (2*a)
                candidates = []
                if t1 >= 1e-9:
                    candidates.append(t1)
                if t2 >= 1e-9:
                    candidates.append(t2)
                if len(candidates) == 0:
                    continue
                tcol = min(candidates)
                # 衝突時刻tcolが両流れ星の自然消滅より前であれば更新
                if tcol < destruction[i] and tcol < destruction[j]:
                    destruction[i] = tcol
                    destruction[j] = tcol

        for t in destruction:
            print("%.10f" % t)

if __name__ == "__main__":
    solve()