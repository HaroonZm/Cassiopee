from collections import deque

N, M, K = map(int, input().split())
dark_rooms = list(map(int, input().split()))
dark_set = set(dark_rooms)

# 入力の読み込み
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    edges = list(map(int, input().split()))
    graph[i] = edges

# 指示はa_iで、a_iは1~Kの範囲をとる
# A君はどの暗い部屋にいても明るい部屋にたどり着けるようにしなければならない
# 部屋の状態を状態集合(bitmask)で持ち、遷移を調べる

# bitの対応づけ：dark_roomsの位置がiのものがビットiに対応
def rooms_to_mask(rooms):
    mask = 0
    for r in rooms:
        idx = dark_rooms.index(r)
        mask |= 1 << idx
    return mask

# 初期状態：暗い部屋すべてが今いる部屋の候補
start_mask = (1 << M) - 1  # 全ての暗い部屋にA君がいる可能性があると考える

# 目的状態：今いる部屋の候補が空集合（すでに明るい部屋にいる）
goal_mask = 0

# BFSで探索
from collections import deque

# dist[state] = 最短手数
dist = [-1] * (1 << M)
prev = [None] * (1 << M)   # 前状態と指示を記録

dist[start_mask] = 0
queue = deque([start_mask])

while queue:
    state = queue.popleft()
    if state == goal_mask:
        break
    # 指示 a in [1..K]
    for a in range(1, K+1):
        next_state = 0
        # 各部屋にいるA君の候補ごとに移動先を計算
        for i in range(M):
            if (state >> i) & 1:
                cur_room = dark_rooms[i]
                nxt_room = graph[cur_room][a-1]
                # nxt_roomが暗い部屋ならビットを立てる
                if nxt_room in dark_set:
                    nxt_index = dark_rooms.index(nxt_room)
                    next_state |= 1 << nxt_index
                # 明るい部屋ならこの候補は除外(何もしない)
        if dist[next_state] == -1:
            dist[next_state] = dist[state] + 1
            prev[next_state] = (state, a)
            queue.append(next_state)

# 最短距離を出力
print(dist[0])