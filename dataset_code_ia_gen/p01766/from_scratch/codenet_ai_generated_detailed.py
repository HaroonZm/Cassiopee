import math
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    
    # 各記録を格納するリスト
    records = []
    for _ in range(N):
        f, a, t, x, y = map(int, input().split())
        records.append((f, a, t, x, y))
    
    # チームごとに最長のパスの情報を記録
    # 辞書の形式: key = チーム(t:0 or 1), value = (max_distance, min_time)
    # 初期値はパスなしを示す(-1, -1)
    longest_pass = {
        0: (-1, -1),
        1: (-1, -1)
    }
    
    for i in range(N-1):
        f1, a1, t1, x1, y1 = records[i]
        f2, a2, t2, x2, y2 = records[i+1]
        
        # 同じチームかつ背番号が異なる場合パスとみなす
        if t1 == t2 and a1 != a2:
            # 距離計算（ユークリッド距離）
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            # 時間計算（フレーム差を60で割って秒数に）
            time = (f2 - f1) / 60
            
            max_dist, min_time = longest_pass[t1]
            # 距離比較、距離が大きいか距離が等しくて時間が短い場合更新
            if dist > max_dist or (math.isclose(dist, max_dist, abs_tol=1e-12) and (min_time == -1 or time < min_time)):
                longest_pass[t1] = (dist, time)
    
    # 出力フォーマットは距離と時間の両方を小数点以下10桁程度で表示、誤差1e-3許容
    for team in [0, 1]:
        dist, time = longest_pass[team]
        if dist == -1 and time == -1:
            print(-1, -1)
        else:
            print(f"{dist:.10f} {time:.10f}")

if __name__ == "__main__":
    main()