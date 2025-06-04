# 入浴券とプール券の料金・使用枚数に基づき最安値を求める問題
# ポイントは「5枚以上の入浴券かつ2枚以上のプール券をまとめ買いすると
# すべての券が2割引になる」こと。また、「使う枚数より多く券を買ってもよい」
# というルール。使う枚数は最低限満たす必要がある。

def main():
    import sys

    input = sys.stdin.readline

    N = int(input())  # 日数

    for _ in range(N):
        x, y, b_use, p_use = map(int, input().split())
        # x: 入浴券料金, y: プール券料金
        # b_use: 使用する入浴券枚数, p_use: 使用するプール券枚数

        # 我々が買う枚数は、使う枚数以上。つまり
        # 入浴券は b_buy >= b_use
        # プール券は p_buy >= p_use
        # ただしb_buy, p_buyはそれぞれ0~6(使用枚数最大6)だが、+αで買うか検討
        # 問題文から多く買うことは可能で最大でも使用枚数は6なので6までを範囲として考えてよい。

        # それぞれ買う枚数の範囲は0～6（最大使用枚数）とする
        # ただし最小は使いたい枚数なのでb_buy≥b_use, p_buy≥p_use

        # b_buy: 入浴券買う枚数 (b_use ≤ b_buy ≤ 6)
        # p_buy: プール券買う枚数 (p_use ≤ p_buy ≤ 6)

        # 買う枚数の組合せを全探索し、割引条件を満たすか判定し最安値を求める

        INF = 10**9
        ans = INF

        for b_buy in range(b_use, 7):
            for p_buy in range(p_use, 7):
                if b_buy == 0 and p_buy == 0:
                    # どちらも0は使わない・買わないので料金0
                    total = 0
                    ans = min(ans, total)
                    continue

                # 割引判定
                # 入浴券5枚以上かつプール券2枚以上でまとめ買いすると割引
                if b_buy >= 5 and p_buy >= 2:
                    # 割引あり
                    total = int((b_buy * x + p_buy * y) * 0.8 + 0.5)  # 四捨五入
                else:
                    total = b_buy * x + p_buy * y

                ans = min(ans, total)

        print(ans)

if __name__ == "__main__":
    main()