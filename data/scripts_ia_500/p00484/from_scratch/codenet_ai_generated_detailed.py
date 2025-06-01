import sys

def main():
    input = sys.stdin.readline
    # 入力値の読み込み
    N, K = map(int, input().split())
    books = [tuple(map(int, input().split())) for _ in range(N)]

    # ジャンルごとに基準価格を降順にソートして格納
    genres = [[] for _ in range(11)]
    for c, g in books:
        genres[g].append(c)
    for g in range(1, 11):
        genres[g].sort(reverse=True)

    # dp[g][k] := ジャンル1～g番までを使ってk冊売ったときの最大価値
    # ジャンルgを使わない場合もあるので初期値は非常に小さい値で初期化
    dp = [[-10**15] * (K + 1) for _ in range(11)]
    dp[0][0] = 0

    for g in range(1, 11):
        prefix_sum = [0]
        # 累積和を計算（まとめてt冊売ったときの基準価格の合計）
        for price in genres[g]:
            prefix_sum.append(prefix_sum[-1] + price)

        # ジャンルgについてt冊売る場合の価値を計算
        # t冊まとめて売ると一冊あたりt-1円上乗せがある
        # 合計買取価格 = 基準価格の合計 + t * (t-1)
        max_t = min(len(genres[g]), K)  # そのジャンルで売る最大冊数はK冊まで
        for k in range(K + 1):
            if dp[g - 1][k] < 0:
                # そもそもこの枚数は達成できていない
                continue
            # ジャンルgを何冊売るか決める t冊 (0冊もあり得る)
            for t in range(max_t + 1):
                if k + t > K:
                    break
                value = dp[g - 1][k] + prefix_sum[t] + t * (t - 1)
                if value > dp[g][k + t]:
                    dp[g][k + t] = value

    # K冊売る最大値が答え
    print(dp[10][K])

if __name__ == "__main__":
    main()