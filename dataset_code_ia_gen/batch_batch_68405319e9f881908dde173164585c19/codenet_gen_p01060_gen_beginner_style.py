W, H = map(int, input().split())
N = int(input())
p = list(map(int, input().split()))

# コの字は2列で、外側がW人、縦にH人の形。実質的に外側列と内側列がある扱い。
# 外側の列を変数 outside、内側の列を inside として表現。
# 外側は横にW人並び、内側は横にW人並び、高さHは2列の長さとは別の情報と考え、
# 問題文では外側列と内側列として考える。ここでは外側列はリストの形で後ろから0番目まで外側W人、
# 内側列は同じくリストの形でH人いるが、コの字を単純化して以下のように解釈する。
# ただし問題文から直接的な座標情報は不明のため、問題の意図に従い単純に0(外側)と1(内側)二つの列と考える。

# 列はそれぞれの後ろに人が並ぶ形で、最初は二人はそれぞれの列の最後尾に隣同士でいる。

# 外側の人はW、内側もWとして扱い、二人はそれぞれ隣接している最後尾の位置で初期位置

# まず列の人数は定義し、外側列と内側列にそれぞれ人数分の人がいる。
# それぞれの列の最後尾にウニクロ卯月さん(U)と目黒凛さん(R)がいる。

# 配列は後ろから前に詰めていくイメージだが、本番問題の具体的座標は複雑なので、
# 位置管理は単純に配列の末尾から前に人がいると管理する。

# ここでは簡単のため、外側は0～W-1、内側も0～H-1の人がいる。
# うづきさんUは外側の最後尾(位置W-1)、りんさんRは内側の最後尾(位置H-1)
# とする。

# うづきさんUは0列に位置W-1、りんさんRは1列に位置H-1。

# 外側も内側も詰めるときは先頭がはけて残りの人が詰める。

# 二人ははけない。

outside_len = W
inside_len = H

# 位置はインデックスで管理。0が列の先頭、最後尾は位置outside_len -1 など。

U_line = 0
U_pos = outside_len -1
R_line = 1
R_pos = inside_len -1

count = 0

# 隣接判定関数
def are_neighbors(U_line, U_pos, R_line, R_pos):
    # 同じ列なら位置が差1なら隣
    if U_line == R_line:
        if abs(U_pos - R_pos) == 1:
            return True
        else:
            return False
    # 違う列の場合はコの字なので、縦と横のつながりがあるとき隣とする。
    # 問題文のコの字の形では差が１同士なら隣の判定になるのだが
    # ここでは簡単にして、末尾同士の間は隣にできない（黒色の角の状態は隣と見なさない）
    # したがって、U_posとR_posが同じ位置かまたは差が1で隣接列であれば隣とみなす。
    # ただし問題文の角（両方が先頭）はダメだが先頭は位置0であることを利用する。

    # 角は先頭(0)の位置にいるときは隣とカウントしない
    if (U_pos == 0 and R_pos == 0):
        return False

    # おおよそ隣だけど離れているときもFalseにするため、単純に隣接位置判定は以下
    # コの字はW, Hが大きいので重ねて接触点は1点、つまり位置が同じか1ずれ（縦横の差）なら隣とする

    if abs(U_pos - R_pos) == 1:
        return True
    if U_pos == R_pos:
        return True

    return False

# 初期の隣は数えないので、最初はカウントせずに判定もしない。

for i in range(N):
    if p[i] == 0:
        # 外側の先頭がはける
        # ただしUがはけることはないのでU_pos != 0なら先頭をはける
        if outside_len > 1:
            if U_line == 0 and U_pos == 0:
                # Uが先頭なのではけない
                pass
            else:
                # 先頭をはけて後ろを詰めるので、UかRの位置も調整
                outside_len -= 1
                if U_line == 0:
                    if U_pos > 0:
                        U_pos -= 1

                if R_line == 0:
                    if R_pos > 0:
                        R_pos -=1

        else:
            # 外側が一人だけならはけない
            pass
    else:
        # 内側の先頭がはける
        if inside_len > 1:
            if R_line == 1 and R_pos == 0:
                # Rが先頭なのではけない
                pass
            else:
                inside_len -=1
                if R_line == 1:
                    if R_pos > 0:
                        R_pos -=1

                if U_line == 1:
                    if U_pos >0:
                        U_pos -=1
        else:
            # 内側一人だけならはけない
            pass

    # はけた後の隣接判定。別々列の時も判定
    if are_neighbors(U_line, U_pos, R_line, R_pos):
        count += 1

print(count)