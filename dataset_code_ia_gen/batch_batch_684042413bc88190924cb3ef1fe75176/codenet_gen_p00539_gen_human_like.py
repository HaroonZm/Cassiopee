import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]

edges = []
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
    edges.append((a, b, d))

# 1からの最短距離をダイクストラ法で求める
INF = 10**15
dist = [INF] * (N + 1)
dist[1] = 0
hq = [(0, 1)]
while hq:
    cost, v = heapq.heappop(hq)
    if dist[v] < cost:
        continue
    for nv, nd in graph[v]:
        ndist = cost + nd
        if dist[nv] > ndist:
            dist[nv] = ndist
            heapq.heappush(hq, (ndist, nv))

# Xを決める探索を二分探索で行う方法もあるが、
# この問題はXが距離の範囲でなく、
# 経路の辺の長さ最大が10^5なので、
# 適切な方法は以下の通り。

# 与えられたXに対してコストを計算する関数を作る
def cost_with_x(X):
    # 地下道でつながる広場は dist[i] <= X の頂点群
    # 道のうち、地上に残すのはどちらかの頂点のdist > Xの場合に限る
    # よって残した道（修理コスト）は dist[a] > X or dist[b] > X の道の長さの和
    # 地下道コストは C * X
    sum_repair = 0
    for a, b, d in edges:
        if dist[a] > X or dist[b] > X:
            sum_repair += d
    return C * X + sum_repair

# Xの候補は dist[1..N]の中の一部の値に限定される
# distはXの関数なので、全てのdist[i]の値を使って試すのが良い
# さらに、Xは0以上なので候補は0も加える

candidate_values = list(set(dist[1:]))
candidate_values.append(0)
candidate_values = [x for x in candidate_values if x != INF]
candidate_values = list(set(candidate_values))
candidate_values.sort()

ans = float('inf')
for X in candidate_values:
    ans = min(ans, cost_with_x(X))

print(ans)