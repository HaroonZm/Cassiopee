import sys
import bisect
import math

def main():
    input = sys.stdin.readline

    N = int(input())
    T = []
    A = []
    for _ in range(N):
        t, a = map(int, input().split())
        T.append(t)
        A.append(a)

    # 地震の影響はパフォーマンスが10 * p パーセント低下すること。
    # つまり、パフォーマンスは (1 - 0.1 * p) 倍される。
    # 複数回の地震がある場合は掛け算される。
    # よって、時刻範囲内の地震の掛け合わせた影響を求めるために
    # log空間で処理すると計算が楽。具体的には log(パフォーマンス倍率)の累積和をとる。

    # 初期パフォーマンスは 10^9

    # 各地震の倍率 (1 - 0.1 * A_i)
    factors = [(1 - 0.1 * a) for a in A]

    # log変換（自然対数）
    # 0 <= A_i <= 7より、factor は 1,0.9,...0.3 の範囲
    # 0はあり得るが、A_i=7のときfactor=0.3 > 0なのでlogは常に定義される
    log_factors = [math.log(f) for f in factors]

    # 累積和を作成し、二分探索で範囲の和を高速取得する
    prefix_log = [0]
    for val in log_factors:
        prefix_log.append(prefix_log[-1] + val)

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        # L < R で、地震発生時刻と作業開始または終了時刻が同タイミングではない

        # 作業時間内で発生した地震は T_i が L < T_i < R のもの
        # したがって、T_i > L かつ T_i < R のインデックス区間を求める

        left_idx = bisect.bisect_right(T, L)  # Lより大きい最初の位置
        right_idx = bisect.bisect_left(T, R)  # Rより小さい最後の位置 + 1

        # 対象となるlog_factors の和を計算
        total_log = prefix_log[right_idx] - prefix_log[left_idx]

        # 累積倍率
        total_factor = math.exp(total_log)

        # 最終パフォーマンス
        result = 1e9 * total_factor

        # 精度考慮し浮動小数点形式で出力
        print(f'{result:.12f}')

if __name__ == '__main__':
    main()