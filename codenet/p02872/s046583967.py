# にゃーん
# う　し　た　ぷ　に　き　あ　く　ん　笑
import sys
from random import randint
from numpy import argmin
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.buffer.readline

# 問題AとB両方同じコードだと嬉しいね
problem_b = True

V, E = map(int, input().split())

v_from = []
v_to = []
cost = []

for _ in range(E):
    u, v, d = map(int, input().split())
    v_from.append(u)
    v_to.append(v)
    cost.append(d)

graph = csr_matrix((cost, (v_from, v_to)), [V+1, V+1])
dist, predecessors = floyd_warshall(graph, directed=False, return_predecessors=True)
dist[dist == 0] = float('inf')

dist_min = list(map(argmin, dist))

# print(dist_min)

# print(dist, predecessors)
# 発生頻度？無視です……
if problem_b:
    input()

T_max = int(input())
# order = [[int(input().split()[1]) for _ in range(int(input()))] for _ in range(T_max)]

time = 0
delivering = False
returning = False
last_return_time = 0
distination = 1
v_next = 1

order = []
end_order = set()

def take_order():
    global order
    n = int(input())
    t = [int(input().split()[1]) for _ in range(n)]
    order.append(t)

    if problem_b:
        # 車に積まれた荷物の情報は捨てる(えー……)
        [input() for _ in range(int(input()))]

def time_next():
    global time, order
    time += 1
    # 時間を進めたらオーダーをとる
    if time < T_max:# - 1:
        take_order()

def print_flush(value):
    print(value, flush=True)

    if problem_b:
        # OKを読み飛ばす
        input()
        # 配達完了情報も読み飛ばします……
        [input() for _ in range(int(input()))]

# 最初オーダーだけとっておく
take_order()

while time < T_max:
    # 配達中なら配達作業
    if delivering:
        # 途中経由地へ進む
        print_flush(v_next)
        # 途中経由地までの残りの距離を減らす
        remaining_next -= 1
        # 到着したら次の途中経由地へ
        if remaining_next == 0:
            # 途中経由地がたまたま店であったら、最後に店に寄った時間を更新する
            # この処理入れるとスコアが悪くなるのでよくわからん
            # のでなんかこねこねしてみる
            if v_next == 1:
                last_return_time = max(last_return_time,  time - randint(0, 200))

            # 到着した途中経由地にたまたま配達できるかもしれないのでそういう集合
            end_order.add(v_next)
            next_temp = predecessors[distination, v_next]
            if next_temp != -9999:
                remaining_next = dist[v_next, next_temp]
                v_next = next_temp
        # 最終目的地までの距離を減らす
        remaining_last -= 1
        # 到着してる(はず)
        if remaining_last == 0:
            # 店に戻り終わった(目的地が店だった)
            if distination == 1:
                returning = False
                delivering = False
            # 店に戻らずに配達した方が良いこともある
            # 面倒くさいので一度戻り始めたら戻ってもらう方針
            elif not returning:
                # 今持ってるオーダーが戻るよりいい感じに運べるならそうする
                idx = jdx = -1
                dist_temp_min_possession = 10**18
                dist_temp_min_not_possession = 10**18
                for i, o in enumerate(order):
                    if not o:
                        continue
                    # 最後に店に寄った時間以前ならそのオーダーの荷物は持ってる
                    if i <= last_return_time:
                        for j, dst in enumerate(o):
                            # たまたま配達完了してる場合
                            if dst in end_order:
                                # 目的地を0にするとコストがinfになるのでいい感じにならない？
                                o[j] = 0
                            else:
                                # 現在地から配達場所までの時間
                                # Waiting time とかいうのがあるのでなんか重みを良い感じにする
                                # 重みを付けない方が良いスコアになるかも……
                                dist_temp = dist[v_next, dst] # + abs(time - i) ** 1
                                if dist_temp < dist_temp_min_possession:
                                    dist_temp_min_possession = dist_temp
                                    idx = i
                                    jdx = j
                    # まだ荷物を載せてないオーダー
                    # 実は考慮しない(今積んでる荷物を運びきる)方がスコアが高く？ -> なった気がする？
                    """
                    else:
                        for dst in o:
                            # 現在地から店 + 店から配達場所までの時間
                            # Waiting time とかいうのがあるのでなんか重みを良い感じにする
                            dist_temp = dist[v_next, 1] + dist[1, dst] + abs(time - i) ** 9
                            if dist_temp < dist_temp_min_not_possession:
                                dist_temp_min_not_possession = dist_temp
                    """
                # 配達完了情報をリセット
                end_order = set()

                if dist_temp_min_possession < dist_temp_min_not_possession:
                    # 目的地等を設定
                    distination = order[idx].pop(jdx)
                    remaining_last = dist[v_next, distination]
                    next_temp = predecessors[distination, v_next]
                    remaining_next = dist[v_next, next_temp]
                    v_next = next_temp
                # 店に戻る
                else:
                    returning = True
                    remaining_last = dist[distination, 1]
                    v_next = predecessors[1, distination]
                    remaining_next = dist[distination, v_next]
                    distination = 1
        time_next()
    # 配達する目的地を決める(一番近いところ)
    else:
        last_return_time = time
        idx = jdx = -1
        remaining_last = 0
        dist_temp_min = 10**18
        for i, o in enumerate(order):
            if not o:
                continue
            for j, dst in enumerate(o):
                # 店から配達場所までの時間
                # Waiting time とかいうのがあるのでなんか重みを良い感じにする
                dist_temp = dist[1, dst] + abs(time - i) ** 2
                if dist_temp < dist_temp_min:
                    dist_temp_min = dist_temp
                    idx = i
                    jdx = j
        # オーダーが無ければ何もせずに次の時間へ
        if idx == -1:
            print_flush(-1)
            time_next()
            continue
        # 目的地等を設定
        distination = order[idx].pop(jdx)
        remaining_last = dist[1, distination]
        v_next = predecessors[distination, 1]
        # print(distination, v_next)
        remaining_next = dist[1, v_next]
        delivering = True