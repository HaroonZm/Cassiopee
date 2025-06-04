# 解説:
# この問題は、複数種類のカードがあり、それぞれのカードに書かれた数値と枚数が与えられます。
# 各ゲームで参加者が宣言した数 n に対して、袋の中から複数のカードを選び、そのカードの総和が n になる組み合わせ数を求めます。
# 同じカードは複数枚あるため、同一種類のカードを最大 b_i 枚まで選ぶことができます。
# また、各ゲーム終了後、カードは袋に戻されるので、それぞれ独立した計算になります。

# アプローチ:
# DP（動的計画法）を用いて解きます。
# dp[i][j]: i種類目までのカードを使って合計をjにする組み合わせ数
# 初期状態 dp[0][0] = 1（カードを何も選ばずに合計0を作る方法は1通り）
# i種類目のカードについて、0枚から最大 b_i 枚まで使った場合のdpテーブルを更新する。
# ただし、計算量を減らすために「多重集合」状況での組み合わせ問題を効率的に処理します。

# 実装上の工夫:
# - 入力が複数のデータセットで終了は0行のみで判別
# - 各ゲームで複数の目標sum n_iがあるため、１つのデータセット内で一度dp配列を作っておけば
#   各ゲームのn_iに対応した結果をすぐに出力できる

import sys

def main():
    input = sys.stdin.readline

    while True:
        m_line = input()
        if not m_line:
            break
        m_line = m_line.strip()
        if m_line == '0':  # 入力の終了判定
            break
        m = int(m_line)
        cards = []
        for _ in range(m):
            a, b = map(int, input().split())
            cards.append((a, b))

        g = int(input())
        targets = []
        max_n = 0
        for _ in range(g):
            n = int(input())
            targets.append(n)
            if n > max_n:
                max_n = n

        # dp[j]: 合計jを作る組み合わせ数（i種類目まで処理した後）
        dp = [0] * (max_n + 1)
        dp[0] = 1  # 0を作る1通り

        # 各カードについて、多重集合対応のDP更新を行う
        for (value, count) in cards:
            # 新しいカードを追加した後のdpをtmpに作成
            tmp = [0] * (max_n + 1)
            for j in range(max_n + 1):
                if dp[j] == 0:
                    continue
                # k枚使う場合のループ k=0～count
                # 合計が超えない範囲で足す
                for k in range(count + 1):
                    nj = j + value * k
                    if nj > max_n:
                        break
                    tmp[nj] += dp[j]
            dp = tmp

        # dpに全カードを使った場合の全合計の組み合わせ数が入っているので、
        # ゲームごとに結果を出力
        for n in targets:
            print(dp[n])

if __name__ == "__main__":
    main()