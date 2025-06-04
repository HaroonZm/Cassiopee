import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# 規則１: 返信先が0のツイートを抽出
rule1 = set(i+1 for i, a in enumerate(A) if a == 0)

# 規則２: どのツイートからも返信されていない (返信先としてA_iに現れない)
replied = set(a for a in A if a != 0)
rule2 = set(range(1, N+1)) - replied

# 距離を求める配列。-1なら未訪問。規則３用。
dist = [-1]*(N+1)

from collections import deque

q = deque()
# 規則３の起点は規則２のツイート（返信されていないツイート）
for r2 in rule2:
    dist[r2] = 0
    q.append(r2)

# 規則３適用可能なツイートはdist[u] < K で辿れるもの。
# 返信元→返信先の辺しか情報がない。規則３は返信先を辿る方向ゆえ、
# 辿りたいのはiからA_iへのパスなので辿るのは返信先へ。ただしdistの初期化は規則２から。
# BFSでdistを更新するとき、i→A_iでしか進めないため、1辺逆方向のグラフにする必要ある。

# ここではdist[u]はuから返信先を辿った回数なので、各ツイートの返信先から逆にたどるのはできない。
# 返信先→返信元の逆辺グラフを作り、ここではdist[u]は「規則２のノードからuまでの距離」として保存。

rev_graph = [[] for _ in range(N+1)]
for i, a in enumerate(A, 1):
    if a != 0:
        rev_graph[a].append(i)

while q:
    u = q.popleft()
    if dist[u] == K - 1:
        continue
    for v in rev_graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

# dist[u] != -1 は規則３に該当
rule3 = set(i for i in range(1, N+1) if dist[i] != -1)

# 規則１、規則２、規則３を合成し重複なくカウント
result = len(rule1 | rule2 | rule3)
print(result)