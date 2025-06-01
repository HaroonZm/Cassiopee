# 解説：
# 鉄道は都市1から都市Nまで連続して繋がっているN-1本の線路で、
# 鉄道iは都市iと都市i+1を結んでいる。
# 旅行はM個の都市P1, P2, ..., PMを順番に訪問する。
# 各移動は鉄道を経由して都市PjからPj+1に移動する。
# 各鉄道の乗車には紙の切符料金AiまたはICカード料金Biがあり、
# ICカードは初回にカード購入費用Ciを払って買う必要がある。
# 既に買ったカードは何度でも使用可能。

# 目標：
# 旅行全行程の総費用（カード購入費＋乗車費用）を最小にする。

# アプローチ：
# 1. まず、どの鉄道が何回使われるかを数える。
#    - 移動は1日で複数の鉄道を乗り継ぐ形になるので、
#      PjからPj+1までの間に通る鉄道iを決めて
#      その線路の利用回数をカウント。
#    - 鉄道iは都市iと都市i+1を結ぶので、
#      区間の都市間の差を見て使われた鉄道路線を特定する。

# 2. 各鉄道iについて、
#    利用回数 = count_i
#    - 紙の切符で使う場合 => cost = Ai * count_i
#    - ICカードを買って使う場合 => cost = Ci + Bi * count_i
#    となる。

# 3. 鉄道ごとに上記コストを比較し、小さい方を選ぶ。

# 4. それらの鉄道のコストを合計し総費用を求める。

# 制約が大きいので（N,M最大10^5）、時間計算量はO(N + M)で行う必要がある。
# 都市間の区間利用回数数え方は差分配列を使う。

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))
A = [0]*(N-1)
B = [0]*(N-1)
C = [0]*(N-1)
for i in range(N-1):
    a,b,c = map(int, input().split())
    A[i] = a
    B[i] = b
    C[i] = c

# 鉄道iの利用回数をカウントするため差分配列を用いる
# 鉄道iは都市i～i+1間の線路なので、区間[x,y]の移動では、
# min(Pj,Pj+1)からmax(Pj,Pj+1)-1までの鉄道が使われる

usage = [0]*(N)  # 差分配列、N個でi番目は鉄道iの1つ前の境界を表す

for j in range(M-1):
    start = P[j]
    end = P[j+1]
    if start < end:
        # 増分区間に+1
        usage[start-1] += 1
        usage[end-1] -= 1
    else:
        # start > endなら逆方向に移動
        usage[end-1] += 1
        usage[start-1] -= 1

# prefix sumで差分配列を展開し、各鉄道の使用回数を求める
for i in range(1, N):
    usage[i] += usage[i-1]

# usage[i] は鉄道i+1の利用回数（0-indexedでi番目の鉄道）

total_cost = 0
for i in range(N-1):
    cnt = usage[i]
    if cnt == 0:
        continue
    # 紙の切符だけで支払ったら
    cost_ticket = A[i] * cnt
    # ICカードを買って使ったら
    cost_card = C[i] + B[i] * cnt
    total_cost += min(cost_ticket, cost_card)

print(total_cost)