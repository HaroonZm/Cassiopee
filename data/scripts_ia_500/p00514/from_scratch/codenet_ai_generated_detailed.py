# 解説：
# この問題は「n種類の色の中から、それぞれの色を少なくともm個ずつ選び、合計でr個のビーズを選ぶ組合せの総数」を求める問題である。
# つまり、n種類の色のビーズの個数の組み合わせ (x1, x2, ..., xn) を考える。
# 条件は、
#   1) 各色の数 xi ≥ m
#   2) 合計 x1 + x2 + ... + xn = r
#
# これを別の形に変換する：
#   yi = xi - m とおくと、yi ≥ 0
#   よって y1 + y2 + ... + yn = r - n*m
#
# この問題は、非負整数の解 (y1,...,yn) の数を求める問題に変わる。
#
# 非負整数の解の数は組合せ計算で求めることができる：
#   「n個の非負整数の和がKである組合せの個数」 = C(K + n - 1, n - 1)
#
# ただし、r - n*m < 0 なら解なし（出力0）
#
# 入力で与えられる n, m, r は、0 <= m < n <= r <= 10000 である。
#
# 組合せ計算は大きくなる可能性があるため、
# Pythonの組み込み関数 math.comb を使用する。
#
# 入力を読み込み、計算して結果を出力するプログラムを以下に示す。

import sys
import math

def main():
    # 入力の読み込み
    line = sys.stdin.readline()
    if not line:
        print(0)
        return
    n_str, m_str, r_str = line.strip().split()
    n = int(n_str)
    m = int(m_str)
    r = int(r_str)

    # r - n*m が負なら条件を満たす組み合わせなし
    total = r - n * m
    if total < 0:
        print(0)
        return

    # 組み合わせの計算
    # n個の非負整数の和がtotalである組合せは C(total + n -1, n -1)
    ans = math.comb(total + n -1, n -1)
    print(ans)

if __name__ == "__main__":
    main()