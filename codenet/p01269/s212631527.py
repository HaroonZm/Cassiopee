from collections import defaultdict
import heapq

while True:
    N, M, L = map(int, input().split())
    if N==M==L==0:
        break
    E = defaultdict(lambda: defaultdict(lambda: float("inf")))
    for _ in range(M):
        A, B, D, E_ = map(int, input().split())
        E[A][B] = (D, E_)  # 金、コスト
        E[B][A] = (D, E_)  # 金、コスト

    start = (1, 0)

    dist = defaultdict(lambda: float("inf"))  # 始点から各頂点までの(仮の)最短距離を格納する
    dist[start] = 0
    q = []  # 各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
    heapq.heappush(q, (0, start))  # 始点をpush
    while len(q) != 0:
        prov_cost, v_m = heapq.heappop(q)  # pop  # 一度取り出された時点でコストは確定
        v, m_v = v_m

        # プライオリティキューに格納されている最短距離が
        # 現在計算できている最短距離より大きければ，distの更新をする必要はない
        if dist[v] < prov_cost:
            continue

        if v==N:
            print(prov_cost)
            break

        # 辺を探索
        Us = {}
        for u, (m, c) in E[v].items():
            Us[(u, m_v)] = c
            if m_v+m <= L:
                Us[(u, m_v+m)] = 0

        for u_m, c in Us.items():
            if dist[u_m] > dist[v_m] + c:
                dist[u_m] = dist[v_m] + c  # distの更新
                heapq.heappush(q, (dist[u_m], u_m))  # キューに新たな仮の距離の情報をpush