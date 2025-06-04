import sys
import math
from collections import deque

def can_collect_all_crystals(n, hx, hy, dx, dy, crystals):
    # 勇者の初期位置
    start = (hx, hy)
    # 魔王の位置
    demon = (dx, dy)

    # 各地点のリスト(金銀銅: 勇者, クリスタル)
    points = [start] + crystals

    # n+1個の地点間の距離, 時間制限の判定用に距離の二乗で計算し、距離を浮動小数点で使う。
    dist = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist[i][j] = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 状態は(現在の地点のindex, 取得済みクリスタルのbitmask)
    # 始点は地点0（勇者の初期位置）で、まだ何も取っていない
    visited = [[False]*(1<<n) for _ in range(n+1)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True

    while queue:
        pos, mask = queue.popleft()
        x, y = points[pos]
        # すべてのクリスタルを取得したら成功
        if mask == (1<<n)-1:
            return "YES"
        for i in range(1, n+1):
            # すでに取ったクリスタルは除く
            if mask & (1<<(i-1)):
                continue
            # 現在の時刻は、これまでに取ったクリスタルを取得するまでに要した時間、または現在地までの移動が必要
            # 
            # 魔王からの距離制限の判定
            # 勇者は移動距離 = 次の場所までの距離dをかけた時間tのみ移動することが可能
            # 時間経過tはこれまでの移動距離（魔王からの距離= 時間より大きい）であるため、
            # 現在地の制限時間は、魔王からの距離-1 より少ない時間にその場所につかなければならない。

            # 移動距離
            d = dist[pos][i]

            # 魔王からの距離は行き先の地点で時間経過により1日あたり距離1で瘴気が広がるため、
            # 時間tにその地点の距離は必ず > t+1 でなければならない。
            # 勇者がその地点に到着するときの経過時間=既にかかった時間+ d (距離=時間)
            # つまり、勇者到着時刻tとなる距離について以下の制約:
            # 魔王からその地点までの距離 r > t (瘴気は境界線上不可)= 到着時刻t < r
            # 時間の初期値は0。
            # 現在地点posにおける到達時刻t_prev、そこから移動距離dだけかけて次の地点に到達時間はt_next = t_prev + d
            # だがt_prevは不明。厳密には最短時間問題。そこで探索は最短距離を前提に、順序にかかわらず最短距離での到達可能性チェックにする。

            # 各地点への最短到達時間の保持は状態遷移関数へ追加で保持しないといけないが、
            # 状態空間が増えるので、距離移動コストを使った状態付きDijkstraやBFSが必要。

            # ここではコーナーケースを考慮し、単純に経路を全探索し、制約を満たすか判定
      
    # しかし上記の議論で単純BFSでは実現困難なので、
    # 最短距離を計算しながら、経過時間経過に伴う距離の制約を満たすか判定していくアプローチを採用。

import heapq

def solve():
    for line in sys.stdin:
        if line.strip()=='':
            continue
        n,hx,hy,dx,dy = map(int,line.split())
        if n==0 and hx==0 and hy==0 and dx==0 and dy==0:
            break
        crystals = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
        # points: 勇者+クリスタル
        points = [(hx,hy)]+crystals
        # 各地点間距離
        dist = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                x1,y1=points[i]
                x2,y2=points[j]
                dist[i][j]=math.sqrt((x1-x2)**2+(y1-y2)**2)
        demon_dist = []
        for i in range(n+1):
            x,y=points[i]
            demon_dist.append(math.sqrt((x-dx)**2+(y-dy)**2))

        # ダイクストラで、状態は(現在地idx, 取得済みビットマスク), コストは時間経過 = 累積移動距離
        INF = float('inf')
        dp = [[INF]*(1<<n) for _ in range(n+1)]
        dp[0][0] = 0
        hq = []
        heapq.heappush(hq,(0,0,0))  # (時間, 位置, マスク)

        while hq:
            time,pos,mask = heapq.heappop(hq)
            if dp[pos][mask]<time:
                continue
            if mask==(1<<n)-1:
                print("YES")
                break
            for nxt in range(1,n+1):
                if mask & (1<<(nxt-1)):
                    continue
                t = time + dist[pos][nxt]
                # 到着時刻tに点nxtの魔王からの距離dはd > t, 境界線上は不可なので厳密に d > t
                if demon_dist[nxt] <= t:
                    continue
                # 移動時刻tに現在の位置も同じ条件であるが、現在は既にその位置にいるため条件クリア
                if dp[nxt][mask|(1<<(nxt-1))] > t:
                    dp[nxt][mask|(1<<(nxt-1))] = t
                    heapq.heappush(hq,(t,nxt,mask|(1<<(nxt-1))))
        else:
            print("NO")

if __name__=="__main__":
    solve()