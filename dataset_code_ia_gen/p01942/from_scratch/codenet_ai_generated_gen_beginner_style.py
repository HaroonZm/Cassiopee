import sys
input = sys.stdin.readline

H, W, T, Q = map(int, input().split())

# 状態を表すプレート用配列
# 0: 何もない
# 1: 焼き上がっていないたい焼き
# 2: 焼き上がったたい焼き
plate = [[0]*(W+1) for _ in range(H+1)]

# 焼き上がる予定時間を記憶するための配列
# 0ならたい焼きなし、0以外なら焼き上がる時刻
bake_time = [[0]*(W+1) for _ in range(H+1)]

# 次に焼き上がるたい焼きを時刻順に処理するためのリスト
# (焼き上がり時刻, h, w)
bake_list = []

# 焼き上がりを反映する際に使うポインタ
bake_idx = 0

events = []

for _ in range(Q):
    tmp = input().split()
    t = int(tmp[0])
    c = int(tmp[1])
    h1 = int(tmp[2])
    w1 = int(tmp[3])
    if c == 2:
        h2 = int(tmp[4])
        w2 = int(tmp[5])
        events.append((t, c, h1, w1, h2, w2))
    else:
        events.append((t, c, h1, w1))

# 焼き上がり処理をまとめて行う関数
def update_baked_until(time):
    global bake_idx
    while bake_idx < len(bake_list) and bake_list[bake_idx][0] <= time:
        bt, bh, bw = bake_list[bake_idx]
        # まだたい焼きが存在し焼き上がっていないなら焼き上がりに更新
        if plate[bh][bw] == 1 and bake_time[bh][bw] == bt:
            plate[bh][bw] = 2
        bake_idx += 1

# たい焼きをセットするイベントを処理しやすい形で先に処理するため、setイベントは後でbake_listにしてソートする
set_events = []
for e in events:
    if e[1] == 0:
        # (焼き上がり時刻, h, w)
        set_events.append((e[0]+T, e[2], e[3]))
set_events.sort()
bake_list = set_events

bake_idx = 0

for e in events:
    t = e[0]
    c = e[1]

    # まず現在時刻までの焼き上がりを反映
    update_baked_until(t)

    if c == 0:
        # たい焼きをセット
        h = e[2]
        w = e[3]
        if plate[h][w] == 0:
            plate[h][w] = 1
            bake_time[h][w] = t + T
    elif c == 1:
        # つまみ食い
        h = e[2]
        w = e[3]
        # 焼き上がったたい焼きがあれば無くす
        if plate[h][w] == 2:
            plate[h][w] = 0
            bake_time[h][w] = 0
    else:
        # カウント
        h1, w1, h2, w2 = e[2], e[3], e[4], e[5]
        baked_count = 0
        not_baked_count = 0
        for i in range(h1, h2+1):
            for j in range(w1, w2+1):
                if plate[i][j] == 2:
                    baked_count += 1
                elif plate[i][j] == 1:
                    not_baked_count += 1
        print(baked_count, not_baked_count)