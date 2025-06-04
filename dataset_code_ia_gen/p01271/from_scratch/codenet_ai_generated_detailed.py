import sys
from collections import deque

def solve():
    # 読み込みを高速化するためにsys.stdinを使う
    input = sys.stdin.readline

    # 移動方向（北, 東, 西, 南）
    # 左右対称の移動とは
    # 北 - 北, 南 - 南, 西 - 東, 東 - 西 に同時に動くこと
    # よって、左の部屋の動きをdx, dyとすると右の部屋の動きは、
    # 北(0,-1) <-> 北(0,-1)
    # 南(0, 1) <-> 南(0, 1)
    # 西 (-1,0) <-> 東 (1, 0)
    # 東 (1, 0) <-> 西 (-1,0)
    moves = [
        (0, -1, 0, -1),  # 北 - 北
        (0, 1, 0, 1),    # 南 - 南
        (-1, 0, 1, 0),   # 西 - 東
        (1, 0, -1, 0)    # 東 - 西
    ]

    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        # 左の部屋と右の部屋のマップを読み込み
        roomL = []
        roomR = []
        for _ in range(H):
            line = input().rstrip('\n').split()
            roomL.append(line[0])
            roomR.append(line[1])

        # 初期位置と目的地の情報取得
        # 左の部屋はLenの初期位置と目的地'%'
        # 右の部屋はRinの初期位置と目的地'%'
        # それぞれ1つずつ存在
        startL = None
        startR = None
        goalL = None
        goalR = None

        for y in range(H):
            for x in range(W):
                cL = roomL[y][x]
                cR = roomR[y][x]
                if cL == 'L':
                    startL = (x, y)
                if cR == 'R':
                    startR = (x, y)
                if cL == '%':
                    goalL = (x, y)
                if cR == '%':
                    goalR = (x, y)

        # BFSで探索する
        # 状態は (左の部屋のx,y, 右の部屋のx,y)
        # すでに訪れた状態を記録し、重複探索を避ける
        visited = set()
        visited.add((startL[0], startL[1], startR[0], startR[1]))
        q = deque()
        q.append((startL[0], startL[1], startR[0], startR[1]))

        def can_move(room, x, y):
            # 範囲内かつ壁じゃないか
            return 0 <= x < W and 0 <= y < H and room[y][x] != '#'

        success = False
        while q:
            lx, ly, rx, ry = q.popleft()

            # 両方が目的地に到達したら成功
            if (lx, ly) == goalL and (rx, ry) == goalR:
                success = True
                break

            # 4方向の同時移動を試す
            for dlx, dly, drx, dry in moves:
                # 左右対称移動の計算ルール
                nlx, nly = lx + dlx, ly + dly
                nrx, nry = rx + drx, ry + dry

                # 左右室の壁や範囲判定。壁ならその場に留まるルール
                if not can_move(roomL, nlx, nly):
                    nlx, nly = lx, ly
                if not can_move(roomR, nrx, nry):
                    nrx, nry = rx, ry

                # すでに訪れたかチェック
                state = (nlx, nly, nrx, nry)
                if state in visited:
                    continue
                visited.add(state)
                q.append(state)

        print("Yes" if success else "No")

if __name__ == "__main__":
    solve()