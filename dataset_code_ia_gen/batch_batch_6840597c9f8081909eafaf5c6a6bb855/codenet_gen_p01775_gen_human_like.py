import sys
import heapq

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, v = heapq.heappop(hq)
        if dist[v] < cost:
            continue
        for nv, w in graph[v]:
            nd = cost + w
            if nd < dist[nv]:
                dist[nv] = nd
                heapq.heappush(hq, (nd, nv))
    return dist

def main():
    input = sys.stdin.readline
    n, m, k, p = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[x].append((y, w))
        graph[y].append((x, w))
    s = []
    t = []
    for _ in range(k):
        sj, tj = map(int, input().split())
        s.append(sj)
        t.append(tj)

    # キーとなる点集合: 出発点p, 郵便物の位置s_j, 配達先t_j
    key_points = [p] + s + t
    size = 1 + 2 * k  # p + k s + k t

    # それぞれのkey_pointsから他key_pointsへの最短距離を計算
    dist_matrix = [[float('inf')] * size for _ in range(size)]
    dists = []
    for i, point in enumerate(key_points):
        dist_i = dijkstra(point, graph, n)
        dists.append(dist_i)
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = dists[i][key_points[j]]

    # 状態: (bitmask 配達済み郵便物, bitmask 拾った郵便物) 現在位置番号
    # 配達済みbitをKbit目まで使い、拾った郵便物も同様にKbit目まで使う
    # 状態数: 2^k * 2^k * size, k<=6 なので約 64*64*13=53248 状態は許容範囲

    from collections import deque
    INF = float('inf')
    # dist[state_picked][state_delivered][pos] = 最小コスト
    dist_dp = [[[INF]*(size) for _ in range(1 << k)] for __ in range(1 << k)]
    dist_dp[0][0][0] = 0
    que = deque()
    que.append((0,0,0))

    while que:
        picked, delivered, pos = que.popleft()
        cur_cost = dist_dp[picked][delivered][pos]
        # 全郵便物配達済みなら終了
        if delivered == (1 << k) - 1:
            print(cur_cost)
            return
        # 現在位置がs_jで、まだ拾っていない郵便物を拾える
        for j in range(k):
            idx_s = 1 + j
            if not (picked & (1 << j)):  # 未拾得
                if pos == idx_s:
                    npicked = picked | (1 << j)
                    if dist_dp[npicked][delivered][pos] > cur_cost:
                        dist_dp[npicked][delivered][pos] = cur_cost
                        que.appendleft((npicked, delivered, pos))  # 同じ位置での操作は優先度高い
        # 現在位置がt_jで、対応する郵便物を拾っていてまだ配達していないなら配達可能
        for j in range(k):
            idx_t = 1 + k + j
            if pos == idx_t and (picked & (1 << j)) and not (delivered & (1 << j)):
                ndelivered = delivered | (1 << j)
                if dist_dp[picked][ndelivered][pos] > cur_cost:
                    dist_dp[picked][ndelivered][pos] = cur_cost
                    que.appendleft((picked, ndelivered, pos))
        # 他のkey pointへ移動
        for nxt in range(size):
            if nxt == pos:
                continue
            nd = cur_cost + dist_matrix[pos][nxt]
            if nd >= INF:
                continue
            if dist_dp[picked][delivered][nxt] > nd:
                dist_dp[picked][delivered][nxt] = nd
                que.append((picked, delivered, nxt))

    print("Cannot deliver")

if __name__ == "__main__":
    main()