# ブレイブ・フォース・ストーリー問題の解法
# 「正6角形のマス目上で、指定ターン数以内に到達可能なマスの数を求める」
#
# アプローチ：
# 1. 入力ごとにデータセットを読み込む。
# 2. 障害物をセットで管理し、探索時に進入禁止判定に使用する。
# 3. スタート地点から幅優先探索(BFS)を行い、ターン数以内に到達可能なマスをすべて列挙する。
# 4. 正6角形の座標系に従い、隣接マスの座標差を適用して探索を行う。
# 5. 到達可能なマスの数を出力する。
#
# 注意点：
# - 入力に0 0が現れたら終了。
# - 最大絶対座標が30なので、座標の管理は辞書やセットで十分高速。

import sys
from collections import deque

# 正6角形の隣接座標リスト
# 問題図より隣接は6方向で以下の通り
# (x+1, y) (x-1, y) (x, y+1) (x, y-1) (x+1, y-1) (x-1, y+1)
directions = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,1)]

def main():
    input = sys.stdin.readline
    while True:
        # t: ターン数, n: 障害物の数
        line = input().strip()
        if line == '':
            break
        t, n = map(int, line.split())
        if t == 0 and n == 0:
            break

        obstacles = set()
        # 障害物の座標を読み込み
        for _ in range(n):
            x, y = map(int, input().split())
            obstacles.add((x,y))

        # スタート位置
        sx, sy = map(int, input().split())

        # BFSで探索
        # キューには (x, y, 現在のターン数) を格納
        queue = deque()
        queue.append((sx, sy, 0))

        visited = set()
        visited.add((sx, sy))

        while queue:
            x, y, dist = queue.popleft()

            if dist == t:
                # 最大ターン数まで到達したらもう先に進まない
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 障害物でないか、かつまだ訪問していないかを確認
                if (nx, ny) not in obstacles and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist+1))

        # 到達可能なマスの数を出力
        print(len(visited))

if __name__ == "__main__":
    main()