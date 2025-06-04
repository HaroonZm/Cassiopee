import sys
import heapq
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N, R = map(int, input().split())
    
    # グラフを隣接リストで表現（各頂点: [(隣接頂点, 重み), ...]）
    graph = [[] for _ in range(N + 1)]
    for _ in range(R):
        s, t, d = map(int, input().split())
        graph[s].append((t, d))
        graph[t].append((s, d))
    
    # 各町間の最短経路距離を求めるために、ダイクストラ法を使う
    # しかしN=1500なので、全頂点ペアのダイクストラは500万回近い計算になり非現実的
    # 解決策として、全頂点からその頂点までの距離を一括で求めるフロイド・ワーシャルはO(N^3)で厳しい
    # 代わりに「直径の端点」のみを求める
    # アイデア：
    # 任意の頂点から最遠の頂点をdijkstraで探し、その頂点からまた最遠の頂点を探すことで、グラフの直径に近い距離を求める
    # この2点間がスタートゴールの候補
    # それらの２点間の最短経路上にある町は「駅伝コースに使われる可能性がある」
    # それ以外は使われない
    #
    # 問題文の「すべての町の組み合わせについて、最短経路の距離を求め」→直径(最長最短距離)を求める意味
    
    # ダイクストラ関数: 開始点startからの最短距離と経路復元用の親を返す
    def dijkstra(start):
        dist = [float('inf')] * (N + 1)
        dist[start] = 0
        parent = [-1] * (N + 1)  # 経路復元用
        hq = [(0, start)]  # (距離, 頂点)
        while hq:
            cost, u = heapq.heappop(hq)
            if dist[u] < cost:
                continue
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    parent[v] = u
                    heapq.heappush(hq, (new_cost, v))
        return dist, parent
    
    # 1. 任意の頂点（ここでは1）から最遠点を求める
    dist_from_1, _ = dijkstra(1)
    max_dist = -1
    max_node = -1
    for i in range(1, N + 1):
        if dist_from_1[i] != float('inf') and dist_from_1[i] > max_dist:
            max_dist = dist_from_1[i]
            max_node = i
    
    # 2. その最遠点から再度最遠点を求める(直径の端点候補)
    dist_from_max, parent = dijkstra(max_node)
    max_dist_2 = -1
    max_node_2 = -1
    for i in range(1, N + 1):
        if dist_from_max[i] != float('inf') and dist_from_max[i] > max_dist_2:
            max_dist_2 = dist_from_max[i]
            max_node_2 = i
    
    # max_node と max_node_2 がスタートとゴール
    # その最短経路を復元し、経路上の町をすべて「駅伝コースに使われる可能性がある町」とマークする
    used = [False] * (N + 1)
    current = max_node_2
    while current != -1:
        used[current] = True
        current = parent[current]
    
    # 使われない町を集める
    not_used = []
    for i in range(1, N + 1):
        if not used[i]:
            not_used.append(i)
    
    # 結果出力
    print(len(not_used))
    for town in sorted(not_used):
        print(town)

if __name__ == "__main__":
    main()