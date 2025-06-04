# 解説：
# 問題は、M問までの各問題に対して得点 S_i と、
# その問題を正解する可能性のある解答者が入力される。
# 最後の問題（M+1問目）の得点 S_{M+1} を決める際、
# 「だれが最後の問題を正解しても必ず優勝できる」ようにしたい。
#
# 「優勝」とは、「その解答者の合計得点が全員の中で最大かつその最大スコアを持つ人がただ1人」ということ。
# ただし、最後の問題はどの解答者でも正解可能。
#
# アプローチ：
# 各解答者について、M問目までの最大得点を計算するとする。
# これは、ある問題で解答者が正解可能ならその問題の得点を得られる可能性があるので、
# i問目の得点 S_i を解答者に加算し、解答者の最大得点を算出する。
#
# 最後の問題の得点 S_{M+1} を考えると、解答者 a が最後の問題で得点して優勝するためには、
# a の合計得点 + S_{M+1} > 他の解答者の合計得点（aを除く）である必要がある。
#
# したがって、各解答者aについて、
# S_{M+1} > (max_maxScore_excluding_a) - maxScore[a]
#
# を満たす必要がある。全ての a でこれを満たす最小の S_{M+1} を求めたい。
#
# ここで max_maxScore_excluding_a は、a以外の解答者の最大得点。
#
# 計算手順：
# 1. 各解答者の最大得点配列 maxScore を作る
# 2. maxScore の最大値と2番目の最大値を求める
# 3. 各解答者 a の S_{M+1} を計算する。a以外の最大値は、
#    maxScore の最大値が maxScore[a] と異なる場合は最大値。
#    そうでなければ2番目の最大値。
# 4. 全ての a について求めた値の最大値 + 1 が求める S_{M+1} の最小値。
#
# 注意点：
# - N 最大10000, M 最大1000, Σk_i 最大100000 と大きいので高速に処理する必要がある。
# - 各問題の得点は最大100なので、上記処理で問題なし。
#
# あとはこれをコードで実装。

import sys
import threading

def main():
    # 標準入力を読み込む
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        # 各解答者の最大得点を0で初期化
        maxScore = [0] * (N+1)  # 解答者は1〜Nのため、インデックス0は使わない

        # 各問題について、得点 S_i と 正解可能解答者を読み込む
        for _ in range(M):
            data = list(map(int, input().split()))
            S_i = data[0]   # 問題iの得点
            k_i = data[1]   # 正解可能解答者数
            c_list = data[2:]

            # 問題iを正解できる解答者は S_i の得点を得られる可能性があるので、その解答者の得点に加える
            for c in c_list:
                maxScore[c] += S_i

        # maxScore[0]は使わないので除外したリストを作る
        scores = maxScore[1:]

        # 最大値と2番目の最大値を求める
        max1 = -1
        max2 = -1
        for sc in scores:
            if sc > max1:
                max2 = max1
                max1 = sc
            elif sc > max2:
                max2 = sc

        # 各解答者aに対し、
        # a以外の最大得点を取得
        # それが M+1問目の点数を決める際の比較対象
        # S_{M+1} > (a以外の最大得点) - maxScore[a]
        # よって、S_{M+1} > diff となるdiffの最大値を求める
        maxDiff = -1
        for a in range(N):
            sc = scores[a]
            # aのスコアがmax1と異なるかどうかで比較対象を決定
            if sc != max1:
                otherMax = max1
            else:
                otherMax = max2
            diff = otherMax - sc
            if diff > maxDiff:
                maxDiff = diff

        # 最小のS_{M+1}は maxDiff + 1
        # 最大得点者の重複を避けるために1を足す
        print(maxDiff + 1)

threading.Thread(target=main).start()