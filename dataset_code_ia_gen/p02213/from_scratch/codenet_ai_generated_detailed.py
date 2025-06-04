from collections import deque

# サイコロの状態を表すクラスを定義
class Dice:
    def __init__(self, bottom=6, front=2, right=3):
        # bottom: 底面の数字
        # front: 前面の数字 (iの増加方向)
        # right: 右面の数字 (jの増加方向)
        self.bottom = bottom
        self.front = front
        self.right = right

    def roll_north(self):
        # サイコロを北方向(前面方向とは逆)に転がしたときの状態変化
        # 新しい底面は今の前面
        # 新しい前面は今の上面、上面は6面中 7-(底面)
        top = 7 - self.bottom
        self.bottom, self.front = self.front, top
        # rightは変わらない

    def roll_south(self):
        # サイコロを南方向(前面方向)に転がしたときの状態変化
        top = 7 - self.bottom
        self.bottom, self.front = top, self.bottom
        # rightは変わらない

    def roll_west(self):
        # サイコロを西方向(右面とは逆)に転がしたときの状態変化
        top = 7 - self.bottom
        self.bottom, self.right = self.right, top
        # frontは変わらない

    def roll_east(self):
        # サイコロを東方向(右面方向)に転がしたときの状態変化
        top = 7 - self.bottom
        self.bottom, self.right = top, self.bottom
        # frontは変わらない

    def copy(self):
        # 深いコピーを返す
        d = Dice()
        d.bottom = self.bottom
        d.front = self.front
        d.right = self.right
        return d

def solve():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    # スタートは(0,0)、底面6、前面2、右面3
    start = (0, 0)
    dice_start = Dice(bottom=6, front=2, right=3)

    # 移動は上下左右 (前面はiの増加方向、右面はjの増加方向)
    moves = [(-1, 0, 'N'), (1, 0, 'S'), (0, -1, 'W'), (0, 1, 'E')]

    # 探索のため状態管理
    # 状態は (i, j, bottom, front, right)
    visited = set()
    queue = deque()

    # 初期状態をセット
    visited.add((0, 0, dice_start.bottom, dice_start.front, dice_start.right))
    queue.append((0, 0, dice_start))

    while queue:
        i, j, dice = queue.popleft()

        # ゴール判定
        if i == H-1 and j == W-1:
            print("YES")
            return

        for di, dj, direction in moves:
            ni, nj = i + di, j + dj

            # 範囲外判定
            if not (0 <= ni < H and 0 <= nj < W):
                continue

            # '#'判定
            if grid[ni][nj] == '#':
                continue

            # サイコロの状態をコピーして転がす
            new_dice = dice.copy()
            if direction == 'N':
                new_dice.roll_north()
            elif direction == 'S':
                new_dice.roll_south()
            elif direction == 'W':
                new_dice.roll_west()
            else:  # 'E'
                new_dice.roll_east()

            # 転がした後、底面の数字とマスの数字が一致するかチェック
            # マスは数字なので文字列からintに変換
            cell_num = int(grid[ni][nj])
            if new_dice.bottom != cell_num:
                continue

            state = (ni, nj, new_dice.bottom, new_dice.front, new_dice.right)
            if state not in visited:
                visited.add(state)
                queue.append((ni, nj, new_dice))

    # 到達できなければNO
    print("NO")

if __name__ == "__main__":
    solve()