# 解法の要点:
# - 赤（Red）のパッケージを上から下へ、緑（Green）のパッケージを左から右へと攪拌装置に投入する。
# - 攪拌装置は上下方向（push_down）と左右方向（push_right）のベルトコンベアから成る十字構造で、
#   赤はpush_downの操作で、緑はpush_rightの操作で動く。
# - 操作は赤パッケージ数(push_downの回数)と緑パッケージ数+1(push_rightの回数)で構成され、
#   最初と最後の操作は必ずpush_right。
# - 入力として、赤パッケージ列、緑パッケージ列、下端（push_downで排出された順）のパッケージ列が与えられる。
# - これらから右端（push_rightで排出された順）のパッケージ列を推定する問題。

# 解決アプローチ:
# - push_downとpush_rightを、いわば２つの文字列(赤と緑)からの文字取り出し操作（それぞれ赤、緑の文字列の先頭から順）に対応させる。
# - 最終的にどの順番で操作があったかは分からないが、
#   初めの動作と最後の動作は必ずpush_rightで、またpush_downの回数は赤パッケージの数、push_rightの回数は緑パッケージの個数+1。
# - この問題は、有名な文字列のインターリーブ（文字列の合成）問題の変種と考えられ、
#   赤と緑の文字列をpush_down・push_rightの操作で混ぜて、一部（push_downで得られた下端のパッケージ列）が与えられた状況に合う右端のパッケージ列（緑によって反映される文字列）を推定するもの。
# - DPにより、赤(i), 緑(j)まで消費した時に下端(k)まで消費可能かを判定しながら、同時に右端に流れた文字を復元する。

def solve():
    import sys

    # 入力文字列は大文字・小文字の英字で、
    # 赤（red）・緑（green）・下端（bottom）をそれぞれ受け取る。
    input_lines = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == '-':
            break
        input_lines.append(line)

    # 3行ずつ1データセット
    for idx in range(0, len(input_lines), 3):
        red = input_lines[idx]
        green = input_lines[idx+1]
        bottom = input_lines[idx+2]

        R, G, B = len(red), len(green), len(bottom)

        # push_right回数 = G+1、push_down回数 = R
        # 操作の総数は R + G +1
        # 操作の順番は push_rightとpush_downが交互に混ざった順列で、
        # 初・終操作は必ず push_right。

        # dp[i][j] = True: 赤i個使い、緑j個使い、
        # それに対応するbottomの先頭i個がbottomのうちi文字と一致するか。
        # 実際はbottomの字数はRの数と同じなので、bottomの文字は赤のpush_down時に得られるものとする。
        # green推移は rightに送られるので別で記録する。

        # bottomのkは赤の取り出した数に対応し、iは赤の読み込み数、jは緑の読み込み数。
        # 赤のpush_downの数はi回目でbottomのk=i番目の文字を得ることになる。

        # DPでは、
        # 状態：(i,j) で赤i個、緑j個使った状態。
        # bottomの先頭i文字がredの取り出しで作れている。
        # 初期状態はdp[0][0] = True

        # 操作はpush_right (緑から1個取り出す j->j+1, bottom変わらず),
        # push_down (赤から1個取り出す i->i+1, bottomのi文字目と一致する必要あり)

        # 最初と最後の操作はpush_rightなので、dpはjから進むがj最大はG、
        # ただし最終的にj=G+1（push_rightがG+1回）

        # 上記を実装しつつ、経路の復元を行う

        from collections import deque

        dp = [[False]*(G+2) for _ in range(R+1)]
        # 前回の状態と操作履歴を記録(p_i, p_j, push_type)
        prev = [[None]*(G+2) for _ in range(R+1)]

        dp[0][0] = True

        # 操作数は R + G + 1
        # dp[i][j]は 赤i個、緑j個使った状態= 操作数 i+j
        # 操作0は push_right (j=1) のはず (初動)
        # 最終は i=R, j=G+1で終了

        for total_ops in range(R+G+1):
            for i in range(max(0, total_ops - (G+1)), min(R, total_ops)+1):
                j = total_ops - i
                if j < 0 or j > G+1:
                    continue
                if not dp[i][j]:
                    continue

                # 次の操作は push_down or push_right どちらか（制約に従う）
                # 操作の順序制約: 最初と最後はpush_right
                # total_ops == 0の時は始めの操作でpush_rightのみあり
                if total_ops == 0:
                    # 初回はpush_right必須
                    if j < G+1:
                        # greenから1文字取る push_right
                        if not dp[i][j+1]:
                            dp[i][j+1] = True
                            prev[i][j+1] = (i, j, 'R')
                    continue

                # 最終操作は全部でR+G+1回、0スタートなのでtotal_ops==R+Gは最後の操作
                if total_ops == R+G:
                    # 最後の操作もpush_right必須
                    if j < G+1:
                        if not dp[i][j+1]:
                            dp[i][j+1] = True
                            prev[i][j+1] = (i, j, 'R')
                    continue

                # それ以外は push_downかpush_rightどちらでもよい
                # push_down
                if i < R:
                    # 次のbottom文字は bottom[i]
                    if bottom[i] == red[i]:
                        # 赤i番目の文字をpush_downで消費しbottomに登場
                        if not dp[i+1][j]:
                            dp[i+1][j] = True
                            prev[i+1][j] = (i, j, 'D')

                # push_right
                if j < G+1 and j < G:
                    # j<Gなら green[j]取り出せる
                    if not dp[i][j+1]:
                        dp[i][j+1] = True
                        prev[i][j+1] = (i, j, 'R')

        # 最終状態は dp[R][G+1]が True でなければ矛盾
        if not dp[R][G+1]:
            # ありえないが保険として
            print("")
            continue

        # 復元
        i, j = R, G+1
        right_res = []

        while not (i == 0 and j == 0):
            pi, pj, op = prev[i][j]
            if op == 'R':
                # push_rightの操作はgreen[pj]を1つ取っている
                right_res.append(green[pj])
            elif op == 'D':
                # push_downの操作はbottomに出しただけなのでright_resには関係なし
                pass
            i, j = pi, pj

        # 右端は逆順に溜まっているので反転する
        print("".join(reversed(right_res)))

if __name__ == "__main__":
    solve()