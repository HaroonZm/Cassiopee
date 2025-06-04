import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    # 入力された道路情報をグラフに保存
    for _ in range(M):
        A, B, D = map(int, input().split())
        graph[A].append((B, D))
        graph[B].append((A, D))

    # まず、広場1から各広場への最短距離をDijkstraで求める
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if dist[u] < d:
            continue
        for v, cost in graph[u]:
            nd = d + cost
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    # Xは0以上の整数で、1からの距離dist[i]がX以下ならその広場は地下道で繋がれる
    # コストは C * X + 道路補修コスト（撤去されなかった道路のみ）
    # 道路撤去されるのは、地下道で繋がれた広場間の道路全て
    # 地下道は地下道内広場はすべて相互に繋がっているので、地下道内の道路は全部撤去される。

    # 方針：
    # 1. Xを変化させてコストを最小化する。
    # 2. Xが大きくなると地下道で繋がれる範囲が広くなり、撤去される道路が増える
    # 3. Xが小さいと地下道工事費が安いが補修する道路が多い
    # 4. このトレードオフを最短距離に基づき計算する。
    #
    # Xの候補は dist の中にある値の集合（距離0も含む）、それ以外のXは意味がない（距離の間にXを置いても結果は同じ）
    # なので distの中の0を含む値集合を候補Xとする

    # 候補Xとして distに含まれるすべての距離(0含む)で試す
    dist_set = set(dist[1:])  # 0番使わないので1から
    dist_set.add(0)

    # 道路の補修コストは、地下道で結ばれた広場どうしの道を撤去するため、それ以外の道の長さの和
    # つまり全道路の長さの和から、
    # 広場間距離が両方とも<=Xの場合の道路長さの和を引く

    total_road_length = 0
    # 道路全体の長さ
    edges = []
    for u in range(1, N + 1):
        for v, d in graph[u]:
            if u < v:
                edges.append((u, v, d))
                total_road_length += d

    min_cost = float('inf')
    for X in dist_set:
        # X以下の距離の広場は地下道で結ばれ、間の道路は撤去される
        # つまり、その範囲にある道路の長さの合計を調べて引く
        # 両端の距離がX以下なら撤去範囲
        remove_length = 0
        for u, v, d in edges:
            if dist[u] <= X and dist[v] <= X:
                remove_length += d
        cost = C * X + (total_road_length - remove_length)
        if cost < min_cost:
            min_cost = cost

    print(min_cost)

if __name__ == '__main__':
    main()