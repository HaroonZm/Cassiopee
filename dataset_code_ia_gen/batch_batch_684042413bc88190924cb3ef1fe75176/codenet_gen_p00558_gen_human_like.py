import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
T = [int(input()) for _ in range(N)]

graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, D = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((B, D))
    graph[B].append((A, D))

# 状態：部屋番号, 最後に寒すぎる部屋を出てからの経過時間, 最後に暑すぎる部屋を出てからの経過時間
# 寒過ぎは t=0, 快適が t=1, 暑過ぎが t=2

INF = 10**15
# dist[node][cold_time][hot_time] はダイクストラ実装では大きすぎるので、
# 実際に記録するのは、状態を区別してベストな時間を持つ。
# ここでは last_temp は 0 から 2 の中で最後に冷たい(0) or 暑い(2) 部屋を出たか、快適(1)は制限なしなので2次元で表現。
# Xが最大200なのでX+1を状態として持つのが現実的。

# ここでは last_cold_time と last_hot_time の経過時間は0~Xの範囲内。
# ただし、快適な部屋は制限なしなので状態は reset 可能。

# 状態を以下のように定義:
#  last_state = 0: 最後は快適か、寒すぎ・暑すぎの時間に制限なし
#  last_state = 1: 最後に寒すぎの部屋を出てからn分経過
#  last_state = 2: 最後に暑すぎの部屋を出てからn分経過
# ただしX分未満での移動に制限があるので、最後に寒すぎを出てからx分, 最後に暑すぎを出てからx分を分けて管理はできるが、
# 本質的には最後に寒すぎか暑すぎか快適かで区別し、その経過分を刻んでDPを管理。

# 状態を (node, last_cold_time, last_hot_time) は状態爆発しすぎるので、
# 最後に"何を出たか"とその経過時間を管理する。
# ここでは状態 (node, last_type, elapsed) で管理する。
# last_type ∈ {0=快適, 1=寒すぎ, 2=暑すぎ}
# elapsed ∈ [0, X]
# elapsed は最後に寒すぎor暑すぎの部屋を出てからの経過時間。
# 快適な部屋を出た場合 elapsed = 0 にリセット。

max_time = X + 1
dist = [[[INF] * max_time for _ in range(3)] for _ in range(N)]

# 初期状態は部屋1にいて、部屋1は寒すぎなので last_type=1, elapsed=0
dist[0][1][0] = 0
queue = []
heapq.heappush(queue, (0, 0, 1, 0))  # (cost, node, last_type, elapsed)

while queue:
    cost, node, last_type, elapsed = heapq.heappop(queue)
    if dist[node][last_type][elapsed] < cost:
        continue
    if node == N - 1:
        print(cost)
        break

    for nxt, d in graph[node]:
        ctemp = T[nxt]  # 次の部屋の温度
        ncost = cost + d

        # elapsed をdだけ進める。制限はX分未満なのでelapsed+dがX超えると制限なし扱いにしてよい。
        nelapsed = min(elapsed + d, X)

        # 温度制約をチェック
        # 最後に寒い部屋を出て elapsed 分未満の間に暑い部屋には入れない
        if last_type == 1 and ctemp == 2 and elapsed + d < X:
            continue
        # 最後に暑い部屋を出て elapsed 分未満の間に寒い部屋には入れない
        if last_type == 2 and ctemp == 1 and elapsed + d < X:
            # ただしctemp==1は快適(1)なのでOK? 問題文によれば快適は制限なし
            # ここは間違い。制限は寒すぎ<->暑すぎ間の移動のみ。
            pass
        if last_type == 2 and ctemp == 0 and elapsed + d < X:
            continue
        # 快適(1)は制限なし

        # next_stateの設定
        # 新しいlast_typeとelapsedを決定
        if ctemp == 1:
            # 快適に移動した場合、elapsedは0にリセット、last_typeは快適(0)
            nlast_type = 0
            nelapsed = 0
        elif ctemp == 0:
            # 寒すぎの部屋に入った場合 last_type=1 elapsed=0
            nlast_type = 1
            nelapsed = 0
        else:
            # 暑すぎの部屋に入った場合 last_type=2 elapsed=0
            nlast_type = 2
            nelapsed = 0

        if dist[nxt][nlast_type][nelapsed] > ncost:
            dist[nxt][nlast_type][nelapsed] = ncost
            heapq.heappush(queue, (ncost, nxt, nlast_type, nelapsed))