import sys
import collections
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    # 入力受け取り
    N, K = map(int, input().split())
    # タクシー会社の運賃C[i]と連続最大距離R[i]
    C = [0] * (N+1)
    R = [0] * (N+1)
    for i in range(1, N+1):
        c, r = map(int, input().split())
        C[i] = c
        R[i] = r

    # グラフの隣接リスト（無向グラフ）
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 各町iについて、
    # 同じタクシー会社iのタクシーに乗ったときに
    # 乗車可能な町(距離R[i]以内)を求める必要がある。
    # 乗車可能な町jに行く場合、運賃はC[i]で固定。

    # 解法：
    # 「町iでタクシー会社iに乗車し距離R[i]以内の町へ行ける範囲」を事前にBFSで求める。
    # 各町iから到達可能な町のリストを作成し、その辺に対応するコストC[i]の有向辺を持つグラフを作る。
    # その後、町1から町Nまでの最小運賃をダイクストラで求める。

    # 事前計算のための隣接リスト（タクシーで移動可能なグラフ）
    taxi_graph = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        # iを起点にBFSをして距離R[i]以内の町を探索
        dist = [-1] * (N+1)
        dist[i] = 0
        queue = collections.deque([i])
        while queue:
            u = queue.popleft()
            if dist[u] == R[i]:
                continue
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        # distが0以上ならiのタクシーでuまで行ける
        for j in range(1, N+1):
            if 0 < dist[j] <= R[i]:
                # iのタクシーでi->jへ行ける経路がある
                taxi_graph[i].append(j)

    # ダイクストラで最小運賃を探索
    # dp[i] := 町iに着くための最小運賃
    dp = [float('inf')] * (N+1)
    dp[1] = 0
    heap = [(0, 1)]  # (運賃, 町番号)

    while heap:
        cost, u = heapq.heappop(heap)
        if dp[u] < cost:
            continue
        if u == N:
            # 目的地に到達したら終了できる
            break
        # uのタクシー会社の運賃C[u]で行ける町へ行く
        for v in taxi_graph[u]:
            # 新しいコストはcost + C[u] (uのタクシー代を払ってu->vへ)
            new_cost = cost + C[u]
            if dp[v] > new_cost:
                dp[v] = new_cost
                heapq.heappush(heap, (new_cost, v))

    print(dp[N])

if __name__ == "__main__":
    main()