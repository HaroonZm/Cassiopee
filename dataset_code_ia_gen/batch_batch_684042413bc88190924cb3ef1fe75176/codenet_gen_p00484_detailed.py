# JOI ブックストア問題の解法
# 問題概要:
# N 冊の本からちょうど K 冊を選び，各ジャンルごとにまとめて売る冊数 T に応じて買取価格が変動する。
# 同じジャンルの本をまとめて T 冊売ると、1 冊あたりの買取価格は基準価格より (T - 1) 円高くなる。
# つまりそのジャンルの本1冊1冊にはT-1円のプレミアムが上乗せされる。
# 合計買取価格を最大化する K 冊の選び方を求めよ。

# 解法の要点:
# - ジャンルごとに本を分類し、高価格順にソートする（高い本を集めるのが得）
# - 各ジャンルの先頭から t 冊選ぶ場合の買取価格の合計を計算する
#     - 買取価格 = (基準価格 + (t - 1)) * t = 基準価格の合計 + (t-1)*t
# - この合計を使って全ジャンルの t_j の組合せで合計冊数Kとなる最大値を動的計画法(DP)で求める

# 計算量：
# - 各ジャンルの冊数の最大は N=2000、ジャンルは最大10
# - DPはジャンルごとに冊数を選ぶため、最大でも10 * 2000 = 20000程度で可能

import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    
    # ジャンルごとの本: {ジャンル番号: [(基準価格), ...]}
    genres = {i: [] for i in range(1, 11)}
    for _ in range(N):
        c, g = map(int, input().split())
        genres[g].append(c)
    
    # 各ジャンルの基準価格を降順にソート
    for g in genres:
        genres[g].sort(reverse=True)
    
    # 各ジャンルの t 冊選ぶ場合の最大買取価格を計算（t=0の場合は0）
    # prefix_sums: 基準価格の累積和を事前計算
    prefix_sums = {}
    for g in genres:
        prefix = [0]
        for price in genres[g]:
            prefix.append(prefix[-1] + price)
        prefix_sums[g] = prefix
    
    # dp[i][j] := ジャンルiまで見て、合計でj冊選んだときの最大合計買取価格
    # ジャンル番号を1〜10とし、0は初期状態
    dp = [[-10**15] * (K+1) for _ in range(11)]
    dp[0][0] = 0
    
    for i in range(1, 11):
        books = genres[i]
        m = len(books)
        prefix = prefix_sums[i]
        for j in range(K+1):
            if dp[i-1][j] < 0:
                continue
            # t = 0(選ばない)からt冊まで選ばう(最大は min(m, K-j))
            max_t = min(m, K - j)
            for t in range(max_t+1):
                if t == 0:
                    # 選ばない場合、価格変動なし
                    value = dp[i-1][j]
                else:
                    # 選ぶ場合の買取価格
                    # (基準価格合計) + (t-1)*t を足す
                    base = prefix[t]
                    bonus = (t - 1) * t
                    value = dp[i-1][j] + base + bonus
                if value > dp[i][j+t]:
                    dp[i][j+t] = value
    
    print(dp[10][K])

if __name__ == '__main__':
    main()