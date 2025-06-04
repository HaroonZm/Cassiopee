import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 解法の概要:
# 1. 計画開始前の運賃はすべて1円なので、この状態で都市1から各都市への最短距離を求める(Dijkstra最短経路)。
#    これをdist_origとする。
# 2. 値上げ路線は毎年1つずつ増えていく。値上げ路線は運賃が2円になる。
# 3. しかし全経路を毎年再度DijkstraするのはQ*Mで大きすぎる。
# 4. ここでアンビルド（逆方向）Dijkstraを使うことにより、元の距離dist_origが最短距離の基準となる。
# 5. 任意の路線を2円に値上げすると、dist_origを使った距離に影響を与える可能性がある。
#    - 距離が伸びる都市は、値上げした路線を使っている最短経路を持つ都市。
# 6. 重要な観察：
#    - 最短距離を更新するのは値上げ路線に関係する都市。
#    - 各値上げ時点ですべての都市の不満度（dist_改定 > dist_orig）を求める必要は計算量的に困難。
# 7. よって、逆の時系列で計算する戦略をとる。
#    - 最終的に値上げられた全路線を2円にして最短距離dist_finalを算出する。
#    - そこから逆に値下げていく(2円から1円に戻す、つまり値上げ記録を逆順で戻す)。
#    - 逆に戻すごとにDijkstraをし、都市の最短距離を更新する。
# 8. 各年ごとに不満度の都市数を記録し、最後に逆順に出力する。
# 9. 実装上はdist_j[j]をdist_statesとして管理しないで、
#    逆に全値上げ路線が値上げ済み→1年目状態、
#    そこから路線を1本ずつ値下げして戻していくことで、
#    最後にdist_orig＝計画開始前の状態になる。
# 10. Qが大きいので、逆方向で動的にDijkstraで局所更新しながら進める方針をとる。

N,M,Q = map(int,input().split())
edges = []
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    edges.append((u,v))
    graph[u].append((v,i))  # iは路線番号（0-based）
    graph[v].append((u,i))

route_raise = []
for _ in range(Q):
    r = int(input())
    route_raise.append(r-1)  # 0-indexに直す

# 計画開始前の最短距離を計算
# 運賃は全1円なのでグラフは単純に辺重み1
dist_orig = [10**15]*(N+1)
dist_orig[1] = 0
queue = [(0,1)]
while queue:
    cd, v = heapq.heappop(queue)
    if dist_orig[v]<cd:
        continue
    for nv,_ in graph[v]:
        nd = cd+1
        if nd<dist_orig[nv]:
            dist_orig[nv] = nd
            heapq.heappush(queue,(nd,nv))

# 路線が値上げされるごとにその路線の重みが1→2になる

# 各辺に現在の重みを設定
# 最終的な状態(すべての値上げ路線が2円)の辺重みを設定
edge_cost = [1]*M
for r in route_raise:
    edge_cost[r] = 2

# 逆側（都市1）から最短距離を計算→dist_final（すべて値上げ済み）
dist = [10**15]*(N+1)
dist[1] = 0
hq = [(0,1)]
while hq:
    cd,v = heapq.heappop(hq)
    if dist[v]<cd:
        continue
    for nv,eid in graph[v]:
        nc = cd + edge_cost[eid]
        if nc<dist[nv]:
            dist[nv]=nc
            heapq.heappush(hq,(nc,nv))

# 年ごとに不満度がいくつか計算する
# 逆からのダイクストラでの値下げ処理を行い、その都度不満度を計算

# 結果格納
ans = [0]*Q

# 逆に値下げ処理するから、
# 今はQ年目の状態。1年目に戻るまで処理する。
# distはQ年目の距離情報
# dist_origは計画前の基準距離

# 都市kが不満= dist[k]> dist_orig[k]
# これはそのまま各年の不満都市のカウント

# 初期Q年目の不満都市数
cnt = 0
for i in range(2,N+1):
    if dist[i]>dist_orig[i]:
        cnt += 1
ans[Q-1] = cnt

# 値下げした路線を1に戻す時
# 路線を1円にすると重みが1減る→経路が最短経路になることがあるから、
# 距離の更新が必要。distを改善させる方向でupdate。

# 値下げした路線の周辺を緩和
# dist[v]への影響があるのは、dist[v]>dist[u]+edge_cost[eid]
# だから値下げした路線の両端の頂点から緩和開始。

for year in range(Q-1,0,-1):
    r = route_raise[year]
    # 値下げ路線rを重み1に変更
    edge_cost[r] = 1
    u,v = edges[r]

    # 値下げした路線の両端から距離更新を始めるキューを作る
    # dist[u], dist[v]が改善される可能性があるから両端から緩和
    hq = []
    for start in [u,v]:
        if dist[start]>dist_orig[start]:
            # 元から不満なら緩和の必要があるかもしれない
            heapq.heappush(hq,(dist[start],start))
        else:
            # 値下げすることで距離が縮まる可能性があるので距離しいて端点から緩和考える
            heapq.heappush(hq,(dist[start],start))

    while hq:
        cd, cur = heapq.heappop(hq)
        if dist[cur]<cd:
            continue
        for nxt,eid in graph[cur]:
            cost = edge_cost[eid]
            nd = dist[cur] + cost
            if dist[nxt]>nd:
                dist[nxt] = nd
                heapq.heappush(hq,(nd,nxt))

    # 更新後の不満都市数を集計
    cnt = 0
    for i in range(2,N+1):
        if dist[i]>dist_orig[i]:
            cnt += 1
    ans[year-1] = cnt

# 出力
print('\n'.join(map(str,ans)))