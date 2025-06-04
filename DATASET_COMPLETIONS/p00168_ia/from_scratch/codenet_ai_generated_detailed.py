# プログラムの説明:
# 入力として階段の段数n（1 <= n <= 30）が与えられ、nが0のとき入力終了。
# 階段の上り方は「1段、2段、3段で昇る組み合わせの総数」を求める問題。
# その総数のうち、一日に10種類の上り方を試すとして、
# 全ての上り方を試すのに必要な日数を計算し、
# 日数を365で割り切れるかどうかで年数を計算する。
# 出力は必要年数（整数）を1行に1つずつ。

def main():
    import sys

    MAX_STEPS = 30
    # dp[i] = i段の階段の上り方の総数（1,2,3段ずつ登る）
    dp = [0] * (MAX_STEPS + 1)
    # 初期条件
    # 0段目は1通り（何もしない）
    dp[0] = 1
    for i in range(1, MAX_STEPS + 1):
        dp[i] = dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        n = int(line)

        total_ways = dp[n]

        # 1日に10種類試すので必要日数を計算
        days = (total_ways + 9) // 10  # 切り上げ

        # 日数から年数計算　1年=365日
        years = (days + 364) // 365  # 日数が1でも1年とする切り上げ

        print(years)

if __name__ == "__main__":
    main()