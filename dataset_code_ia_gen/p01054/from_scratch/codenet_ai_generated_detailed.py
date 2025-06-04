# 解説：
# 問題の流れを整理すると、
# 1. ジェニファーがSの文字列を任意に並び替えられる → 文字の出現頻度だけ考慮すればよい
# 2. マリアンが2種類の文字を全量交換を任意回数可能 → 任意のアルファベットの置換（文字種の入れ替え）を表す
# 3. カーラが任意回数「1文字を別の1文字に置換」して最終的にTにする
# 
# ジェニファーとマリアンはカーラの置換回数を最小にしたい
#
# 考え方：
# - Sの文字を並び替えで自由に順序変更できるため、Sの文字種類と個数を元に考える
# - マリアンの操作は、同じ文字を別の文字に一括して置換すること。
#   複数回組み合わせることで、アルファベットのマッチング(1対1の文字の対応)を任意に変換可能。
# - よって、Sの文字からTの文字への文字種の対応付けを考えることになる。
# - 例えば、Sの文字集合をX、Tの文字集合をYとすると、Xの文字をYの文字に1対1で対応付ける（置換）
# - マリアンの置換は置換同士の交換なので、
#   置換は文字同士の等価な置き換えなので文字の対応関係は任意に設定可能。ただし、Sの文字種からTの文字種へのマッチングになる。
# - カーラの置換は「文字を別の文字に変換」なので、
#   実際に鮮明に文字がマッチしない場合はカーラの置換回数が増える。
#
# 以上より、この問題は以下の視点で捉えられる：
# - 文字の個数を考慮した上で、Sの文字集合をTの文字集合に1対1でマッチング（対応づけ）を対応付ける問題。
# - そのうえでカーラの置換回数は、マップに含まれない文字を置換しなければならない回数と等しい。
#
# 具体的には：
# - SとTの文字の頻度を算出
# - Sの文字集合(s_chars), Tの文字集合(t_chars)
# - s_charsの各文字をt_charsの各文字に割り当てる（マッチング）
# - 割り当てはすべてのマッチングのうち、対応付けで同じ文字個数を最大限合わせるようにする
# - つまり最大重みマッチング問題（最大重み二部マッチング）となる
#   - ノード1: Sに現れる文字
#   - ノード2: Tに現れる文字
#   - 辺の重み：Sの文字の個数とTの文字の個数のうち、小さい方（上限となるマッチング量）
# - 最大マッチング数を求め、それに相当する文字がマリアンの置換で対応付け可能。
# - 実際にカーラが置換せざるを得ない回数は n - 最大マッチング数 である。
#
# つまり、
# 答え = n - 最大重みの完全な文字対応マッチングの合計値
#
# 言い換えれば、文字種類間の最大対応数を二部マッチングで見つける問題になる。
#
# 注意：nは大きいがアルファベットは 'a'～'z' の26文字のみ。
# よって26x26 = 676辺の最大重み二部マッチングで十分に高速に処理可能。
#
# 最大重み二部マッチングアルゴリズム(Kuhn-Munkresアルゴリズム)で解く。
#
# ----------------------
# 入力例で確認：
# Sample Input 1:
# 3
# abc
# xyz
# S: {a:1, b:1, c:1}
# T: {x:1, y:1, z:1}
# 対応付けられる最大文字数 = 0 （文字集合が全く対応しないが重みは1ずつあるため1つ割り当てられそうに見えるが、アルファベットが違うが置換で自由に変換可能と考え、同じ出現数を最大マッチング数とするのは間違い。
# 実はマリアンの操作で文字種類の交換が可能のため文字種類は入れ替え可能 -つまり重みは個数のmin ＝ 1で条件満足
# →最大マッチングは３ => 答え 3-3=0
#
# Sample Input 2:
# 5
# aaabb
# xyxyz
# S: a:3, b:2
# T: x:3, y:2, z:1
# 重みは、例えばa→x 3、a→y 2、a→z 1
# b→x 3, b→y 2, b→z 1
# 最大マッチングは4（a→x 3 + b→y 1）、残りはカーラが置換
# 答えは 1
#
# よって最大重みマッチングで解く。

import sys
sys.setrecursionlimit(10**7)

def kuhn_munkres(weight):
    """
    Kuhn-Munkres Algorithm (Hungarian Algorithm) for maximum weight bipartite matching
    weight: 2D list of weights, size n x m (n <= m)
    Returns: (max_weight, matchR)
    matchR[j]: index i matched to j, or -1 if none
    """
    n = len(weight)
    m = len(weight[0])
    u = [0]*(n+1)
    v = [0]*(m+1)
    p = [0]*(m+1)
    way = [0]*(m+1)

    for i in range(1,n+1):
        p[0] = i
        j0 = 0
        minv = [float('inf')]*(m+1)
        used = [False]*(m+1)
        while True:
            used[j0] = True
            i0 = p[j0]
            j1 = 0
            delta = float('inf')
            for j in range(1,m+1):
                if not used[j]:
                    cur = u[i0] + v[j] - weight[i0-1][j-1]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m+1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        # augmenting path
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    matchR = [-1]*m
    for j in range(1,m+1):
        if p[j]!=0:
            matchR[j-1] = p[j]-1
    max_weight = -v[0]
    return max_weight, matchR


def main():
    n = int(input())
    S = input()
    T = input()

    # 文字a～z の頻度カウント
    freq_S = [0]*26
    freq_T = [0]*26
    for c in S:
        freq_S[ord(c)-ord('a')] +=1
    for c in T:
        freq_T[ord(c)-ord('a')] +=1

    s_chars = [i for i in range(26) if freq_S[i]>0]
    t_chars = [i for i in range(26) if freq_T[i]>0]

    # 2部グラフの重み行列を作成（行: Sの文字, 列: Tの文字）
    # 重みは freq_S[s] と freq_T[t] の min を入れる。
    weight = [[0]*len(t_chars) for _ in range(len(s_chars))]
    for i, s_ch in enumerate(s_chars):
        for j, t_ch in enumerate(t_chars):
            weight[i][j] = min(freq_S[s_ch], freq_T[t_ch])

    # 最大重みマッチングを実行
    max_match, matchR = kuhn_munkres(weight)

    # 答えは n - 最大マッチング値（カーラの置換回数最小）
    print(n - max_match)


if __name__ == "__main__":
    main()