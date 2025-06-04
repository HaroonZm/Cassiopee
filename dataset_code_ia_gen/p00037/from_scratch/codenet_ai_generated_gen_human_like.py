# 入力を受け取る
horizontal_walls = [input() for _ in range(5)]  # 横の壁：0,2,4,6,8行目
vertical_walls = [input() for _ in range(4)]    # 縦の壁：1,3,5,7行目

# 格子のサイズは横方向にlen(horizontal_walls[0]) - 1、縦方向に5
W = len(horizontal_walls[0]) - 1  # 横の区画数
H = 5                           # 縦の区画数

# 格子点の座標系を設定：左上が(0,0)、右方向がx+1、下方向がy+1
# 点Aは最上段の左端 (0,0)
# 壁情報を整理
# horizontal_walls[y][x]は、点(x,y)から点(x+1,y)の上側の壁の有無（yは0,2,4,6,8行目に対応）
# vertical_walls[y][x]は、点(x,y)から点(x,y+1)の左側の壁の有無（yは1,3,5,7行目に対応）

# 上・右・下・左の方向定義と移動ベクトル
dirs = {
    0: (1, 0),   # 右
    1: (0, 1),   # 下
    2: (-1, 0),  # 左
    3: (0, -1),  # 上
}

# 右手を壁につけて歩く 方向転換の優先順位は右→前→左→後ろ
# 右手方向 = (current_direction + 1) % 4
# 前 = current_direction
# 左 = (current_direction + 3) % 4
# 後ろ = (current_direction + 2) % 4

# 点の座標は(0<=x<=W,0<=y<=H)

def has_wall(px, py, direction):
    # 点(px,py)からdirection方向への壁があるか判定
    # direction 0:右,1:下,2:左,3:上
    if direction == 0:  # 右向きの壁は horizontal_walls[2*py][px]で判定
        # horizontal_wallsは5行、長さはW+1 横線の壁は5段階、地点は0からW
        # ここでは横線の壁は上方向としているため右方向は縦の壁として判定すべき
        # 右壁は vertical_walls[py][px]で判定、pyは0～3で縦壁は4行
        if py >= H or px >= W:
            return True  # 境界外は壁
        return vertical_walls[py][px] == '1'
    elif direction == 1:  # 下向きの壁は horizontal_walls[2*py+2][px]で判定
        if py >= H or px > W:
            return True
        return horizontal_walls[py * 2 + 2][px] == '1'
    elif direction == 2:  # 左向きは vertical_walls[py][px-1]
        if py >= H or px <= 0:
            return True
        return vertical_walls[py][px-1] == '1'
    else:  # 上向きは horizontal_walls[2*py][px]
        if py <= 0 or px > W:
            return True
        return horizontal_walls[(py)*2][px] == '1'

# 初期状態
x, y = 0, 0
d = 3  # 上向き(0:右,1:下,2:左,3:上)

# 最初に右に1区画進む（この壁は必ずある）
if not has_wall(x, y, 0):
    # 通常問題の設定的にここは常にTrueのはずだが念のため
    pass
else:
    # 右に1歩進む
    x += dirs[0][0]
    y += dirs[0][1]
    d = 0  # 右向きに向きを変える

path = 'R'  # 最初の移動

# 移動開始点と方向記憶のために開始位置と方向を保存
start = (0,0,0)  # Aの位置は(0,0)で右向き (壁に右手をついた状態)
# ただし問題では点Aは左上(0,0)で初期方向は上向き(3)で、最初に右に1歩行くので方向は右(0)

# 現在の位置と方向を更新（初期では1移動済み、x=1,y=0,d=0）

# 終了判定はx,y,dがスタートのものと一致した時

while True:
    # 右手方向を見る
    right = (d + 1) % 4
    # 右手方向に進めるか(壁がないか)checking
    nx = x + dirs[right][0]
    ny = y + dirs[right][1]
    if not has_wall(x, y, right):
        # 右に曲がって進む
        d = right
        x = nx
        y = ny
        path += 'R' if d == 0 else 'D' if d == 1 else 'L' if d == 2 else 'U'
    elif not has_wall(x, y, d):
        # 右に曲がれないが前には進める
        x += dirs[d][0]
        y += dirs[d][1]
        path += 'R' if d == 0 else 'D' if d == 1 else 'L' if d == 2 else 'U'
    else:
        # 右手も前も行けないなら左へ曲がるか後ろ向きに曲がる
        # 調べる左方向と後ろ方向の優先順位で曲がる
        ld = (d + 3) % 4
        if not has_wall(x, y, ld):
            # 左に曲がる
            d = ld
            x += dirs[d][0]
            y += dirs[d][1]
            path += 'R' if d == 0 else 'D' if d == 1 else 'L' if d == 2 else 'U'
        else:
            # 後ろ(180度)に曲がって一歩進む
            back = (d + 2) % 4
            if not has_wall(x, y, back):
                d = back
                x += dirs[d][0]
                y += dirs[d][1]
                path += 'R' if d == 0 else 'D' if d == 1 else 'L' if d == 2 else 'U'
            else:
                # どこにも行けない場合は終了（通常ここは起こらない）
                break

    # スタートに戻ったか
    if x == 0 and y == 0 and d == 0:
        break

print(path)