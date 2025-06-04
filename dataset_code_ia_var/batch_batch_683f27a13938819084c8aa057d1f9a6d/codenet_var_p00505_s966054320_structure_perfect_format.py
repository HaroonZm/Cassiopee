i, j, k, l = 0, 0, 0, 0

while True:
    # 引数:0 == AB, 1 == BC, 2 == CA と仮定
    listTRI = [int(val) for val in input().split()]
    sumList = sum(listTRI)
    # 三角形が不成立でbreak
    if min(listTRI) <= 0:
        break
    if sumList - max(listTRI) <= max(listTRI):
        break
    # 辺の最大値のインデックス取得
    maxIND = listTRI.index(max(listTRI))
    # 余弦定理を用いて、最大の辺の「対角のcos」を求める
    # 全ての辺の2乗の合計から一番長い辺の2乗を2回引く
    cos1 = sum(x ** 2 for x in listTRI) - 2 * (listTRI[maxIND] ** 2)
    # 全ての辺の2倍の合計から一番長い辺の2倍を引く
    cos2 = sumList * 2 - listTRI[maxIND] * 2
    # cos1とcos2を割った結果
    cosTRI = cos1 / cos2
    # cosTRIが正なら鋭角、0なら直角、負なら鈍角
    if cosTRI < 0:
        i += 1
        l += 1
    elif cosTRI > 0:
        i += 1
        k += 1
    else:
        i += 1
        j += 1

print(i, j, k, l)