import sys
sys.setrecursionlimit(10**7)

N, M, s, t = map(int, input().split())
d = list(map(int, input().split()))
magic = [tuple(map(int, input().split())) for _ in range(M)]

# グラフを作る
# 次元間の移動は
# i > j のとき自由に移動可能(追加コストなし)
# i < j のとき魔法による移動のみ可能
# そのため、各次元から移動可能な次元を保持するグラフを作る
# 魔法の移動は a_i -> b_i のみ
# 自由移動は i -> j (i > j)

# グラフの隣接リストを作る
# 辺のコストは行き先の次元の呪いのダメージを受ける場合がある
# ただし、次元呪いの仕様によって、より大きい次元の呪いを受けていれば
# より小さい次元の呪いは無効となる
# sは既に呪いを受けている次元なのでダメージは考えない
# 問題の複雑さのため、単純なDijkstraを使ってセルフカットのように動く。

from collections import defaultdict, deque

graph = defaultdict(list)
for i in range(1, N+1):
    # 自由にiより小さい次元へ移動可能 (i>j)
    for j in range(i-1, 0, -1):
        graph[i].append(j)
for a_i,b_i in magic:
    graph[a_i].append(b_i)

# ダメージの計算について
# 次元iに行くとd_iの呪いを受けるが、
# その後ずっと j < i の次元の呪いは受けない
# つまり現在持っている「一番大きい次元の呪い」より小さい次元に移動しても追加ダメージはなし
# 一番大きい次元の呪いを持っている状態を管理しながら移動する必要がある

# 状態: (現在の次元, 現在持っている最大の呪いの次元)
# この状態の費用はこれまで受けたダメージの合計

import heapq

INF = 10**15

# dist[(node, max_curse_dim)] = 最小ダメージ
# max_curse_dim=0の場合は呪い無しの状態だが初期状態はsで呪い済みなのでmax_curse_dim = s とする
dist = dict()
hq = []

# 初期状態: sにいて初期に呪いを受けているのでmax_curse_dim = s, ダメージ0
start_state = (s, s)
dist[start_state] = 0
heapq.heappush(hq, (0, s, s))  # (cost, node, max_curse_dim)

while hq:
    cost, node, max_curse = heapq.heappop(hq)
    if (node, max_curse) in dist and dist[(node, max_curse)] < cost:
        continue
    if node == t:
        print(cost)
        break
    for nxt in graph[node]:
        # 移動したときに受ける呪いを計算
        # 呪いは現在持っているmax_curseより大きい次元なら受ける
        # そうでなければ受けない
        new_max_curse = max_curse
        add_cost = 0
        if nxt > max_curse:
            new_max_curse = nxt
            add_cost = d[nxt-1]

        new_cost = cost + add_cost
        next_state = (nxt, new_max_curse)
        if next_state not in dist or dist[next_state] > new_cost:
            dist[next_state] = new_cost
            heapq.heappush(hq, (new_cost, nxt, new_max_curse))