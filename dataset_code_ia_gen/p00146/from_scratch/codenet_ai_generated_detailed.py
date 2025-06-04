import sys
import math
from functools import lru_cache

# 問題概要:
# 会津若松市の城から北に一直線に並ぶ蔵について、
# ルパン一行は蔵を順に訪れて中の千両箱を運び出す。
# 大介はどんな重さでも運べるが、重さが増すと速度が遅くなる。
# 速度は分速 2000 / (70 + w) メートルで、wは運搬重量(kg)。
# 蔵から蔵への移動は地下道で行い、距離は城からの距離の差の絶対値。
# 初めに最初の蔵に行き、越ェ門が破り、大介が箱を持ち運ぶ。
# その後、運搬中の箱を持ちながら次の蔵へ向かう。
# 箱は20kg/個なので 蔵iの箱の重さは 20 * v_i kg。
# 目的は最初の蔵を訪れたあとから全蔵を破り終えて最後の蔵まで移動する時間を最小化する順序を求めること。
# 入力は 蔵の数 n (≤15), 各蔵の番号 s_i, 距離 d_i, 箱数 v_i


# 入力を読み込み
n = int(sys.stdin.readline())
warehouses = []
for _ in range(n):
    s, d, v = map(int, sys.stdin.readline().split())
    warehouses.append((s, d, v))

# 箱の重さを計算する関数
# 千両箱1個=20kgなので総重量は20 * 箱の個数
def weight(box_count):
    return 20 * box_count

# 移動距離は通りに沿った距離の差 (地下道)
def dist(i, j):
    return abs(warehouses[i][1] - warehouses[j][1])

# 大介の移動速度は分速 2000/(70 + w)
# wは現在運んでいる箱の重さ (kg)
def speed(w):
    return 2000 / (70 + w)

# dp[state][last] := stateで表される蔵の集合を訪れた後、
# 最後にlastの蔵を訪れたときの最小移動時間(分)
# stateはbitmaskで蔵の訪問状態を表す(0~(2**n)-1)
# lastは最後に訪れた蔵のインデックス(0~n-1)

# 箱は持ったまま次に蔵へ移動するので、
# 運搬重量は今まで訪れた蔵の箱の合計重量。

# 備考：最初に訪れる蔵は固定なし。入力のどの蔵から始めても良いのか問題文に明示なしだが、
# 「最初の蔵に行く」の意味から、全てのスタート候補から最適解を探す。

# DPで全ルートを試すのはO(n^2 * 2^n)で n=15なら可能。

@lru_cache(None)
def dp(state, last):
    # stateとlastの条件は訪問済みの蔵の集合と最後に訪れた蔵
    # stateに含まれない蔵を訪問していく
    if state == (1 << n) - 1:
        # 全ての蔵を訪問したので終了
        return 0
    res = math.inf
    # 現在まで訪問した蔵の箱の重量合計（除lastは含む）
    total_box_count = 0
    for i in range(n):
        if (state >> i) & 1:
            total_box_count += warehouses[i][2]
    # lastの蔵で追加分は既に持っているのでtotal_box_countは今の運搬箱個数
    # 移動速度はtotal_box_count分の運搬重量で計算
    current_weight = weight(total_box_count)
    for nxt in range(n):
        if (state >> nxt) & 1:
            continue
        # nextに行く時間 = 距離 / 速度
        distance = dist(last, nxt)
        spd = speed(current_weight)
        time = distance / spd
        cost = time + dp(state | (1 << nxt), nxt)
        if cost < res:
            res = cost
    return res

# 最初の蔵に行く移動時間は
# ルパンの運転で先に行くが、
# 運搬速度の計算は破った後の大介の運搬時間なので
# 最初の蔵へは無負荷移動とみなし最初のステップを含めずに計算する

# なので実質のdpは最初の蔵を選んでそこから始めて残りを計算

# 最適解の経路復元用
@lru_cache(None)
def trace(state, last):
    if state == (1 << n) - 1:
        return [warehouses[last][0]]
    res = math.inf
    ans = None
    total_box_count = 0
    for i in range(n):
        if (state >> i) & 1:
            total_box_count += warehouses[i][2]
    current_weight = weight(total_box_count)
    for nxt in range(n):
        if (state >> nxt) & 1:
            continue
        distance = dist(last, nxt)
        spd = speed(current_weight)
        time = distance / spd
        cost = time + dp(state | (1 << nxt), nxt)
        if cost < res:
            res = cost
            ans = nxt
    return [warehouses[last][0]] + trace(state | (1 << ans), ans)

# 最初の蔵を選び、その後のルートをdpで決定し、
# 最小移動時間となる経路を出力

ans_time = math.inf
ans_route = None

for start in range(n):
    # start蔵を最初に選択、stateにstartを含める
    # ただし最初の蔵までのヘリ移動時間などは考慮しない（問題文の条件より）
    val = dp(1 << start, start)
    if val < ans_time:
        ans_time = val
        ans_route = [warehouses[start][0]] + trace(1 << start, start)[1:]

# 結果の蔵番号を空白区切りで出力
print(' '.join(map(str, ans_route)))