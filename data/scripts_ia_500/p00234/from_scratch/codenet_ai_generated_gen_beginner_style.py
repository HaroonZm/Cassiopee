import sys
sys.setrecursionlimit(1000000)

def solve():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        W,H = map(int,line.strip().split())
        if W == 0 and H == 0:
            break
        f = int(sys.stdin.readline())
        m = int(sys.stdin.readline())
        o = int(sys.stdin.readline())
        grid = []
        for _ in range(H):
            row = []
            count = 0
            while count < W:
                parts = sys.stdin.readline().strip().split()
                for val in parts:
                    row.append(int(val))
                    count += 1
            grid.append(row)

        # 状態管理：座標(x,y), 酸素量(oxygen), 補給済の酸素セルの状態(bitmask)
        # 酸素セルを番号付ける
        ox_cells = {}
        ox_id = 0
        for y in range(H):
            for x in range(W):
                if grid[y][x] > 0:
                    ox_cells[(x,y)] = ox_id
                    ox_id += 1

        from collections import deque

        # 掘り始めはy=0のいずれかのセル（1行目）
        # 掘り進む目標はy=H-1のいずれかのセル（最下行）
        # 動ける方向：左右、下
        # 酸素量が0になると移動も掘ることもできない。
        # 移動するたびに酸素1減る。
        # 酸素セルについたら必ず補給（補給したらそのセルは使えなくなる）
        # 掘るには土セルの費用がかかる。酸素セルは掘る必要なし（費用0）
        # 初期酸素量o
        # 容量mを超えた酸素は破棄。
        # 掘り進むとは、そのセルに到達すること。
        # コストがfを超えるならNA

        # 状態メモ：[x,y,oxygen,used_oxygen_bitmask] -> cost
        from collections import defaultdict
        visited = {}

        # 初期地点はy=0のいずれかのセル。そこから掘り始める
        # いずれも最初の酸素補給はなし（最初にいるセルでは補給しない）
        # 移動はこのセルに行く判定なので酸素減る。だが最初のセルは掘り始める地点なので酸素減らずコストも発生しないとみなす
        # 問題文的に最初のセルの掘削費用はかかる？「一番小さいyのセルのうち一つを選んでそこから掘り始める」なのでそのセルも掘らないといけない(費用かかる)はず
        # だが酸素はその場で減らない（一歩目の移動ではない）
        # よって初期状態ではコストにそのセルの費用（土セルなら費用）、酸素量o、そのセルの酸素補給ありなら補給することになるが補給は「そのセルに辿りついたら必ず補給」なので最初のセルも補給しなければならない

        # よって初期状態:
        # - 土セルなら費用かかる
        # - 酸素セルなら酸素を補給してから開始（酸素量増加し、補給済み管理）
        # - 移動したわけではないので酸素減らない

        # 探索
        from heapq import heappush, heappop

        start_states = []
        for x0 in range(W):
            y0 = 0
            cell = grid[y0][x0]
            # 初期酸素量
            oxygen = o
            used_mask = 0
            cost = 0
            if cell < 0:
                # 土セル 掘る費用かかる
                cost = -cell
                if cost > f:
                    continue
            else:
                # 酸素セル 補給しなければならない
                ox_index = ox_cells[(x0,y0)]
                oxygen += cell
                if oxygen > m:
                    oxygen = m
                used_mask |= (1 << ox_index)
            # 状態
            key = (x0,y0,oxygen,used_mask)
            if key not in visited or visited[key] > cost:
                visited[key] = cost
                heappush(start_states,(cost,x0,y0,oxygen,used_mask))

        ans = None
        while start_states:
            cost,x,y,oxygen,used_mask = heappop(start_states)
            # 目標の深さに到達かつ酸素>0なら成功
            if y == H-1 and oxygen > 0:
                if ans is None or ans > cost:
                    ans = cost
                continue
            # 掘るセルは現在位置なので費用はすでに払っている

            # 移動候補：左、右、下
            # 移動するたびに酸素減る
            moves = []
            if x-1 >= 0:
                moves.append((x-1,y))
            if x+1 < W:
                moves.append((x+1,y))
            if y+1 < H:
                moves.append((x,y+1))
            for nx,ny in moves:
                no = oxygen - 1
                if no <= 0:
                    continue
                ncell = grid[ny][nx]
                nused_mask = used_mask
                ncost = cost
                if ncell < 0:
                    # 土セル 掘る費用かかる
                    ncost += -ncell
                    if ncost > f:
                        continue
                else:
                    # 酸素セル
                    ox_i = ox_cells[(nx,ny)]
                    if (used_mask & (1 << ox_i)) == 0:
                        # 未補給なら補給必須
                        no += ncell
                        if no > m:
                            no = m
                        nused_mask = used_mask | (1 << ox_i)
                    else:
                        # 既に補給済みは費用なし酸素補給なし
                        pass
                nkey = (nx,ny,no,nused_mask)
                if nkey not in visited or visited[nkey] > ncost:
                    visited[nkey] = ncost
                    heappush(start_states,(ncost,nx,ny,no,nused_mask))

        if ans is None or ans > f:
            print("NA")
        else:
            print(ans)

if __name__ == "__main__":
    solve()