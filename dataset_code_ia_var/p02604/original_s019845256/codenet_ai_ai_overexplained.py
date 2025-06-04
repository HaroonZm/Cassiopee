import sys

# 'sys'モジュールの'stdin'（標準入力）の'readline'を短縮名'input'として使う
input = sys.stdin.readline

# 非常に大きな数値を定数'INF'として定義する。DPなどで初期値として利用する。
INF = 10**13

def main():
    # まず、最初の入力を読み込み、整数Nとして集落の数を取得する
    N = int(input())

    # 集落ごとの情報(x座標, y座標, p)を2次元リストTに格納する
    # 入力はN回、各行につきx, y, pが空白区切りで与えられる
    # 例: T = [[x1, y1, p1], [x2, y2, p2], ...]
    T = [[int(i) for i in input().split()] for j in range(N)]

    # X_dist と Y_distは、それぞれbitmaskによる都市集合について各集落に対する評価距離を格納する2次元リスト
    # たとえば、X_dist[bit][i]はbitで示される集落集合に道を作ったときの集落iへのx距離コスト
    # '1 << N'は2のN乗。bitmaskで各都市が含まれるかを全探索できる
    X_dist = [[0]*N for _ in range(1 << N)]
    Y_dist = [[0]*N for _ in range(1 << N)]

    # 全ての道路集合（bitmask）の組み合わせについて
    for bit in range(1 << N):
        # 現在bitmaskに含まれる都市のx座標/ y座標リストを作成。最初は座標(0,0)に必ず道が接続されている前提
        cur_x = [0]
        cur_y = [0]

        # 各集落を走査
        for i in range(N):
            # bitmaskのiビット目が1なら、その集落を道路集合に含める
            if bit & (1 << i):
                # それぞれの座標をリストに追加
                cur_x.append(T[i][0])
                cur_y.append(T[i][1])

        # 各集落jについて処理
        for i, (x, y, p) in enumerate(T):
            # 集落iのx, y, p情報を取得
            # cur_x内どの道路からも辿れる。その中で最小のx距離を取得しp倍
            X_dist[bit][i] = p * min(abs(cx - x) for cx in cur_x)
            # cur_yについても同様。y軸方向で最小の距離*p
            Y_dist[bit][i] = p * min(abs(cy - y) for cy in cur_y)

    # 答えを格納するリスト。indexは建設した道路群の数(0,...,N)
    # 最小コストで初期化
    answer = [INF] * (N + 1)

    # 全ての道路群集合iについて全探索。iはbitmaskでどの都市に道路があるかを示す
    for i in range(1 << N):
        cnt = 0  # 道路群集合iに含まれる集落の数を数える変数
        for j in range(N):
            # ifでiのjビット目が1か判定。1ビットずつshiftして確認。
            if (i >> j) & 1:
                cnt += 1  # 1ビットごとにcntを+1

        # 集合iの部分集合jについて探索するための変数jをiで初期化
        j = i
        # jが0以上で繰り返す(すべての部分集合を生成)
        while j >= 0:
            # j &= iでjをiの部分集合になるよう更新。
            # 最初はj==i、次はiから1ビットずつ減らしていくイメージ
            j &= i

            cost = 0  # 今回の部分集合分割におけるコストを格納する変数

            # 各集落kについて
            for k in range(N):
                # if not ((i >> k) & 1)：
                # 集合iにkが含まれていなければ（道路が設置されていない集落）
                if not((i >> k) & 1):
                    # その集落へは、「部分集合jに対するx方向道路」または
                    # 「残り部分i-jに対するy方向道路」どちらかで行けるのでそのうちコストが小さい方を取る
                    cost += min(X_dist[j][k], Y_dist[i - j][k])

            # 集合iに含まれる集落数(cnt)における答えを更新。コストが小さい方を残す
            answer[cnt] = min(answer[cnt], cost)
            # jを1減らす（すべての部分集合を列挙）
            j -= 1

    # 0本からN本までの道路群ごとの最小コストを出力する
    for ans in answer:
        print(ans)

# スクリプトが直接実行された場合のみmain()を呼ぶ。モジュールとしてimportされた場合は実行されない
if __name__ == '__main__':
    main()