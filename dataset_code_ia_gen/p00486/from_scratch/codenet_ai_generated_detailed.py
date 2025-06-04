# 解法概要
# サンタクロースは任意の交差点に降り立ち、各家へ片道ずつ往復（一旦降りた交差点へ戻る）してチョコレートケーキを届ける。
# 各家 (X_i, Y_i) への往復距離は「2 * マンハッタン距離(降り立つ点, 家の位置)」。
# 総所要時間はすべての家について往復距離の合計。
# 最後の家の配達後戻る時間はカウントしないので、その家の分は「往復距離 - 帰りの1往復分 = 片道距離分」のみとなる。
#
# よって、
# 所要時間 = 全家への「2 * 往路距離」の合計 - 最大の「帰り分(片道距離)」
#          = 2 * Σ(距離降り立つ点→家) - max(距離降り立つ点→家)
#
# これを簡略化すると：
# 総所要時間 = Σ(距離往復分) - 最大1往復の帰り分 = Σ(2 * 距離) - max(距離)
#
# 距離はマンハッタン距離 = |x - X_i| + |y - Y_i|
#
# 不変なのは各家への距離の和の2倍であり、-\max距離の部分で最小化が効く
#
# この問題はまず家のX座標とY座標に分けて考えることができる。
# ・X方向：|x - X_i|
# ・Y方向：|y - Y_i|
#
# Σ |x - X_i| と Σ |y - Y_i| を最小化する x,y を求めることがポイント
#
# Σ|x - X_i| は代表値の1つである中央値で最小化される
#
# また、最大距離のオフセットする点を決める際、問題の条件にしたがって複数解の絞り込みを行う
#
# 具体的に：
# ・降り立つ点は交差点なので整数
# ・複数の点が候補にあれば、x最小 → y最小 の順で選ぶ
#
# 細部は後述の実装で対応

import sys

input = sys.stdin.readline

def main():
    W, H = map(int, input().split())
    N = int(input())
    X = []
    Y = []
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
        points.append((x, y))

    # X,Yそれぞれソートして中央値を求める
    X.sort()
    Y.sort()

    # Σ|x - X_i| が最小となるxはXの中央値
    # Nが奇数ならX[N//2]のみ候補
    # Nが偶数なら中央値は区間内の任意の点（X[N//2-1], X[N//2]）の間
    # だが座標は整数なので候補はこの2点
    # ただしこの2つの任意の間の整数座標は全て同様の距離和となる
    # 最大距離の減少を含めて考えるので
    # 垂直方向でも同様。各座標で試す。
    #
    # よってX候補は中央値の1 or 2個
    # Y候補は中央値の1 or 2個

    candidates_x = []
    if N % 2 == 1:
        candidates_x = [X[N//2]]
    else:
        # 2つの中央値
        candidates_x = [X[(N//2)-1], X[N//2]]

    candidates_y = []
    if N % 2 == 1:
        candidates_y = [Y[N//2]]
    else:
        candidates_y = [Y[(N//2)-1], Y[N//2]]

    # Σ|x - X_i| を事前に計算すると高速
    # しかしN最大10^5なので計算は可能
    # ただし全組合せ試すことは(2x2=4通りなので問題なし)

    # Σ|x - X_i|の計算関数
    def sum_abs_diff(arr, val):
        # arrはソート済み
        # 二分探索利用
        import bisect
        idx = bisect.bisect_left(arr, val)
        left_sum = idx * val - sum(arr[:idx])      # valより左の差分
        right_sum = sum(arr[idx:]) - (len(arr) - idx)*val  # valより右の差分
        return left_sum + right_sum

    # 最大距離を最小化する降り立つ交差点を求める
    # 探索候補は家の座標それぞれ、x,y座標は中央値候補で絞っても
    # 最大距離は家に対して最大 |x - Xi| + |y - Yi| なので
    # 最大距離を最小化する点は「メディアンではないこともある」
    #
    # ただし最大距離最小化点は家の座標または家の座標の間にある点
    # この問題で「最小化対象はΣ距離 - max距離」
    #
    # 試すべき降り立つ点は
    # ・中央値候補での距離和が最小
    # ・max距離を考慮して各候補が最適か検証
    #
    # 探索範囲が大きいので候補点は家の座標にする
    
    # ここで問題の定義に注目：
    # シンプルに全部の交差点を試せないので、
    # 降り立つ点を家の座標のいずれか、または中央値で絞ることで解を出す
    
    # よって候補点は家の座標に絞って試す
    # なお最大距離を計算するのにN回かかるのは重いがN=10^5でpythonでは工夫必要
    
    # 最良の結果保持用
    best_time = None
    best_point = None

    # Σ2*距離 と max距離 を計算する関数
    # 呼び出し回数を削減するため、座標を一本化した試し方をする

    # 4つの中央値候補の組み合わせ＋各家と中央値候補も試す
    candidate_points = set()
    for cx in candidates_x:
        for cy in candidates_y:
            candidate_points.add((cx, cy))
    # 家の座標も候補に加える（複数解の考慮）
    for px, py in points:
        candidate_points.add((px, py))

    # 最小値探索
    for cx, cy in candidate_points:
        # Σ距離
        sum_dist = 0
        max_dist = -1
        for px, py in points:
            d = abs(cx - px) + abs(cy - py)
            sum_dist += d
            if d > max_dist:
                max_dist = d
        total_time = 2 * sum_dist - max_dist
        # 更新条件
        if (best_time is None) or (total_time < best_time) or \
           (total_time == best_time and (cx < best_point[0] or (cx == best_point[0] and cy < best_point[1]))):
            best_time = total_time
            best_point = (cx, cy)

    print(best_time)
    print(best_point[0], best_point[1])

if __name__ == "__main__":
    main()