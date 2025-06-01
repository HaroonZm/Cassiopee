# 解法のポイント：
# - 矢を0～4本まで投げて得点合計を最大化する問題。
# - 合計がMを超すと得点は0になるため、Mを超えない最大の得点を求める必要がある。
# - N個の点数が与えられ、それぞれ何本でも使えるが合計本数は最大4本。
# - 使う矢は最大4本までなので、重複組合せの考え方で、0～4個の点数の和を計算する必要がある。
# - Nは最大1000、Mは大きいため、効率的に探索する必要がある。
#
# アプローチ：
# - 矢の本数は4本以下なので、全パターンを列挙してもそこまで爆発的ではない。（N^4 = 10^12は多いが、N=1000でそれは無理）
# - しかしN=1000だと4重ループは無理。
# - そこで、動的計画法（DP）を用いる：
#   dp[k] := 矢をk本投げたときに達成可能な得点の集合
# - 初期状態は dp[0] = {0}（矢を使わないとき得点0）
# - そこからdp[k] = 各p_iを1本追加してdp[k-1]に足す形で更新
# - 各段階でMを超える点数は破棄し、重複を避けるために集合を使う
# - kは0～4までで計算
#
# 最終的にdp[0]～dp[4]からM以下の最大値が答え
#
# 実装詳細：
# - setで管理するが計算量削減のため次のように変換
# - 各段階で集合に新たな得点を追加する操作は、集合のサイズ×Nになる
# - Nは最大1000なのでdpの各ステップのサイズは大きくなる可能性あり
# - しかし4回の繰り返しで済むため、工夫して高速化する
#
# 入力を複数読み込み、終了条件は N=0,M=0

import sys

def solve():
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        points = [int(input()) for _ in range(N)]

        # dp[k]: 矢をk本投げたときにとれる得点のset
        dp = [set() for _ in range(5)]
        dp[0].add(0)

        for k in range(1, 5):
            current = set()
            # dp[k-1]の各得点に対し、全てのpointsの点数を足して更新
            for s in dp[k-1]:
                for p in points:
                    val = s + p
                    if val <= M:
                        current.add(val)
            dp[k] = current

        # dpの中の最大値を求める
        ans = 0
        for k in range(5):
            if dp[k]:
                max_val = max(dp[k])
                if max_val > ans:
                    ans = max_val
        print(ans)

if __name__ == "__main__":
    solve()