import sys
import heapq
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    # 入力の読み込み
    N, M, K, S = map(int, input().split())  # 町数, 道路数, ゾンビ支配町数, 危険判定の距離制限
    P, Q = map(int, input().split())       # 安い宿の費用, 高級宿の費用
    zombies = [int(input()) for _ in range(K)]  # ゾンビ支配町のリスト

    # グラフの隣接リスト作成
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # ゾンビ支配の町から距離S以内の町を「危険な町」とする
    # ゾンビ支配町は訪問禁止なのでそこから距離0として、距離S以内の町を見つける
    dist = [-1]*(N+1)  # 各町のゾンビからの最短距離。-1は未訪問
    queue = deque()

    # ゾンビ支配町は距離0でキューに入れる
    for z in zombies:
        dist[z] = 0
        queue.append(z)

    # BFSで距離S以内の町を求める
    while queue:
        now = queue.popleft()
        if dist[now] == S:
            continue
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                queue.append(nxt)

    # 各町の宿泊費の定義
    # 町1と町Nでは宿泊しないので費用0とする
    # ゾンビ支配町は通行禁止なのでこれも考慮しておく（距離が0のところは支配町なので通れない）
    cost = [0]*(N+1)
    for i in range(2, N):
        if dist[i] != -1 and dist[i] <= S:
            # 危険な町：高級宿Q円
            cost[i] = Q
        else:
            # 危険でない町：安い宿P円
            cost[i] = P

    # ダイクストラ法で町1から町Nまでの最小宿泊費を求める
    INF = 10**15
    dp = [INF]*(N+1)
    dp[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        cur_cost, node = heapq.heappop(heap)
        if dp[node] < cur_cost:
            continue
        if node == N:
            # 目的地に到達したら最小費用が確定
            print(cur_cost)
            return
        for nxt in graph[node]:
            # ゾンビ支配町は通れないのでcostが0でないかつdistが0の状態は通行不可
            # 実際にcostで判別するよりはdist==0で判別
            if dist[nxt] == 0:
                continue  # ゾンビ支配町は通り抜け禁止

            nd = cur_cost + cost[nxt]  # 移動先での宿泊費加算
            if dp[nxt] > nd:
                dp[nxt] = nd
                heapq.heappush(heap, (nd, nxt))

if __name__ == "__main__":
    main()