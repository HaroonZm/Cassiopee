import sys
import collections
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    natsume_start, lennon_start = map(int, input().split())

    # グラフの隣接リスト（部屋ID: [(隣接部屋,扉種類), ...]）
    graph = [[] for _ in range(n + 1)]
    # 夏への扉は部屋0に繋がる扉が1つだけ存在する (0は特別な部屋番号)
    # 部屋0のノードを扱うため配列を(n+1)で確保し、0を部屋0として使用

    for _m in range(m):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        # cが'N'なら人間用扉、'L'ならねこ用扉
        graph[a].append((b, c))
        graph[b].append((a, c))

    # なつめ(N)が開けられる扉はコスト1で開けなければならず、それ以外は0。

    # なつめとレノンの両方が通れるか？
    # レノンはL扉は自分で開けて通れる（コスト0）
    # N扉はなつめが開けないと通れない（コスト1）

    # レノンの移動範囲を制限しつつ、
    # なつめが開ける扉の数の最小化を求める問題。

    # 解法：
    # なつめが扉を開けるのはN扉のみ。
    # L扉はねこが自分で通れるため、通行にコストはかからない。
    # なつめは開けてからはその扉を自由に通行可能。
    # 最終的にレノンが夏への扉0に辿り着けるように、
    # なつめが開けるN扉の最小数を求める。

    # これを扱うために、状態は「部屋の位置」のみ考えればよい。
    # なつめの役割はN扉を開けて道を作ること。
    # L扉はレノンだけが通れるからコスト0。
    # 0への最短経路のコストは、N扉を開ける数。

    # 実際には、レノンがL扉を自由に通れることにより、
    # 最短経路探索のコストは「N扉のみ1、それ以外は0」で良い。

    # そこで、ダイクストラでも良いが0-1 BFSで高速に解く。
    # コストは0か1だけであるため、dequeを使う。

    dist = [float('inf')] * (n + 1)
    dist[lennon_start] = 0
    dq = collections.deque()
    dq.append(lennon_start)

    while dq:
        current = dq.popleft()
        for nxt, door_type in graph[current]:
            cost = 1 if door_type == 'N' else 0
            nd = dist[current] + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                if cost == 1:
                    dq.append(nxt)
                else:
                    dq.appendleft(nxt)

    print(dist[0])