import sys
import heapq

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, t = map(int, input().split())
        graph[x].append((y, t))
        graph[y].append((x, t))
    v0 = int(input())
    a, b, c = map(int, input().split())

    # 前処理: 速度の遷移を計算しておく（速度は mod c 内の0~c-1）
    # 速度は状態として扱う。j回目の移動後の速度 v_j は 
    # v_j = (a * v_{j-1} + b) mod c
    # 速度は最大 c=50 までなので状態数は小さい。
    # 各速度 v_j に対して次の速度を求めるテーブルを作る
    next_v = [0]*c
    for v in range(c):
        next_v[v] = (a*v + b) % c

    # ダイクストラで状態を(v, 頂点)の組み合わせで管理
    # dist[v][node]: 頂点node 到達時の速度vでの最小の体感距離和
    INF = 10**18
    dist = [[INF]*(n+1) for _ in range(c)]
    dist[v0][1] = 0
    # 優先度付きキュー (cost, v, node)
    pq = []
    heapq.heappush(pq, (0, v0, 1))

    # 最終的に求めたいのは、頂点1に戻るときの最小コスト（速度は不問）
    # つまり dist[v][1] の最小値を求める。

    while pq:
        cost, v, node = heapq.heappop(pq)
        if dist[v][node] < cost:
            continue
        # nodeが1でスタート地点かつcost>0なら終了できる経路になるため記録に使う
        # ただしここでは全探索続行し最後に最小を取る。

        for (nxt, t) in graph[node]:
            # この辺を速度vで通過すると体感距離は t * v
            moved_cost = t * v
            nv = next_v[v]  # 次の速度
            ncost = cost + moved_cost
            if dist[nv][nxt] > ncost:
                dist[nv][nxt] = ncost
                heapq.heappush(pq, (ncost, nv, nxt))

    # 頂点1に戻ってくるコストの最小値を求める
    ans = min(dist[v][1] for v in range(c))
    print(ans)

if __name__ == "__main__":
    main()