while True:
    data = input().split()
    if len(data) < 6:
        break
    N, M, L, K, A, H = map(int, data)
    if N == 0 and M == 0 and L == 0 and K == 0 and A == 0 and H == 0:
        break

    freezer = []
    if L > 0:
        freezer = list(map(int, input().split()))
    freezer_set = set(freezer)
    freezer_set.add(A)
    freezer_set.add(H)

    roads = [[] for _ in range(N)]
    for _ in range(K):
        X, Y, T = map(int, input().split())
        roads[X].append((Y, T))
        roads[Y].append((X, T))

    # 状態は(町, 残りの冷凍可能時間)
    # 最短時間を管理する2D配列
    INF = 10**9
    dist = [[INF]*(M+1) for _ in range(N)]

    # 始点：A町、残り冷凍時間M、時間0
    from collections import deque
    q = deque()
    dist[A][M] = 0
    q.append((A, M))

    while q:
        town, time_left = q.popleft()
        current_time = dist[town][time_left]
        for nxt, cost in roads[town]:
            # cost分冷凍せずに移動すると残り時間が減る
            if cost > time_left:
                # 移動できない（血液が腐る）
                continue
            new_time_left = time_left - cost
            # もし次の町に冷凍施設があれば冷凍を行える
            if nxt in freezer_set:
                # 冷凍にかけられる時間はM - new_time_left分以内(1分冷凍で1分回復)
                # 血液の残り時間は最大Mになるように冷凍
                # 冷凍時間 = M - new_time_left
                freeze_time = M - new_time_left
                total_time = current_time + cost + freeze_time
                next_time_left = M
                if dist[nxt][next_time_left] > total_time:
                    dist[nxt][next_time_left] = total_time
                    q.append((nxt, next_time_left))
            else:
                # 冷凍できない時は何もしないで移動
                total_time = current_time + cost
                next_time_left = new_time_left
                if dist[nxt][next_time_left] > total_time:
                    dist[nxt][next_time_left] = total_time
                    q.append((nxt, next_time_left))

    ans = min(dist[H])
    if ans == INF:
        print("Help!")
    else:
        print(ans)