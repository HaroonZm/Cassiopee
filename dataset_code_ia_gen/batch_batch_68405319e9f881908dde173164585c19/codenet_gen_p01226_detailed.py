# バトルタウンのプロトタイプ実装
# 与えられたマップと操作列に基づいて戦車の移動と射撃をシミュレーションし、最終マップを出力する。

def battle_town():
    import sys

    input = sys.stdin.readline

    # 戦車の向きを管理するための辞書
    # key: 操作文字 ('U','D','L','R')
    # value: (向き文字, 移動方向のdelta(y,x))
    direction_map = {
        'U': ('^', (-1, 0)),
        'D': ('v', (1, 0)),
        'L': ('<', (0, -1)),
        'R': ('>', (0, 1))
    }

    # 戦車の向き記号 → 方向移動 (y,x)
    tank_dir = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    T = int(input())
    for test_num in range(T):
        H, W = map(int, input().split())
        # マップをリストのリスト(行列)で保持
        board = [list(input().rstrip('\n')) for _ in range(H)]

        # 戦車の位置と向きを探索
        tank_y, tank_x, tank_facing = -1, -1, None
        for y in range(H):
            for x in range(W):
                if board[y][x] in ['^','v','<','>']:
                    tank_y, tank_x = y, x
                    tank_facing = board[y][x]
                    break
            if tank_facing is not None:
                break

        N = int(input())
        commands = input().rstrip('\n')

        # コマンドを順に処理
        for cmd in commands:
            if cmd in ['U','D','L','R']:
                # 向きを変更
                new_facing, (dy, dx) = direction_map[cmd]
                tank_facing = new_facing
                # 移動可能なら移動
                ny, nx = tank_y + dy, tank_x + dx
                if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
                    # 移動前のマスは平地に戻る
                    board[tank_y][tank_x] = '.'
                    tank_y, tank_x = ny, nx
                # 戦車の現在位置に向き文字をセット
                board[tank_y][tank_x] = tank_facing

            elif cmd == 'S':
                # 発射処理
                dy, dx = tank_dir[tank_facing]
                by, bx = tank_y, tank_x
                while True:
                    by += dy
                    bx += dx
                    if not (0 <= by < H and 0 <= bx < W):
                        # マップ外に出ると砲弾消滅
                        break
                    cell = board[by][bx]
                    if cell == '*':
                        # レンガの壁に命中→壁破壊（平地に変える）、砲弾消滅
                        board[by][bx] = '.'
                        break
                    elif cell == '#':
                        # 鉄の壁に命中→壁は変化せず砲弾消滅
                        break
                    else:
                        # その他は通過可能。(*以外の壁なら打ち止めだが、他マスは平地(.)や戦車がいないため通過)
                        continue

        # 出力
        for row in board:
            print(''.join(row))
        if test_num != T-1:
            print()  # データセット間に空行を出す

if __name__ == '__main__':
    battle_town()