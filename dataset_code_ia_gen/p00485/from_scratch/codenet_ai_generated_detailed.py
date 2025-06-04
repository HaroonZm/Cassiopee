import sys
import math
import heapq

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    # グラフは各ノードに接続する(隣接ノード, 辺の長さ)のリストで管理
    graph = [[] for _ in range(N+1)]
    edges = []
    for _ in range(M):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
        edges.append((a, b, l))
    malls = [int(input()) for _ in range(K)]

    # ショッピングモールからの最短距離を計算するために、
    # 複数スタートのDijkstraを実装する
    dist = [math.inf] * (N + 1)
    hq = []
    # ショッピングモールの町の距離を0に設定し、優先度付きキューに全て入れる
    for mall in malls:
        dist[mall] = 0
        heapq.heappush(hq, (0, mall))

    # Dijkstraアルゴリズム：複数のスタート地点からの最短距離計算
    while hq:
        cur_dist, u = heapq.heappop(hq)
        if dist[u] < cur_dist:
            continue
        for v, l in graph[u]:
            nd = cur_dist + l
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))

    # dist[i] は町iのショッピングモールまでの最短距離
    # 道路上の点は端点だけでなく途中の任意の点も考慮するため、
    # 各辺についても最短距離の差分から道路上のいちばん遠い点を考える
    # 辺 (a,b) 上の点をpとすると、pからの距離はdist[a] + x または dist[b] + (l - x) のどちらか小さい方
    # この最小値が最大になる点が答え
    ans = 0
    for a, b, l in edges:
        da = dist[a]
        db = dist[b]
        # 道路上の距離の最大値を求めるには、
        # 距離差の半分 + 小さい方の距離を足す
        # (ここは三角形の性質を利用)
        d1, d2 = da, db
        # 差の絶対値の半分
        diff = abs(d1 - d2) / 2
        # 小さいほうの距離にdiffを足した値が辺上の最遠点の距離
        cand = min(d1, d2) + diff
        if cand > ans:
            ans = cand

    # 求まった最大値を四捨五入して出力
    print(round(ans))

if __name__ == "__main__":
    main()