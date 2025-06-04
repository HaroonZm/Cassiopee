import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 問題概要：
# 木が与えられたとき、各頂点から出発して全ての頂点を訪れるための最短ステップ数を求める。
# ここでの「最短ステップ数」とは、
# 頂点から出発し、すべての辺を少なくとも一度は通る（すべての頂点を訪れるために辺を行き来する）最短の移動距離。
#
# 解法の鍵：
# - 木の中で全ての辺を通るためには、基本的に片道だけでなく往復が必要な辺が多い。
# - 全辺を2回通ると考えれば、「総辺長の2倍」が初期評価となる。
# - しかし「出発点からはじめて全ての辺を通る最短のルート」は、
#   最も遠い2つの頂点間の距離（直径）を考慮することで算出できる。
#
# 公式：
#   各頂点から全頂点を訪れる最短ステップ数
#   = 2 * (N-1) - (その頂点から見た木の直径の長さ)
#
# 直径の長さの求め方：
# 1) 任意の頂点から一番遠い頂点を見つける（点A）
# 2) 点Aから一番遠い頂点を見つける（点B）
# 3) 点Aと点B間の距離が直径の長さ
#
# 今回は各頂点について出発点にした場合のステップ数を求める必要がある。
# だが直径の両端（点A,点B）の距離情報があれば、
# ある頂点xからの最短ステップ数は
# 2*(N-1) - max(dist(x,A), dist(x,B))　となる。
#
# これは、最短で全辺を通るには「直径の長さ」を一度重複して通らずに済む工夫ができるため。
#
# 実装手順：
# 1) 隣接リストでグラフ構築
# 2) 任意の点（ここでは1）から最も遠い点Aを BFS で探索
# 3) Aから最も遠い点Bを BFS で探索して距離配列を得る
# 4) Bからの距離配列も BFS で得る
# 5) 各頂点について max(dist_from_A[i], dist_from_B[i]) を計算し
#    2*(N-1) - max(...) を答えとして出力

from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 任意の点1から一番遠い点Aを見つける
    dist_from_1 = bfs(1, graph, n)
    A = dist_from_1.index(max(dist_from_1[1:]))

    # 点Aから一番遠い点Bを見つける
    dist_from_A = bfs(A, graph, n)
    B = dist_from_A.index(max(dist_from_A[1:]))

    # 点Bからの距離も求めておく
    dist_from_B = bfs(B, graph, n)

    # 全辺の数は n-1
    # 各頂点からスタートして全てを訪れる最短ステップ数は
    # 2*(n-1) - max(dist_from_A[i], dist_from_B[i])
    total = 2*(n-1)
    for i in range(1, n+1):
        print(total - max(dist_from_A[i], dist_from_B[i]))

if __name__ == "__main__":
    main()