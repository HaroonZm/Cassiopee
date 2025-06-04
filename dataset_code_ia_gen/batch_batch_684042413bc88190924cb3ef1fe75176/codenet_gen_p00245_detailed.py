# LL堂のタイムセールシミュレーション問題の解法

from collections import deque
import sys

sys.setrecursionlimit(10**7)

def main():
    while True:
        # 入力取得
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        X, Y = map(int, line.strip().split())
        if X == 0 and Y == 0:
            break

        # 店内マップを格納
        # 入力はY行、各行にX要素だが問題文の入力例を見ると、X行Y列の形式で与えられているので注意
        # 問題文の例では6 5 → X=6,Y=5 のとき6行5列の入力となっている
        # 入力例:
        # 6 5
        # 1 1 . 0 0 4
        # 1 . . . . .
        # . . 2 2 . .
        # . . 2 2 3 3
        # P . . . . .
        #
        # ここで、m_i,j の i=1~X (列?), j=1~Y(行?)
        # よってm_1,1...m_X,1(最上段)、続いて m_1,2...m_X,2 ...
        # つまり各行にX個の要素がある。なのでX列Y行のグリッドと考え、
        # 入力はY行、1行にXの要素があると読む
        grid = []
        px = py = -1
        for _ in range(Y):
            row = sys.stdin.readline().strip().split()
            grid.append(row)

        # Pの位置を特定
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 'P':
                    px, py = x, y
                    grid[y][x] = '.'  # Pは通路として扱う

        n = int(sys.stdin.readline())

        # 商品ごとのタイムセール情報を辞書で保持
        # key=商品番号 g, value=(値引き額d, 開始時刻s, 終了時刻e)
        time_sales = {}
        for _ in range(n):
            g, d, s, e = sys.stdin.readline().split()
            g = int(g)
            d = int(d)
            s = int(s)
            e = int(e)
            time_sales[g] = (d, s, e)

        # 店内には商品棚がおり、その数字が商品番号。通路は'.'
        # 通路しか移動できず、商品棚のマスには移動できない。
        # ただし商品を取るときは、その商品棚の上下左右4方向の通路マスで時間制約を満たせば取れる。

        # まず、各マスから上下左右に移動可能な通路マスのグラフと考え、
        # 移動可能なマスは通路マスのみ。

        # 目標は、単一人物が初期位置(px,py)0時から移動し、
        # それぞれの商品はそれぞれのタイムセール期間(s<=t<e)内に、
        # 商品棚の隣接通路マスで商品を「とる」こと（移動時間tがその範囲内）を行えること。
        # ひとつの商品は一度だけ取れる。

        # 解法の流れ：
        # 1. 商品棚マスごとに、その商品棚に隣接する通路マスリストを作成
        # 2. 各通路マス間の最短距離を求める（BFS）
        # 3. 開始位置から各商品の隣接通路マスへの最短距離を求める
        # 4. 各商品間の移動距離（商品Aの隣接マスから商品Bの隣接マスへの最短距離）も計算する
        # 5. bit DPで商品購入の順序を探索し、時間制約(s,e)を考慮して最大割引額の合計を計算

        # 詳細実装：

        # 通路マスの座標を取得
        passages = []
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == '.':
                    passages.append( (x,y) )

        # 商品棚マスの辞書商品番号->(x,y)のリスト
        product_shelves = {}
        for y in range(Y):
            for x in range(X):
                c = grid[y][x]
                if c.isdigit():
                    g = int(c)
                    if g not in product_shelves:
                        product_shelves[g] = []
                    product_shelves[g].append( (x,y) )

        # 商品番号0~9の中でもタイムセール情報がある商品のみ対象とする
        sale_products = list(time_sales.keys())  # 探索対象の商品のリスト

        # ある商品棚マスの上下左右の通路マスを取得
        def get_adjacent_passages(x,y):
            adj = []
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < X and 0 <= ny < Y:
                    if grid[ny][nx] == '.':
                        adj.append((nx,ny))
            return adj

        # 商品ごとに隣接する通路マスの集合(複数棚があれば全部の隣接通路マスを集める)
        product_adj_passages = {}
        for g in sale_products:
            adj_list = []
            for (x,y) in product_shelves.get(g, []):
                adj_list.extend(get_adjacent_passages(x,y))
            # 重複削除
            adj_set = list(set(adj_list))
            product_adj_passages[g] = adj_set

        # 通路マスのみのグリッドで距離を計算するため、通路マスを頂点としたグラフを作成
        # ここでは座標同士の距離は1辺の重み1のグラフでBFSで計算できる

        # BFSでstart(通路マス座標)から全通路マスへの距離を計算する汎用関数
        def bfs(start_x, start_y):
            dist = [[-1]*X for _ in range(Y)]
            dist[start_y][start_x] = 0
            queue = deque( [(start_x,start_y)] )
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < X and 0 <= ny < Y:
                        if dist[ny][nx] == -1 and grid[ny][nx] == '.':
                            dist[ny][nx] = dist[y][x] + 1
                            queue.append((nx,ny))
            return dist

        # 開始点(px,py)から各商品の隣接通路マスまでの最短距離を計算
        dist_start = bfs(px, py)

        # 各商品間の移動距離を計算するために、各商品の隣接通路マスの代表点を準備
        # 商品の隣接通路マスが複数ある場合、最短距離を計算する際には最短のものを選ぶ
        # なので商品の隣接通路マス集合を使い、距離の最小値を評価する

        # 各商品の隣接通路マスの距離テーブル(各通路マスからの距離)
        # すべての通路マスを起点に距離を計算するのはコストが高いので、
        # 必要な商品同士の距離だけを計算する。

        # まず、各商品の隣接通路マスからBFSして距離を計算し、
        # 他商品の隣接通路マスへの最短距離を求める

        # 商品の数 <= 8 なので8x8の距離行列を作成

        # 商品を番号付きリストに変換
        product_list = sale_products
        m = len(product_list)
        # 商品番号からindexマッピング
        product_idx = {g:i for i,g in enumerate(product_list)}

        # 各商品の隣接通路マス集合を使い、
        # start_dist[i] = startからi番目の商品棚の隣接通路マスまでの最短距離(最小)
        start_dist = [10**9]*m
        for i,g in enumerate(product_list):
            adjs = product_adj_passages.get(g, [])
            mind = 10**9
            for (ax,ay) in adjs:
                d = dist_start[ay][ax]
                if d != -1 and d < mind:
                    mind = d
            start_dist[i] = mind

        # 各商品iの隣接通路マスからの距離マップを計算し、
        # 他商品jの隣接通路マスまでの最短距離を求める
        # dist_matrix[i][j] = 商品iから商品jへの最小距離（隣接通路マス間）
        dist_matrix = [[10**9]*m for _ in range(m)]

        # BFSでi番目商品の隣接通路マス群を始点に距離を計算
        # 商品棚の隣接通路マス群を複数始点としてBFS
        def multi_bfs(starts):
            dist = [[-1]*X for _ in range(Y)]
            queue = deque()
            for (sx,sy) in starts:
                dist[sy][sx] = 0
                queue.append((sx,sy))
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < X and 0 <= ny < Y:
                        if dist[ny][nx]==-1 and grid[ny][nx] == '.':
                            dist[ny][nx] = dist[y][x] + 1
                            queue.append( (nx,ny) )
            return dist

        for i in range(m):
            g_i = product_list[i]
            adj_i = product_adj_passages[g_i]
            dist_i = multi_bfs(adj_i)
            for j in range(m):
                if i == j:
                    dist_matrix[i][j] = 0
                    continue
                g_j = product_list[j]
                adj_j = product_adj_passages[g_j]
                min_d = 10**9
                # adj_jの各点からの距離dist_iを調べ、最小値を採用
                for (xj,yj) in adj_j:
                    d = dist_i[yj][xj]
                    if d != -1 and d < min_d:
                        min_d = d
                dist_matrix[i][j] = min_d

        # DPで最大割引額を求める
        # 状態: dp[bit][i] = bitで示された商品の集合を買い、最後にi番目の商品を買った時の最短時間(=移動時間)
        # bit: 0~(1<<m)-1
        # i: 0~m-1
        # 初期はstartから商品iに行く時間start_dist[i]
        # 商品iを買えるのは、その商品のタイムセール開始s <= t <= 終了e-1 の間に可能であること
        # 移動時間は1単位刻みで進み、商品を取る時間は考慮しない

        # ただしtは時間0以上なので、start_dist[i] >= 0であることを確認し、かつその時間に販売時間が間に合うかチェック

        # 最大値問題なので-1は到達不可能を意味する

        INF = 10**9
        dp = [ [-1]*m for _ in range(1<<m) ]

        # 初期化
        for i in range(m):
            if start_dist[i] == -1 or start_dist[i] == INF:
                # 到達不可
                continue
            d_i, s_i, e_i = time_sales[product_list[i]]
            t = start_dist[i]
            # tは商品を取る時間(瞬時)
            # タイムセール開始s_i <= t < e_iで買うことができるか
            # 式は s_i <= t < e_i
            if s_i <= t < e_i:
                dp[1<<i][i] = t

        # bit DPで遷移
        for bit in range(1<<m):
            for i in range(m):
                if dp[bit][i] < 0:
                    continue
                current_time = dp[bit][i]
                for j in range(m):
                    if (bit & (1<<j)) != 0:
                        continue
                    # i -> jへの移動距離
                    dist_ij = dist_matrix[i][j]
                    if dist_ij == -1 or dist_ij == INF:
                        continue
                    nxt_time = current_time + dist_ij
                    d_j, s_j, e_j = time_sales[product_list[j]]
                    # 時間制約判定
                    if s_j <= nxt_time < e_j:
                        if dp[bit|(1<<j)][j] == -1 or dp[bit|(1<<j)][j] > nxt_time:
                            dp[bit|(1<<j)][j] = nxt_time

        # dpから最大割引額合計を求める
        ans = 0
        for bit in range(1<<m):
            # bitに含まれる商品の割引額合計を計算
            discount_sum = 0
            for i in range(m):
                if (bit & (1<<i)) != 0:
                    discount_sum += time_sales[product_list[i]][0]
            # bitで買えるかどうかをdpで判定
            possible = False
            for i in range(m):
                if dp[bit][i] != -1:
                    possible = True
                    break
            if possible and discount_sum > ans:
                ans = discount_sum

        print(ans)

if __name__ == '__main__':
    main()