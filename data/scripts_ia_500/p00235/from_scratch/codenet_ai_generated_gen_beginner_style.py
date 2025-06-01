def dfs(current, visited, adj, total_time):
    if len(visited) == len(adj):
        return total_time
    times = []
    for nxt, time in adj[current]:
        if nxt not in visited:
            times.append(dfs(nxt, visited | {nxt}, adj, total_time + 2 * time))
    if times:
        return min(times)
    else:
        return total_time

while True:
    N = int(input())
    if N == 0:
        break
    adj = {i: [] for i in range(1, N+1)}
    for _ in range(N-1):
        a, b, t = map(int, input().split())
        adj[a].append((b, t))
        adj[b].append((a, t))
    # 総橋の重み合計
    sum_t = 0
    for edges in adj.values():
        for n, time in edges:
            sum_t += time
    sum_t //= 2  # 双方向なので半分にする

    # スタートは1で、全ての橋を爆破するための最小の時間 = 総移動距離の2倍 - 最も長い片道経路の距離
    # 初心者向けに単純に全探索で最長距離の橋を含む経路を見つける
    # ここでは何も考えず1からのパスを全探索し最小値計算
    res = dfs(1, {1}, adj, 0) - sum_t
    print(res)